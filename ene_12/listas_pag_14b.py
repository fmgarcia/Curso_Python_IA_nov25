'''
Pide al usuario 5 números e introdúcelos en una lista. Después muestra:
–Lista de los números
–Suma de los números
–Media de los números
–Mínimo y máximo
'''

def sumar():
    numeros = []  # Lista para almacenar los números
    print("Introduce 5 números separados por espacios (ej: 1 2 3 4 5):")
    #numeros = list(map(float, input().split()))
    n1,n2,n3,n4,n5 = map(float, input().split())
    numeros = [n1, n2, n3, n4, n5]
    
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
