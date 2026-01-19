suma = lambda n1, n2: n1 + n2

def suma2(n1, n2): 
    return n1 + n2

print(type(suma)) # <class 'function'>
resultado = suma(3, 5)
print(resultado) # 8

# Ejemplo lambda con filter
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6, 8, 10]

# ejemplo filte con listas por comprensión
pares2 = [x for x in numeros if x % 2 == 0]
print(pares2)  # [2, 4, 6, 8, 10]

# Ejemplo lambda con map
cuadrados = list(map(lambda x: x ** 2, numeros))
print(cuadrados)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# ejemplo map con listas por comprensión
cuadrados2 = [x ** 2 for x in numeros]

# ejemplo lambda con reduce
from functools import reduce
suma_total = reduce(lambda x, y: x + y, numeros)
print(suma_total)  # 55

# usando una operación built-in
suma_total2 = sum(numeros)
print(suma_total2)  # 55

concatena = reduce(lambda total, x: total + str(x), numeros, "la cadena concatenada es: ")
print(concatena) # 12345678910