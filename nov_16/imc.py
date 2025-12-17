# programa que calcula el imc (índice de masa corporal)
peso = input("Introduce tu peso en kg: ")
altura = input("Introduce tu altura en centímetros: ")
if peso.isdigit() and altura.isdigit():
    peso = float(peso)
    altura = float(altura) / 100  # Convertir centímetros a metros
    imc = peso / (altura ** 2)
    print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")
else:
    print("Error: Debes introducir números válidos para peso y altura.")