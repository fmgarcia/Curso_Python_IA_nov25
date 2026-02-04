# 🚀 Manual de Uso

## Acceso a la Aplicación

### URL de Acceso
- **Frontend:** http://localhost:3000
- **API Docs:** http://localhost:8000/docs

---

## 🔐 Inicio de Sesión

### Credenciales por Defecto
```
Usuario: admin
Contraseña: admin
```

### Pasos
1. Abrir `http://localhost:3000`
2. Ingresar usuario: `admin`
3. Ingresar contraseña: `admin`
4. Clic en "Iniciar Sesión"

> **Nota:** Las credenciales se muestran en la pantalla de login como recordatorio.

---

## 🎛️ Panel de Control

### Selección de Modelo
Elegir uno de los 5 modelos disponibles:

| Modelo | Descripción |
|--------|-------------|
| Random Forest | Ensemble de árboles de decisión |
| XGBoost | Gradient boosting optimizado |
| AdaBoost | Boosting adaptativo |
| Gradient Boosting | Boosting por gradiente |
| Voting Classifier | Combinación de modelos |

### Entrenamiento
1. Seleccionar modelo del dropdown
2. Clic en "🎯 Entrenar [Modelo]"
3. Esperar a que termine (muestra spinner)
4. Ver mensaje de éxito con accuracy

### Estado de Modelos
- ✓ **Verde**: Modelo entrenado (muestra % accuracy)
- ○ **Gris**: Sin entrenar

---

## 📋 Introducción de Datos

### Datos de Ejemplo
Usar los botones rápidos para cargar datos de prueba:

| Botón | Descripción |
|-------|-------------|
| 🟢 Caso Benigno | Carga datos de un caso benigno real |
| 🔴 Caso Maligno | Carga datos de un caso maligno real |
| 🎲 Datos Aleatorios | Genera datos aleatorios realistas |

### Entrada Manual
Completar los 30 campos organizados en 3 secciones:

#### 📊 Valores Medios (Mean)
- Radio medio, Textura media, Perímetro medio
- Área media, Suavidad media, Compacidad media
- Concavidad media, Puntos cóncavos medios
- Simetría media, Dimensión fractal media

#### 📈 Errores Estándar (Error)
- Error de radio, Error de textura, Error de perímetro
- Error de área, Error de suavidad, Error de compacidad
- Error de concavidad, Error de puntos cóncavos
- Error de simetría, Error de dimensión fractal

#### ⚠️ Valores Peores (Worst)
- Peor radio, Peor textura, Peor perímetro
- Peor área, Peor suavidad, Peor compacidad
- Peor concavidad, Peor puntos cóncavos
- Peor simetría, Peor dimensión fractal

---

## 🔬 Realizar Predicción

### Pasos
1. Asegurar que hay un modelo entrenado
2. Cargar o introducir datos
3. Clic en "🔬 Realizar Predicción"
4. Ver resultado

### Interpretación del Resultado

#### Resultado Benigno 🟢
```
Diagnóstico: BENIGNO
Probabilidad Benigno: XX%
Probabilidad Maligno: XX%
```
El tumor tiene características compatibles con tejido benigno.

#### Resultado Maligno 🔴
```
Diagnóstico: MALIGNO
Probabilidad Maligno: XX%
Probabilidad Benigno: XX%
```
El tumor presenta características que sugieren malignidad.

> **⚠️ Importante:** Este sistema es una herramienta de apoyo. El diagnóstico final debe ser realizado por un profesional médico.

---

## 🎨 Modo Oscuro/Claro

### Cambiar Tema
- Clic en el icono 🌙/☀️ en la esquina superior derecha
- El tema se guarda en el navegador

---

## 🗑️ Limpiar Formulario

Clic en "🗑️ Limpiar" para:
- Vaciar todos los campos
- Limpiar resultado de predicción
- Mantener el modelo seleccionado

---

## 🔄 Flujo de Trabajo Típico

```
1. Login (admin/admin)
        ↓
2. Seleccionar modelo
        ↓
3. Entrenar modelo (si no está entrenado)
        ↓
4. Cargar datos de ejemplo o introducir manualmente
        ↓
5. Realizar predicción
        ↓
6. Interpretar resultado
```

---

## ⌨️ Atajos de Teclado

| Atajo | Acción |
|-------|--------|
| Enter | Enviar formulario (realizar predicción) |
| Tab | Navegar entre campos |

---

## 📱 Uso en Móvil

La aplicación es responsive y funciona en:
- 📱 Smartphones (portrait y landscape)
- 📱 Tablets
- 💻 Escritorio

---

*[← Volver al Índice](./index.md)*
