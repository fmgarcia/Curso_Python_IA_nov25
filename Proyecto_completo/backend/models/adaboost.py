# pyright: reportMissingImports=false, reportGeneralTypeIssues=false
"""
AdaBoost Classifier para detección de tumores
Basado en el dataset breast_cancer de scikit-learn
"""
import os
import json
import joblib  # type: ignore
import numpy as np  # type: ignore
import pandas as pd  # type: ignore
from sklearn.datasets import load_breast_cancer  # type: ignore
from sklearn.model_selection import train_test_split  # type: ignore
from sklearn.ensemble import AdaBoostClassifier  # type: ignore
from sklearn.tree import DecisionTreeClassifier  # type: ignore
from sklearn.metrics import accuracy_score  # type: ignore

MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'weights', 'adaboost.joblib')
FEATURE_NAMES_PATH = os.path.join(os.path.dirname(__file__), '..', 'weights', 'feature_names.joblib')
ACCURACY_PATH = os.path.join(os.path.dirname(__file__), '..', 'weights', 'adaboost_accuracy.json')
CUSTOM_DATASET_PATH = os.path.join(os.path.dirname(__file__), '..', 'uploads', 'custom_dataset.csv')


def load_training_data():
    """Carga los datos de entrenamiento (personalizado o original)"""
    if os.path.exists(CUSTOM_DATASET_PATH):
        df = pd.read_csv(CUSTOM_DATASET_PATH)
        dataset_name = "personalizado"
    else:
        df = load_breast_cancer(as_frame=True).frame  # type: ignore
        dataset_name = "original"
    return df, dataset_name


def train():
    """
    Entrena el modelo AdaBoost y guarda los pesos
    Returns:
        dict: Información del entrenamiento (accuracy, mensaje)
    """
    # Cargar datos (personalizado o original)
    df, dataset_name = load_training_data()
    
    X = df.drop(columns=['target'])
    y = df['target']
    
    # Dividir datos
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Entrenar modelo con DecisionTree como estimador base
    model = AdaBoostClassifier(
        estimator=DecisionTreeClassifier(max_depth=10),
        n_estimators=100, 
        random_state=42
    )
    model.fit(X_train, y_train)
    
    # Evaluar
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    # Guardar modelo
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    joblib.dump(list(X.columns), FEATURE_NAMES_PATH)
    
    # Guardar accuracy
    accuracy_pct = round(accuracy * 100, 2)
    with open(ACCURACY_PATH, 'w') as f:
        json.dump({"accuracy": accuracy_pct, "dataset": dataset_name}, f)
    
    dataset_msg = f" (dataset {dataset_name})" if dataset_name == "personalizado" else ""
    
    return {
        "model": "adaboost",
        "accuracy": accuracy_pct,
        "message": f"Modelo AdaBoost entrenado y guardado correctamente{dataset_msg}"
    }


def predict(features: dict):
    """
    Realiza una predicción con el modelo entrenado
    Args:
        features: Diccionario con los 30 parámetros de entrada
    Returns:
        dict: Predicción (Maligno/Benigno) y probabilidades
    """
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("El modelo no ha sido entrenado. Ejecute /train/adaboost primero.")
    
    model = joblib.load(MODEL_PATH)
    feature_names = joblib.load(FEATURE_NAMES_PATH)
    
    # Crear DataFrame con el orden correcto de columnas
    X = pd.DataFrame([features], columns=feature_names)
    
    # Predecir
    prediction = model.predict(X)[0]
    probabilities = model.predict_proba(X)[0]
    
    # 0 = Maligno, 1 = Benigno
    result = "Benigno" if prediction == 1 else "Maligno"
    
    return {
        "prediction": result,
        "probability_malignant": round(probabilities[0] * 100, 2),
        "probability_benign": round(probabilities[1] * 100, 2)
    }


def is_trained():
    """Verifica si el modelo está entrenado"""
    return os.path.exists(MODEL_PATH)


def get_accuracy():
    """Devuelve el accuracy del modelo entrenado"""
    if os.path.exists(ACCURACY_PATH):
        with open(ACCURACY_PATH, 'r') as f:
            data = json.load(f)
            return data.get("accuracy", None)
    return None
