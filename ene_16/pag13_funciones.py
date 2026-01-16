'''
●Crea una función que reciba 2 números enteros por parámetro (un mínimo y un máximo). 
La función mostrará la lista de números comprendidos entre el mínimo y el máximo. 
El mínimo tendrá un valor por defecto de 0 y el máximo de 20. 
●Llama a la función al menos 4 veces. 
Una sin pasarle nada, otra pasándole ambos números, otra pasándole el mínimo, y otra sólo el máximo 
(usa el envío de parámetros nominales para esto último).
'''

def mostrar(minimo=0, maximo=20):
    for numero in range(minimo, maximo + 1):
        print(numero, end=' ')
    print()  # Salto de línea al final

# Llamadas a la función
mostrar()  # Sin parámetros, usa valores por defecto
mostrar(5, 15)  # Pasando ambos números
mostrar(10)  # Pasando sólo el mínimo
mostrar(maximo=10)  # Pasando sólo el máximo usando parámetro nominal