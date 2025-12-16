import sys
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal.
    IMC = Peso (kg) / Altura (m)²
    """
    return peso / (altura ** 2)

def clasificar_imc(imc):
    """
    Clasificación del IMC según la OMS (Organización Mundial de la Salud).
    """
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Peso normal (Saludable)"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidad Grado I"
    elif 35 <= imc < 40:
        return "Obesidad Grado II"
    else:
        return "Obesidad Grado III (Mórbida)"

def calcular_grasa_corporal_deurenberg(imc, edad, sexo):
    """
    Estima el porcentaje de grasa corporal usando la fórmula de Deurenberg.
    %GC = (1.20 * IMC) + (0.23 * Edad) - (10.8 * Sexo) - 5.4
    Donde Sexo = 1 para hombres, 0 para mujeres.
    """
    valor_sexo = 1 if sexo == 'H' else 0
    grasa = (1.20 * imc) + (0.23 * edad) - (10.8 * valor_sexo) - 5.4
    return grasa

# --- Rutas del Servidor Web ---

@app.route('/')
def index():
    """
    Sirve el archivo frontend único.
    """
    return send_file('frontend_imc.html')

@app.route('/api/calcular', methods=['POST'])
def api_calcular():
    """
    Endpoint API que recibe JSON y devuelve resultados.
    """
    try:
        datos = request.get_json()
        
        if not datos:
            return jsonify({"error": "No se recibieron datos"}), 400
            
        peso = float(datos.get('peso', 0))
        altura = float(datos.get('altura', 0))
        edad = int(datos.get('edad', 0))
        sexo = datos.get('sexo', '').upper()

        # Validaciones
        if peso < 20 or peso > 300:
            return jsonify({"error": "El peso debe estar entre 20 y 300 kg"}), 400
        if altura < 0.5 or altura > 2.5:
            return jsonify({"error": "La altura debe estar entre 0.5 y 2.5 m"}), 400
        if edad < 10 or edad > 120:
            return jsonify({"error": "La edad debe estar entre 10 y 120 años"}), 400
        if sexo not in ['H', 'M']:
            return jsonify({"error": "Sexo inválido. Use 'H' o 'M'"}), 400

        # Cálculos
        imc = calcular_imc(peso, altura)
        clasificacion = clasificar_imc(imc)
        grasa = calcular_grasa_corporal_deurenberg(imc, edad, sexo)

        return jsonify({
            "imc": imc,
            "clasificacion": clasificacion,
            "grasa_corporal": grasa
        })

    except ValueError as e:
        return jsonify({"error": f"Error en los datos: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"Error interno: {str(e)}"}), 500

if __name__ == "__main__":
    print("Iniciando servidor web en http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
