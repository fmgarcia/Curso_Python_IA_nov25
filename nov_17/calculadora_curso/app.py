from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# --- Variables Globales de Configuración (Lógica de Negocio) ---
PRECIO_BASE = 800.0
UMBRAL_SALARIO = 25000.0
UMBRAL_HIJOS = 2
DESCUENTO_PORCENTAJE = 0.15
DESCUENTO_FAMILIA_NUMEROSA = 100.0

@app.route('/')
def index():
    """Sirve el archivo frontend."""
    return send_file('index.html')

@app.route('/api/config', methods=['GET'])
def get_config():
    """
    Devuelve la configuración necesaria para que el frontend 
    sepa cuándo activar los campos (evitando hardcode en JS).
    """
    return jsonify({
        "umbral_salario": UMBRAL_SALARIO
    })

@app.route('/api/calcular', methods=['POST'])
def calcular_precio():
    """
    Calcula el precio final basado en el salario y número de hijos.
    """
    try:
        data = request.get_json()
        salario = float(data.get('salario', 0))
        # El número de hijos es opcional si el salario es alto, pero lo leemos si viene
        hijos = int(data.get('hijos', 0))
        
        precio_final = PRECIO_BASE
        desglose = [f"Precio base: {PRECIO_BASE}€"]

        # Lógica del programa original
        if salario < UMBRAL_SALARIO:
            descuento_pct = precio_final * DESCUENTO_PORCENTAJE
            precio_final -= descuento_pct
            desglose.append(f"Descuento por salario (< {UMBRAL_SALARIO}€): -{descuento_pct:.2f}€ (15%)")
            
            if hijos > UMBRAL_HIJOS:
                precio_final -= DESCUENTO_FAMILIA_NUMEROSA
                desglose.append(f"Descuento familia numerosa (> {UMBRAL_HIJOS} hijos): -{DESCUENTO_FAMILIA_NUMEROSA}€")
        
        return jsonify({
            "precio_final": precio_final,
            "desglose": desglose
        })

    except ValueError:
        return jsonify({"error": "Datos inválidos"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print(f"Iniciando servidor en http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
