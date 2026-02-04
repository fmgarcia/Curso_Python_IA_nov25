# 🏥 Sistema de Detección de Tumores con IA

Aplicación web completa para un centro médico que utiliza Inteligencia Artificial para la detección de tumores mamarios (Benigno/Maligno) utilizando el dataset `load_breast_cancer` de scikit-learn.

## 📁 Estructura del Proyecto

```
Proyecto_completo/
├── backend/
│   ├── main.py                    # API FastAPI
│   ├── requirements.txt           # Dependencias Python
│   ├── models/
│   │   ├── __init__.py
│   │   ├── random_forest.py       # RandomForestClassifier
│   │   ├── xgboost_model.py       # XGBClassifier
│   │   ├── adaboost.py            # AdaBoostClassifier
│   │   ├── gradient_boosting.py   # GradientBoostingClassifier
│   │   └── voting_model.py        # VotingClassifier
│   └── weights/                   # Carpeta para guardar modelos entrenados
│
└── frontend/
    ├── package.json
    ├── public/
    │   ├── index.html
    │   └── manifest.json
    └── src/
        ├── App.js                 # Componente principal
        ├── index.js               # Punto de entrada
        ├── index.css              # Estilos globales
        ├── context/
        │   └── AppContext.js      # Estado global con Context API
        └── components/
            ├── ModelSelector.js   # Selector y entrenamiento de modelos
            ├── PredictionForm.js  # Formulario con los 30 campos
            └── PredictionResult.js # Visualización de resultados
```

## 🚀 Instrucciones de Instalación y Ejecución

### Prerrequisitos
- Python 3.8 o superior
- Node.js 16 o superior
- npm o yarn

### Backend (FastAPI)

1. **Navegar a la carpeta del backend:**
   ```bash
   cd backend
   ```

2. **Crear un entorno virtual (recomendado):**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar el servidor:**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

   El backend estará disponible en: `http://localhost:8000`
   
   Documentación interactiva (Swagger): `http://localhost:8000/docs`

### Frontend (React)

1. **Abrir una nueva terminal y navegar a la carpeta del frontend:**
   ```bash
   cd frontend
   ```

2. **Instalar dependencias:**
   ```bash
   npm install
   ```

3. **Ejecutar la aplicación:**
   ```bash
   npm start
   ```

   El frontend estará disponible en: `http://localhost:3000`

## 📡 API Endpoints

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/` | Información de la API |
| GET | `/models` | Lista de modelos disponibles y su estado |
| GET | `/features` | Lista de características requeridas |
| GET | `/sample-data` | Datos de ejemplo para pruebas |
| POST | `/train/{model_name}` | Entrena el modelo especificado |
| POST | `/predict` | Realiza una predicción |

### Modelos Disponibles
- `random_forest` - Random Forest Classifier
- `xgboost` - XGBoost Classifier
- `adaboost` - AdaBoost Classifier
- `gradient_boosting` - Gradient Boosting Classifier
- `voting` - Voting Classifier (DecisionTree + LogisticRegression + KNN)

## 🔬 Características del Dataset

El formulario requiere 30 características organizadas en 3 categorías:

### Valores Medios (Mean)
- mean radius, mean texture, mean perimeter, mean area
- mean smoothness, mean compactness, mean concavity
- mean concave points, mean symmetry, mean fractal dimension

### Errores Estándar (Error)
- radius error, texture error, perimeter error, area error
- smoothness error, compactness error, concavity error
- concave points error, symmetry error, fractal dimension error

### Valores Peores/Máximos (Worst)
- worst radius, worst texture, worst perimeter, worst area
- worst smoothness, worst compactness, worst concavity
- worst concave points, worst symmetry, worst fractal dimension

## 🎯 Flujo de Uso

1. **Iniciar Backend y Frontend** (en terminales separadas)
2. **Seleccionar un modelo** en el panel de control
3. **Entrenar el modelo** haciendo clic en "Entrenar"
4. **Ingresar datos del tumor** o cargar datos de ejemplo
5. **Realizar predicción** y ver el resultado

## 📊 Resultados de la Predicción

- **Benigno** (target = 1): Se muestra en verde con probabilidades
- **Maligno** (target = 0): Se muestra en rojo con alerta

## ⚠️ Notas Importantes

- Los modelos se guardan localmente en archivos `.joblib` dentro de `backend/weights/`
- Este sistema es educativo y no sustituye el diagnóstico médico profesional
- El dataset Wisconsin Breast Cancer contiene 569 muestras con 30 características

## 🛠️ Tecnologías Utilizadas

### Backend
- FastAPI
- scikit-learn
- XGBoost
- Pandas, NumPy
- Joblib

### Frontend
- React 18
- Context API (Estado global)
- Axios
- CSS3 (Gradientes, Animaciones)
