'''
Pide al usuario 5 números e introdúcelos en una lista. Después muestra:
–Lista de los números
–Suma de los números
–Media de los números
–Mínimo y máximo
'''

def sumar():
    numeros = []  # Lista para almacenar los números
    for i in range(5): # Pedir 5 números al usuario
        numero = float(input(f"Introduce el número {i + 1}: ")) # Convertir la entrada a float
        numeros.append(numero) # Añadir el número a la lista por el final

    # Operaciones con la lista de números
    suma_numeros = sum(numeros)
    media_numeros = suma_numeros / len(numeros)
    minimo_numeros = min(numeros)
    maximo_numeros = max(numeros)

    # Mostrar resultados
    print(f"Lista de números: {numeros}")
    print(f"Suma de los números: {suma_numeros}")
    print(f"Media de los números: {media_numeros}")
    print(f"Mínimo: {minimo_numeros}, Máximo: {maximo_numeros}")


if __name__ == "__main__":
    sumar()
