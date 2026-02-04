# 🔌 API Reference

## Base URL
```
http://localhost:8000
```

## Documentación Interactiva
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

---

## Endpoints

### 📍 GET /
**Información de la API**

```http
GET / HTTP/1.1
Host: localhost:8000
```

**Response 200:**
```json
{
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
```

---

### 📍 GET /models
**Lista de modelos disponibles y su estado**

```http
GET /models HTTP/1.1
Host: localhost:8000
```

**Response 200:**
```json
[
    {
        "name": "random_forest",
        "display_name": "Random Forest",
        "trained": true,
        "accuracy": 95.61
    },
    {
        "name": "xgboost",
        "display_name": "XGBoost",
        "trained": false,
        "accuracy": null
    }
]
```

---

### 📍 POST /train/{model_name}
**Entrenar un modelo**

**Parámetros:**
| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| model_name | path | Nombre del modelo |

**Valores válidos para model_name:**
- `random_forest`
- `xgboost`
- `adaboost`
- `gradient_boosting`
- `voting`

```http
POST /train/random_forest HTTP/1.1
Host: localhost:8000
```

**Response 200:**
```json
{
    "model": "random_forest",
    "accuracy": 95.61,
    "message": "Modelo Random Forest entrenado y guardado correctamente"
}
```

**Response 404:**
```json
{
    "detail": "Modelo 'invalid_model' no encontrado. Modelos disponibles: ['random_forest', 'xgboost', 'adaboost', 'gradient_boosting', 'voting']"
}
```

---

### 📍 POST /predict
**Realizar predicción**

```http
POST /predict HTTP/1.1
Host: localhost:8000
Content-Type: application/json

{
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
```

**Response 200:**
```json
{
    "prediction": "Maligno",
    "probability_malignant": 99.5,
    "probability_benign": 0.5
}
```

**Response 400:**
```json
{
    "detail": "El modelo 'random_forest' no ha sido entrenado."
}
```

---

### 📍 GET /features
**Lista de características requeridas**

```http
GET /features HTTP/1.1
Host: localhost:8000
```

**Response 200:**
```json
{
    "total_features": 30,
    "feature_names": ["mean radius", "mean texture", ...],
    "categories": {
        "mean": ["mean radius", "mean texture", ...],
        "error": ["radius error", "texture error", ...],
        "worst": ["worst radius", "worst texture", ...]
    }
}
```

---

### 📍 GET /sample-data
**Datos de ejemplo para pruebas**

```http
GET /sample-data HTTP/1.1
Host: localhost:8000
```

**Response 200:**
```json
{
    "malignant_example": {
        "mean radius": 17.99,
        "mean texture": 10.38,
        ...
    },
    "benign_example": {
        "mean radius": 12.34,
        "mean texture": 14.56,
        ...
    }
}
```

---

### 📍 GET /random-sample
**Genera datos aleatorios realistas**

```http
GET /random-sample HTTP/1.1
Host: localhost:8000
```

**Response 200:**
```json
{
    "random_sample": {
        "mean radius": 14.25,
        "mean texture": 18.72,
        ...
    }
}
```

---

## Ejemplos con cURL

### Entrenar modelo
```bash
curl -X POST "http://localhost:8000/train/random_forest"
```

### Realizar predicción
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"model_name": "random_forest", "features": {...}}'
```

---

## Ejemplos con PowerShell

### Entrenar modelo
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/train/random_forest" -Method Post
```

### Obtener modelos
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/models" -Method Get
```

---

## Códigos de Estado

| Código | Descripción |
|--------|-------------|
| 200 | Operación exitosa |
| 400 | Error de validación o modelo no entrenado |
| 404 | Recurso no encontrado |
| 500 | Error interno del servidor |

---

*[← Volver al Índice](./index.md)*
