# 🏗️ Arquitectura del Sistema

## Visión General

El Sistema de Detección de Tumores es una aplicación web full-stack que utiliza Machine Learning para clasificar tumores mamarios como benignos o malignos.

---

## 📁 Estructura del Proyecto

```
Proyecto_completo/
├── backend/                    # Servidor FastAPI
│   ├── main.py                # Punto de entrada de la API
│   ├── requirements.txt       # Dependencias Python
│   ├── pyrightconfig.json     # Configuración de tipo
│   ├── models/                # Módulos de ML
│   │   ├── __init__.py
│   │   ├── random_forest.py
│   │   ├── xgboost_model.py
│   │   ├── adaboost.py
│   │   ├── gradient_boosting.py
│   │   └── voting_model.py
│   ├── weights/               # Pesos de modelos entrenados
│   │   ├── *.joblib           # Modelos serializados
│   │   └── *_accuracy.json    # Métricas de accuracy
│   └── venv/                  # Entorno virtual Python
│
├── frontend/                  # Aplicación React
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── App.js            # Componente principal
│   │   ├── index.js          # Punto de entrada
│   │   ├── index.css         # Estilos globales
│   │   ├── context/
│   │   │   └── AppContext.js # Estado global
│   │   └── components/
│   │       ├── Login.js
│   │       ├── ModelSelector.js
│   │       ├── PredictionForm.js
│   │       └── PredictionResult.js
│   └── package.json
│
├── docs/                      # Documentación
│   ├── index.md
│   ├── arquitectura.md
│   ├── instalacion.md
│   ├── uso.md
│   ├── api.md
│   ├── modelos.md
│   └── testing.md
│
└── tests/                     # Pruebas
    ├── backend/
    └── frontend/
```

---

## 🔧 Stack Tecnológico

### Backend
| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| Python | 3.11+ | Lenguaje principal |
| FastAPI | 0.109.0 | Framework web |
| Uvicorn | 0.27.0 | Servidor ASGI |
| Scikit-learn | 1.4.0 | Modelos ML |
| XGBoost | 2.0.3 | Modelo XGBoost |
| Pandas | 2.2.0 | Manipulación de datos |
| NumPy | 1.26.3 | Computación numérica |
| Joblib | 1.3.2 | Serialización |

### Frontend
| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| React | 18.2.0 | Framework UI |
| Axios | Latest | Cliente HTTP |
| Context API | - | Estado global |
| CSS3 | - | Estilos |

---

## 🔄 Flujo de Datos

```
┌──────────────┐     HTTP/JSON    ┌──────────────┐
│   Frontend   │ ◄──────────────► │   Backend    │
│    React     │                  │   FastAPI    │
└──────┬───────┘                  └──────┬───────┘
       │                                 │
       │                                 │
       ▼                                 ▼
┌──────────────┐                  ┌──────────────┐
│  AppContext  │                  │  Modelos ML  │
│    State     │                  │   sklearn    │
└──────────────┘                  └──────────────┘
```

### Flujo de Entrenamiento
1. Usuario selecciona modelo en Frontend
2. Frontend envía POST a `/train/{model_name}`
3. Backend carga dataset Wisconsin Breast Cancer
4. Entrena el modelo seleccionado
5. Guarda pesos en `/weights/`
6. Retorna accuracy al Frontend

### Flujo de Predicción
1. Usuario ingresa 30 características
2. Frontend envía POST a `/predict`
3. Backend carga modelo entrenado
4. Realiza predicción
5. Retorna resultado (Benigno/Maligno) con probabilidades

---

## 🏛️ Patrones de Arquitectura

### Backend
- **RESTful API**: Endpoints claros y predecibles
- **Modular Design**: Cada modelo en su propio módulo
- **Dependency Injection**: Modelos cargados dinámicamente

### Frontend
- **Component-Based**: UI dividida en componentes reutilizables
- **Context Pattern**: Estado global con React Context
- **Responsive Design**: Adaptable a diferentes pantallas

---

## 🔐 Seguridad

- **CORS**: Configurado para localhost:3000
- **Autenticación**: Login básico (admin/admin)
- **Validación**: Pydantic para validar requests

---

## 📊 Dataset

**Wisconsin Breast Cancer Dataset**
- 569 muestras
- 30 características numéricas
- 2 clases: Maligno (0) y Benigno (1)
- Fuente: UCI Machine Learning Repository

---

*[← Volver al Índice](./index.md)*
