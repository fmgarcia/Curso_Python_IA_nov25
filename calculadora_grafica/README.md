# 🧮 Calculadora Gráfica

Aplicación web que permite al usuario ingresar funciones matemáticas y visualizar sus gráficas en tiempo real.

## 📁 Estructura del Proyecto

```
calculadora_grafica/
├── backend/
│   ├── app.py              # Servidor Flask principal
│   └── requirements.txt    # Dependencias Python
└── frontend/
    ├── index.html          # Estructura de la interfaz
    ├── style.css           # Estilos (diseño responsivo)
    └── script.js           # Lógica del frontend y comunicación API
```

## 🚀 Instalación y Ejecución

### 1. Instalar dependencias

```bash
cd calculadora_grafica/backend
pip install -r requirements.txt
```

### 2. Ejecutar el servidor

```bash
python app.py
```

### 3. Abrir en el navegador

Visita: **http://localhost:5000**

## 📊 Diagrama de Flujo

```
┌─────────────────────────────────────────────────────────────────────┐
│                    COMUNICACIÓN FRONTEND - BACKEND                  │
└─────────────────────────────────────────────────────────────────────┘

    ┌─────────────────┐
    │  Usuario ingresa │
    │  función: sin(x) │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │ Click en botón  │
    │   "Graficar"    │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │   JavaScript    │
    │ handleGraphBtn  │
    │ Click()         │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐         POST /api/graficar
    │   Fetch API     │─────────────────────────────────┐
    │  (Async Request)│     {"funcion": "sin(x)",       │
    └─────────────────┘      "x_min": -10,              │
                             "x_max": 10}               │
                                                        ▼
                                               ┌─────────────────┐
                                               │   Flask Server  │
                                               │   /api/graficar │
                                               └────────┬────────┘
                                                        │
                                                        ▼
                                               ┌─────────────────┐
                                               │  SymPy Parser   │
                                               │ (Parsing seguro │
                                               │  sin eval())    │
                                               └────────┬────────┘
                                                        │
                                                        ▼
                                               ┌─────────────────┐
                                               │     NumPy       │
                                               │ np.linspace()   │
                                               │ lambdify()      │
                                               └────────┬────────┘
                                                        │
    ┌─────────────────┐         JSON Response           │
    │   JavaScript    │◄────────────────────────────────┘
    │ Recibe respuesta│    {"success": true,
    └────────┬────────┘     "x_coords": [...],
             │              "y_coords": [...]}
             ▼
    ┌─────────────────┐
    │   Plotly.js     │
    │  renderGraph()  │
    └────────┬────────┘
             │
             ▼
    ┌─────────────────┐
    │  📈 Gráfico     │
    │  interactivo    │
    │  renderizado    │
    └─────────────────┘
```

## 🔧 API Endpoint

### POST `/api/graficar`

**Request:**
```json
{
    "funcion": "sin(x) + x^2",
    "x_min": -10,
    "x_max": 10,
    "num_puntos": 200
}
```

**Response (éxito):**
```json
{
    "success": true,
    "x_coords": [-10, -9.9, ..., 10],
    "y_coords": [99.544, 97.46, ..., 99.544],
    "funcion_parseada": "x**2 + sin(x)"
}
```

**Response (error):**
```json
{
    "success": false,
    "error": "Error al parsear la función: ..."
}
```

## 📐 Funciones Matemáticas Soportadas

| Función | Ejemplo |
|---------|---------|
| Seno | `sin(x)` |
| Coseno | `cos(x)` |
| Tangente | `tan(x)` |
| Exponencial | `exp(x)` o `e^x` |
| Logaritmo natural | `log(x)` |
| Raíz cuadrada | `sqrt(x)` |
| Valor absoluto | `abs(x)` |
| Potencias | `x^2`, `x**3` |
| Constantes | `pi`, `e` |

## 🛡️ Seguridad

El backend utiliza **SymPy** para parsear las expresiones matemáticas de forma segura, evitando el uso de `eval()` y previniendo inyección de código malicioso.

## 🛠️ Tecnologías

- **Backend:** Python, Flask, NumPy, SymPy, Flask-CORS
- **Frontend:** HTML5, CSS3, JavaScript (ES6+), Plotly.js

---
Desarrollado para EOI 2025
