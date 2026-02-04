# pyright: reportMissingImports=false, reportGeneralTypeIssues=false
"""
API FastAPI para detección de tumores (Benigno/Maligno)
Centro Médico - Sistema de Inteligencia Artificial
"""
import os
import io
import random
from fastapi import FastAPI, HTTPException, UploadFile, File  # type: ignore
from fastapi.middleware.cors import CORSMiddleware  # type: ignore
from fastapi.responses import StreamingResponse  # type: ignore
from pydantic import BaseModel  # type: ignore
from typing import Dict, Any, List, Optional
from sklearn.datasets import load_breast_cancer  # type: ignore
import pandas as pd  # type: ignore
import numpy as np  # type: ignore

# Importar módulos de modelos
from models import random_forest, xgboost_model, adaboost, gradient_boosting, voting_model

app = FastAPI(
    title="API Detección de Tumores",
    description="Sistema de IA para detección de tumores mamarios (Benigno/Maligno)",
    version="1.0.0"
)

# Configurar CORS para permitir conexiones desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mapeo de nombres de modelos a módulos
MODELS = {
    "random_forest": random_forest,
    "xgboost": xgboost_model,
    "adaboost": adaboost,
    "gradient_boosting": gradient_boosting,
    "voting": voting_model
}

# Obtener nombres de características del dataset
FEATURE_NAMES = load_breast_cancer().feature_names.tolist()  # type: ignore

# Almacenamiento temporal del dataset personalizado
CUSTOM_DATASET_PATH = os.path.join(os.path.dirname(__file__), 'uploads', 'custom_dataset.csv')
current_dataset_info = {"name": "Wisconsin Breast Cancer (Original)", "samples": 569, "is_custom": False}


class SyntheticDataRequest(BaseModel):
    """Esquema para solicitud de generación de datos sintéticos"""
    num_samples: int
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "num_samples": 100
            }
        }
    }


class PredictionRequest(BaseModel):
    """Esquema para solicitud de predicción"""
    model_name: str
    features: Dict[str, float]
    
    model_config = {
        "protected_namespaces": (),
        "json_schema_extra": {
            "example": {
                "model_name": "random_forest",
                "features": {
                    "mean radius": 17.99,
                    "mean texture": 10.38,
                    "mean perimeter": 122.8,
                    "mean area": 1001.0,
                    "mean smoothness": 0.1184,
                    "mean compactness": 0.2776,
                    "mean concavity": 0.3001,
                    "mean concave points": 0.1471,
                    "mean symmetry": 0.2419,
                    "mean fractal dimension": 0.07871,
                    "radius error": 1.095,
                    "texture error": 0.9053,
                    "perimeter error": 8.589,
                    "area error": 153.4,
                    "smoothness error": 0.006399,
                    "compactness error": 0.04904,
                    "concavity error": 0.05373,
                    "concave points error": 0.01587,
                    "symmetry error": 0.03003,
                    "fractal dimension error": 0.006193,
                    "worst radius": 25.38,
                    "worst texture": 17.33,
                    "worst perimeter": 184.6,
                    "worst area": 2019.0,
                    "worst smoothness": 0.1622,
                    "worst compactness": 0.6656,
                    "worst concavity": 0.7119,
                    "worst concave points": 0.2654,
                    "worst symmetry": 0.4601,
                    "worst fractal dimension": 0.1189
                }
            }
        }
    }


class TrainResponse(BaseModel):
    """Esquema para respuesta de entrenamiento"""
    model: str
    accuracy: float
    message: str


class PredictionResponse(BaseModel):
    """Esquema para respuesta de predicción"""
    prediction: str
    probability_malignant: float
    probability_benign: float


class ModelStatus(BaseModel):
    """Esquema para estado de modelo"""
    name: str
    display_name: str
    trained: bool
    accuracy: Optional[float] = None


@app.get("/", tags=["Info"])
async def root():
    """Endpoint raíz con información de la API"""
    return {
        "title": "API Detección de Tumores",
        "description": "Sistema de IA para detección de tumores mamarios",
        "version": "1.0.0",
        "endpoints": {
            "GET /models": "Lista de modelos disponibles",
            "POST /train/{model_name}": "Entrenar un modelo",
            "POST /predict": "Realizar predicción",
            "GET /features": "Lista de características requeridas"
        }
    }


@app.get("/models", response_model=List[ModelStatus], tags=["Modelos"])
async def get_models():
    """
    Obtiene la lista de modelos disponibles y su estado (entrenado/no entrenado)
    """
    display_names = {
        "random_forest": "Random Forest",
        "xgboost": "XGBoost",
        "adaboost": "AdaBoost",
        "gradient_boosting": "Gradient Boosting",
        "voting": "Voting Classifier"
    }
    
    models_status = []
    for name, module in MODELS.items():
        is_trained = module.is_trained()
        accuracy = module.get_accuracy() if is_trained else None
        models_status.append(ModelStatus(
            name=name,
            display_name=display_names.get(name, name),
            trained=is_trained,
            accuracy=accuracy
        ))
    
    return models_status


@app.get("/features", tags=["Info"])
async def get_features():
    """
    Obtiene la lista de características (features) requeridas para la predicción
    Organizadas por categorías: Mean, Error, Worst
    """
    # Organizar features por categorías
    mean_features = [f for f in FEATURE_NAMES if f.startswith("mean")]
    error_features = [f for f in FEATURE_NAMES if "error" in f]
    worst_features = [f for f in FEATURE_NAMES if f.startswith("worst")]
    
    return {
        "total_features": len(FEATURE_NAMES),
        "feature_names": FEATURE_NAMES,
        "categories": {
            "mean": mean_features,
            "error": error_features,
            "worst": worst_features
        }
    }


@app.post("/train/{model_name}", response_model=TrainResponse, tags=["Entrenamiento"])
async def train_model(model_name: str):
    """
    Entrena el modelo especificado y guarda los pesos localmente
    
    - **model_name**: Nombre del modelo a entrenar (random_forest, xgboost, adaboost, gradient_boosting, voting)
    """
    if model_name not in MODELS:
        raise HTTPException(
            status_code=404,
            detail=f"Modelo '{model_name}' no encontrado. Modelos disponibles: {list(MODELS.keys())}"
        )
    
    try:
        result = MODELS[model_name].train()
        return TrainResponse(**result)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al entrenar el modelo: {str(e)}"
        )


@app.post("/predict", response_model=PredictionResponse, tags=["Predicción"])
async def predict(request: PredictionRequest):
    """
    Realiza una predicción de tumor (Benigno/Maligno) usando el modelo especificado
    
    - **model_name**: Nombre del modelo a usar
    - **features**: Diccionario con los 30 parámetros del tumor
    """
    if request.model_name not in MODELS:
        raise HTTPException(
            status_code=404,
            detail=f"Modelo '{request.model_name}' no encontrado. Modelos disponibles: {list(MODELS.keys())}"
        )
    
    # Verificar que el modelo esté entrenado
    if not MODELS[request.model_name].is_trained():
        raise HTTPException(
            status_code=400,
            detail=f"El modelo '{request.model_name}' no ha sido entrenado. Ejecute POST /train/{request.model_name} primero."
        )
    
    # Verificar que se proporcionen todas las características
    missing_features = set(FEATURE_NAMES) - set(request.features.keys())
    if missing_features:
        raise HTTPException(
            status_code=400,
            detail=f"Faltan las siguientes características: {list(missing_features)}"
        )
    
    try:
        result = MODELS[request.model_name].predict(request.features)
        return PredictionResponse(**result)
    except FileNotFoundError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al realizar la predicción: {str(e)}"
        )


@app.get("/sample-data", tags=["Info"])
async def get_sample_data():
    """
    Obtiene datos de ejemplo del dataset para pruebas
    Retorna un caso benigno y un caso maligno
    """
    data = load_breast_cancer(as_frame=True)
    df = data.frame  # type: ignore
    
    # Obtener un caso maligno (target=0) y uno benigno (target=1)
    malignant_sample = df[df['target'] == 0].iloc[0].drop('target').to_dict()
    benign_sample = df[df['target'] == 1].iloc[0].drop('target').to_dict()
    
    return {
        "malignant_example": malignant_sample,
        "benign_example": benign_sample
    }


@app.get("/random-sample", tags=["Info"])
async def get_random_sample():
    """
    Genera un caso aleatorio realista basado en las estadísticas del dataset.
    Los valores se generan dentro del rango real de cada característica
    con una distribución normal alrededor de la media.
    """
    data = load_breast_cancer(as_frame=True)
    df = data.frame.drop(columns=['target'])  # type: ignore
    
    # Calcular estadísticas por columna
    stats = df.describe()
    
    random_sample = {}
    for col in df.columns:
        mean_val = stats.loc['mean', col]
        std_val = stats.loc['std', col]
        min_val = stats.loc['min', col]
        max_val = stats.loc['max', col]
        
        # Generar valor con distribución normal, limitado al rango real
        value = random.gauss(mean_val, std_val * 0.8)
        value = max(min_val, min(max_val, value))  # Clamp al rango
        random_sample[col] = round(value, 4)
    
    return {"random_sample": random_sample}


@app.get("/dataset-info", tags=["Dataset"])
async def get_dataset_info():
    """
    Obtiene información sobre el dataset actual que se usará para entrenamiento.
    """
    global current_dataset_info
    return current_dataset_info


@app.post("/upload-dataset", tags=["Dataset"])
async def upload_dataset(file: UploadFile = File(...)):
    """
    Sube un dataset personalizado en formato CSV para entrenar los modelos.
    El CSV debe tener las 30 características + columna 'target' (0=Maligno, 1=Benigno).
    """
    global current_dataset_info
    
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="El archivo debe ser un CSV")
    
    try:
        # Leer el contenido del archivo
        contents = await file.read()
        df = pd.read_csv(io.BytesIO(contents))
        
        # Verificar que tenga las columnas correctas
        required_columns = set(FEATURE_NAMES + ['target'])
        actual_columns = set(df.columns)
        
        missing_columns = required_columns - actual_columns
        if missing_columns:
            raise HTTPException(
                status_code=400,
                detail=f"El dataset no tiene las columnas requeridas. Faltan: {list(missing_columns)}"
            )
        
        # Verificar valores de target
        if not df['target'].isin([0, 1]).all():
            raise HTTPException(
                status_code=400,
                detail="La columna 'target' debe contener solo valores 0 (Maligno) o 1 (Benigno)"
            )
        
        # Guardar el dataset
        os.makedirs(os.path.dirname(CUSTOM_DATASET_PATH), exist_ok=True)
        df.to_csv(CUSTOM_DATASET_PATH, index=False)
        
        # Actualizar información del dataset
        current_dataset_info = {
            "name": file.filename,
            "samples": len(df),
            "is_custom": True,
            "malignant_count": int((df['target'] == 0).sum()),
            "benign_count": int((df['target'] == 1).sum())
        }
        
        return {
            "message": f"Dataset '{file.filename}' cargado correctamente",
            "dataset_info": current_dataset_info
        }
        
    except pd.errors.EmptyDataError:
        raise HTTPException(status_code=400, detail="El archivo CSV está vacío")
    except pd.errors.ParserError:
        raise HTTPException(status_code=400, detail="Error al parsear el archivo CSV")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar el archivo: {str(e)}")


@app.post("/reset-dataset", tags=["Dataset"])
async def reset_dataset():
    """
    Resetea el dataset al original de Wisconsin Breast Cancer.
    """
    global current_dataset_info
    
    # Eliminar dataset personalizado si existe
    if os.path.exists(CUSTOM_DATASET_PATH):
        os.remove(CUSTOM_DATASET_PATH)
    
    current_dataset_info = {
        "name": "Wisconsin Breast Cancer (Original)",
        "samples": 569,
        "is_custom": False
    }
    
    return {
        "message": "Dataset reseteado al original",
        "dataset_info": current_dataset_info
    }


@app.post("/generate-synthetic-data", tags=["Dataset"])
async def generate_synthetic_data(request: SyntheticDataRequest):
    """
    Genera un dataset sintético realista basado en las estadísticas del dataset original.
    Retorna un archivo CSV descargable.
    """
    if request.num_samples < 1:
        raise HTTPException(status_code=400, detail="El número de muestras debe ser al menos 1")
    
    if request.num_samples > 10000:
        raise HTTPException(status_code=400, detail="El número máximo de muestras es 10000")
    
    # Cargar dataset original para obtener estadísticas
    data = load_breast_cancer(as_frame=True)
    df_original = data.frame  # type: ignore
    
    # Separar por clase para generar datos más realistas
    df_malignant = df_original[df_original['target'] == 0].drop(columns=['target'])
    df_benign = df_original[df_original['target'] == 1].drop(columns=['target'])
    
    stats_malignant = df_malignant.describe()
    stats_benign = df_benign.describe()
    
    # Calcular correlaciones del dataset original para mantener coherencia
    corr_matrix = df_original.drop(columns=['target']).corr()
    
    synthetic_data = []
    
    # Generar proporción similar al original (~37% maligno, ~63% benigno)
    malignant_ratio = 0.37
    
    for i in range(request.num_samples):
        is_malignant = random.random() < malignant_ratio
        stats = stats_malignant if is_malignant else stats_benign
        
        row = {}
        for col in FEATURE_NAMES:
            mean_val = stats.loc['mean', col]
            std_val = stats.loc['std', col]
            min_val = stats.loc['min', col]
            max_val = stats.loc['max', col]
            
            # Añadir algo de ruido para mayor variabilidad
            noise_factor = random.uniform(0.7, 1.3)
            value = random.gauss(mean_val, std_val * noise_factor)
            
            # Asegurar valores no negativos y dentro de un rango razonable
            value = max(min_val * 0.5, min(max_val * 1.5, value))
            value = max(0, value)  # No permitir valores negativos
            
            row[col] = round(value, 6)
        
        row['target'] = 0 if is_malignant else 1
        synthetic_data.append(row)
    
    # Crear DataFrame
    df_synthetic = pd.DataFrame(synthetic_data)
    
    # Reordenar columnas: features + target
    columns_order = FEATURE_NAMES + ['target']
    df_synthetic = df_synthetic[columns_order]
    
    # Convertir a CSV
    csv_buffer = io.StringIO()
    df_synthetic.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)
    
    # Estadísticas del dataset generado
    malignant_count = int((df_synthetic['target'] == 0).sum())
    benign_count = int((df_synthetic['target'] == 1).sum())
    
    # Retornar como archivo descargable
    return StreamingResponse(
        io.BytesIO(csv_buffer.getvalue().encode()),
        media_type="text/csv",
        headers={
            "Content-Disposition": f"attachment; filename=synthetic_tumor_data_{request.num_samples}_samples.csv",
            "X-Synthetic-Info": f"samples:{request.num_samples},malignant:{malignant_count},benign:{benign_count}"
        }
    )


@app.get("/synthetic-preview", tags=["Dataset"])
async def get_synthetic_preview(num_samples: int = 10):
    """
    Genera una vista previa de datos sintéticos (sin descargar).
    Útil para verificar la estructura antes de generar un dataset grande.
    """
    if num_samples < 1 or num_samples > 100:
        raise HTTPException(status_code=400, detail="El número de muestras debe estar entre 1 y 100")
    
    data = load_breast_cancer(as_frame=True)
    df_original = data.frame  # type: ignore
    
    df_malignant = df_original[df_original['target'] == 0].drop(columns=['target'])
    df_benign = df_original[df_original['target'] == 1].drop(columns=['target'])
    
    stats_malignant = df_malignant.describe()
    stats_benign = df_benign.describe()
    
    synthetic_data = []
    
    for i in range(num_samples):
        is_malignant = random.random() < 0.37
        stats = stats_malignant if is_malignant else stats_benign
        
        row = {}
        for col in FEATURE_NAMES:
            mean_val = stats.loc['mean', col]
            std_val = stats.loc['std', col]
            min_val = stats.loc['min', col]
            max_val = stats.loc['max', col]
            
            value = random.gauss(mean_val, std_val * random.uniform(0.7, 1.3))
            value = max(min_val * 0.5, min(max_val * 1.5, value))
            value = max(0, value)
            
            row[col] = round(value, 4)
        
        row['target'] = 0 if is_malignant else 1
        row['diagnosis'] = 'Maligno' if is_malignant else 'Benigno'
        synthetic_data.append(row)
    
    return {
        "preview": synthetic_data,
        "columns": FEATURE_NAMES + ['target', 'diagnosis'],
        "message": f"Vista previa de {num_samples} muestras sintéticas"
    }


if __name__ == "__main__":
    import uvicorn  # type: ignore
    uvicorn.run(app, host="0.0.0.0", port=8000)
