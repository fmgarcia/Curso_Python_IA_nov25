"""
Servidor Flask para la Calculadora Gráfica.
Proporciona un endpoint seguro para evaluar funciones matemáticas.
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import numpy as np
from sympy import symbols, sympify, lambdify, sin, cos, tan, exp, log, sqrt, pi, E
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
import os

app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

# Símbolo x para las expresiones matemáticas
x = symbols('x')

# Funciones matemáticas permitidas (whitelist de seguridad)
FUNCIONES_PERMITIDAS = {
    'sin': sin,
    'cos': cos,
    'tan': tan,
    'exp': exp,
    'log': log,
    'sqrt': sqrt,
    'abs': abs,
    'pi': pi,
    'e': E,
}

# Transformaciones para el parser
TRANSFORMACIONES = standard_transformations + (implicit_multiplication_application,)


def parsear_funcion_segura(funcion_str: str):
    """
    Parsea una función matemática de forma segura usando SymPy.
    Evita la inyección de código malicioso al usar un whitelist de funciones.
    """
    try:
        # Reemplazar notación común
        funcion_str = funcion_str.replace('^', '**')
        funcion_str = funcion_str.replace('sen', 'sin')  # Español a inglés
        
        # Parsear la expresión con SymPy (seguro)
        expr = parse_expr(
            funcion_str,
            local_dict={'x': x, **FUNCIONES_PERMITIDAS},
            transformations=TRANSFORMACIONES,
            evaluate=True
        )
        return expr, None
    except Exception as e:
        return None, str(e)


def calcular_puntos(expr, x_min: float = -10, x_max: float = 10, num_puntos: int = 200):
    """
    Calcula los puntos (x, y) para graficar la función.
    Usa NumPy para cálculos vectorizados eficientes.
    """
    try:
        # Crear función numérica a partir de la expresión simbólica
        func_numerica = lambdify(x, expr, modules=['numpy'])
        
        # Generar valores de x
        x_vals = np.linspace(x_min, x_max, num_puntos)
        
        # Calcular valores de y
        y_vals = func_numerica(x_vals)
        
        # Convertir a lista y manejar valores infinitos/NaN
        x_lista = x_vals.tolist()
        y_lista = []
        
        for y in y_vals:
            if np.isnan(y) or np.isinf(y):
                y_lista.append(None)  # JSON puede manejar null
            else:
                y_lista.append(float(y))
        
        return x_lista, y_lista, None
    except Exception as e:
        return None, None, str(e)


@app.route('/')
def index():
    """Sirve la página principal del frontend."""
    if app.static_folder is None:
        return "Error: static folder not configured", 500
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/<path:path>')
def static_files(path):
    """Sirve archivos estáticos del frontend."""
    if app.static_folder is None:
        return "Error: static folder not configured", 500
    return send_from_directory(app.static_folder, path)


@app.route('/api/graficar', methods=['POST'])
def graficar():
    """
    Endpoint API para calcular los puntos de una función.
    
    Request JSON:
        {
            "funcion": "sin(x) + x**2",
            "x_min": -10,      (opcional)
            "x_max": 10,       (opcional)
            "num_puntos": 200  (opcional)
        }
    
    Response JSON:
        {
            "success": true,
            "x_coords": [...],
            "y_coords": [...],
            "funcion_parseada": "sin(x) + x**2"
        }
    """
    try:
        data = request.get_json()
        
        if not data or 'funcion' not in data:
            return jsonify({
                'success': False,
                'error': 'Se requiere el campo "funcion" en el JSON.'
            }), 400
        
        funcion_str = data['funcion'].strip()
        
        if not funcion_str:
            return jsonify({
                'success': False,
                'error': 'La función no puede estar vacía.'
            }), 400
        
        # Parámetros opcionales con valores por defecto
        x_min = data.get('x_min', -100)
        x_max = data.get('x_max', 100)
        num_puntos = data.get('num_puntos', 200)
        
        # Validar parámetros
        try:
            x_min = float(x_min)
            x_max = float(x_max)
            num_puntos = int(num_puntos)
        except ValueError:
            return jsonify({
                'success': False,
                'error': 'Los parámetros x_min, x_max deben ser números y num_puntos entero.'
            }), 400
        
        if x_min >= x_max:
            return jsonify({
                'success': False,
                'error': 'x_min debe ser menor que x_max.'
            }), 400
        
        if num_puntos < 10 or num_puntos > 1000:
            return jsonify({
                'success': False,
                'error': 'num_puntos debe estar entre 10 y 1000.'
            }), 400
        
        # Parsear la función de forma segura
        expr, error = parsear_funcion_segura(funcion_str)
        
        if error:
            return jsonify({
                'success': False,
                'error': f'Error al parsear la función: {error}'
            }), 400
        
        # Calcular los puntos
        x_coords, y_coords, error = calcular_puntos(expr, x_min, x_max, num_puntos)
        
        if error:
            return jsonify({
                'success': False,
                'error': f'Error al calcular los puntos: {error}'
            }), 400
        
        return jsonify({
            'success': True,
            'x_coords': x_coords,
            'y_coords': y_coords,
            'funcion_parseada': str(expr)
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Error interno del servidor: {str(e)}'
        }), 500


if __name__ == '__main__':
    print("=" * 50)
    print("🧮 Calculadora Gráfica - Backend Flask")
    print("=" * 50)
    print("Servidor corriendo en: http://localhost:5000")
    print("Abre esta URL en tu navegador para usar la calculadora.")
    print("Presiona Ctrl+C para detener el servidor.")
    print("=" * 50)
    app.run(debug=True, port=5000)
