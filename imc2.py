import sys

def obtener_numero(mensaje, tipo=float, min_val=None, max_val=None):
    """
    Solicita un número al usuario de forma robusta.
    Valida el tipo de dato y el rango.
    """
    while True:
        try:
            entrada = input(mensaje)
            valor = tipo(entrada)
            
            if min_val is not None and valor < min_val:
                print(f"Error: El valor debe ser mayor o igual a {min_val}.")
                continue
            if max_val is not None and valor > max_val:
                print(f"Error: El valor debe ser menor o igual a {max_val}.")
                continue
                
            return valor
        except ValueError:
            print(f"Error: Por favor, introduce un número válido ({tipo.__name__}).")

def obtener_sexo():
    """
    Solicita el sexo biológico al usuario.
    Necesario para fórmulas de grasa corporal.
    """
    while True:
        entrada = input("Introduce tu sexo biológico (H para hombre, M para mujer): ").strip().upper()
        if entrada in ['H', 'M']:
            return entrada
        print("Error: Por favor, introduce 'H' o 'M'.")

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

def main():
    print("=== Calculadora Avanzada de IMC y Composición Corporal ===")
    print("Este programa calcula tu IMC y estima tu porcentaje de grasa corporal.")
    print("Nota: Aunque el IMC solo requiere peso y altura, parámetros como la edad y el sexo")
    print("influyen en la interpretación de la composición corporal (fórmula de Deurenberg).\n")

    # Recolección de datos robusta
    peso = obtener_numero("Introduce tu peso en kg (ej. 70.5): ", float, 20.0, 300.0)
    altura = obtener_numero("Introduce tu altura en metros (ej. 1.75): ", float, 0.5, 2.5)
    edad = obtener_numero("Introduce tu edad en años (ej. 30): ", int, 10, 120)
    sexo = obtener_sexo()

    # Cálculos
    imc = calcular_imc(peso, altura)
    clasificacion = clasificar_imc(imc)
    grasa_corporal = calcular_grasa_corporal_deurenberg(imc, edad, sexo)

    # Resultados
    print("\n" + "="*40)
    print("RESULTADOS")
    print("="*40)
    print(f"IMC Calculado: {imc:.2f}")
    print(f"Clasificación OMS: {clasificacion}")
    print("-" * 40)
    print(f"Estimación de Grasa Corporal (Fórmula Deurenberg): {grasa_corporal:.2f}%")
    print("-" * 40)
    
    # Nota sobre pliegues
    print("\nNOTA TÉCNICA SOBRE PLIEGUES:")
    print("Has preguntado por pliegues corporales. El IMC estándar NO utiliza pliegues.")
    print("Los pliegues cutáneos (tricipital, subescapular, etc.) se usan en métodos")
    print("antropométricos directos (como Durnin-Womersley) para medir la densidad corporal.")
    print("La fórmula de Deurenberg utilizada aquí es una alternativa precisa que usa")
    print("tu IMC, edad y sexo para estimar la grasa sin necesidad de un plicómetro.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nPrograma interrumpido por el usuario.")
        sys.exit(0)
