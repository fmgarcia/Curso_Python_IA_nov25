# 🤖 Modelos de Machine Learning

## Visión General

El sistema implementa 5 modelos de clasificación, todos basados en el dataset Wisconsin Breast Cancer con 30 características.

---

## 📊 Dataset

### Wisconsin Breast Cancer Dataset
- **Fuente:** UCI Machine Learning Repository
- **Muestras:** 569
- **Características:** 30 (numéricas)
- **Clases:** 2 (Maligno=0, Benigno=1)
- **Distribución:** 357 benignos, 212 malignos

### Características
Las 30 características se calculan a partir de imágenes digitalizadas de aspiración con aguja fina (FNA) de masas mamarias:

| Categoría | Características |
|-----------|-----------------|
| **Mean** | Radio, textura, perímetro, área, suavidad, compacidad, concavidad, puntos cóncavos, simetría, dimensión fractal |
| **Error** | Error estándar de las 10 características anteriores |
| **Worst** | Peor valor (mayor) de las 10 características base |

---

## 🌲 Random Forest

### Descripción
Ensemble de múltiples árboles de decisión que votan para la predicción final.

### Hiperparámetros
```python
RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    random_state=42
)
```

### Ventajas
- ✅ Robusto al overfitting
- ✅ Maneja bien datos no lineales
- ✅ No requiere normalización
- ✅ Proporciona importancia de características

### Accuracy Típico
~95-97%

---

## ⚡ XGBoost

### Descripción
Implementación optimizada de Gradient Boosting con regularización.

### Hiperparámetros
```python
XGBClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=10,
    eval_metric='logloss',
    random_state=42
)
```

### Ventajas
- ✅ Alto rendimiento
- ✅ Regularización incorporada
- ✅ Manejo de valores faltantes
- ✅ Velocidad de entrenamiento

### Accuracy Típico
~95-98%

---

## 🔄 AdaBoost

### Descripción
Boosting adaptativo que ajusta pesos de muestras mal clasificadas.

### Hiperparámetros
```python
AdaBoostClassifier(
    estimator=DecisionTreeClassifier(max_depth=10),
    n_estimators=100,
    random_state=42
)
```

### Ventajas
- ✅ Simple de implementar
- ✅ Menos propenso al overfitting
- ✅ Buena interpretabilidad
- ✅ Funciona bien con estimadores débiles

### Accuracy Típico
~94-96%

---

## 📈 Gradient Boosting

### Descripción
Construye modelos secuencialmente minimizando errores residuales.

### Hiperparámetros
```python
GradientBoostingClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=10,
    random_state=42
)
```

### Ventajas
- ✅ Alta precisión
- ✅ Flexible en función de pérdida
- ✅ Bueno para datos tabulares
- ✅ Maneja interacciones complejas

### Accuracy Típico
~95-97%

---

## 🗳️ Voting Classifier

### Descripción
Combina predicciones de múltiples modelos mediante votación suave.

### Composición
```python
VotingClassifier(
    estimators=[
        ('dt', DecisionTreeClassifier(max_depth=10)),
        ('lr', LogisticRegression(max_iter=10000)),
        ('knn', KNeighborsClassifier(n_neighbors=5))
    ],
    voting='soft'
)
```

### Modelos Base
1. **Decision Tree:** Ábol de decisión simple
2. **Logistic Regression:** Clasificador lineal probabilístico
3. **KNN:** K-vecinos más cercanos

### Ventajas
- ✅ Reduce varianza
- ✅ Más robusto que modelos individuales
- ✅ Aprovecha fortalezas de cada modelo
- ✅ Votación suave para probabilidades

### Accuracy Típico
~94-96%

---

## 📊 Comparativa de Modelos

| Modelo | Accuracy | Velocidad | Interpretabilidad |
|--------|----------|-----------|-------------------|
| Random Forest | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| XGBoost | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ |
| AdaBoost | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| Gradient Boosting | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| Voting | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |

---

## 🔧 Proceso de Entrenamiento

```
1. Cargar dataset (sklearn.datasets.load_breast_cancer)
        ↓
2. Dividir datos (80% train, 20% test, stratified)
        ↓
3. Entrenar modelo con hiperparámetros definidos
        ↓
4. Evaluar en conjunto de test (accuracy)
        ↓
5. Guardar modelo (joblib) y accuracy (JSON)
```

---

## 📁 Almacenamiento

### Pesos de Modelos
```
backend/weights/
├── random_forest.joblib
├── xgboost.joblib
├── adaboost.joblib
├── gradient_boosting.joblib
├── voting.joblib
└── feature_names.joblib
```

### Métricas
```
backend/weights/
├── random_forest_accuracy.json
├── xgboost_accuracy.json
├── adaboost_accuracy.json
├── gradient_boosting_accuracy.json
└── voting_accuracy.json
```

---

## 🎯 Recomendaciones de Uso

| Caso de Uso | Modelo Recomendado |
|-------------|-------------------|
| Mayor precisión | XGBoost |
| Equilibrio precision/velocidad | Random Forest |
| Interpretabilidad | Voting Classifier |
| Recursos limitados | AdaBoost |
| Datasets grandes | XGBoost |

---

*[← Volver al Índice](./index.md)*
