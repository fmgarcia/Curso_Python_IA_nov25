# Ejemplo lambda con filter
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6, 8, 10]

cadenas = ["casa", "coche", "moto", "avión", "barco"]
cadenas_con_o = list(filter(lambda s: 'o' in s, cadenas)) # ['coche', 'moto', 'avión', 'barco']
cadenas_empiezan_con_c_y_mas_de_4_letras = list(filter(lambda s: s.startswith("c") and len(s) > 4, cadenas)) # ['coche']

# ejemplo filte con listas por comprensión (pitónico)
pares2 = [x for x in numeros if x % 2 == 0] # [2, 4, 6, 8, 10]
cadenas_con_o2 = [s for s in cadenas if 'o' in s] # ['coche', 'moto', 'avión', 'barco']
cadenas_empiezan_con_c_y_mas_de_4_letras2 = [s for s in cadenas if s.startswith("c") and len(s) > 4] # ['coche']

# Ejemplo lambda con map. Aplicar una función a todos los elementos de una lista para obtener una nueva lista donde cada elemento es el resultado de aplicar la función al elemento original
cuadrados = list(map(lambda x: x ** 2, numeros)) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
cadenas = ["casa", "coche", "moto", "avión", "barco"]
longitudes = list(map(lambda s: len(s), cadenas)) # [4, 5, 4, 5, 5]

# ejemplo map con listas por comprensión
cuadrados2 = [x ** 2 for x in numeros]
longitudes2 = [len(s) for s in cadenas]

# Combinando filter y map
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares_cuadrados = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numeros))) # [4, 16, 36, 64, 100]
cadenas = ["casa", "coche", "moto", "avión", "barco"]
numeros_letras_cadenas_con_mas_de_4_letras = list(filter(lambda e: e>4, map(lambda s: len(s), cadenas))) # [5, 5, 5]

# combinando filter y map con listas por comprensión
pares_cuadrados2 = [x ** 2 for x in numeros if x % 2 == 0] # [4, 16, 36, 64, 100]
numeros_letras_cadenas_con_mas_de_4_letras2 = [len(s) for s in cadenas if len(s) > 4] # [5, 5, 5]

# Función que dada una palabra devuelve la misma palabra sustituyendo cada letra por la siguiente en el alfabeto
def siguiente_letra(palabra):
    return ''.join(map(lambda c: chr(ord(c) + 1) if c.isalpha() else c, palabra))
cadenas = ["casa", "coche", "moto", "avión", "barco"]
resultado = list(map(siguiente_letra, cadenas))
print(resultado)  # ['dbtb', 'dpdif', 'npup', 'bwjón', 'cbsdp']
resultado2 = list(map(lambda palabra: ''.join(map(lambda c: chr(ord(c) + 1) if c.isalpha() else c, palabra)), cadenas))
print(resultado2)  # ['dbtb', 'dpdif', 'npup', 'bwjón', 'cbsdp']
resultado3 = [siguiente_letra(palabra) for palabra in cadenas]
print(resultado3)  # ['dbtb', 'dpdif', 'npup', 'bwjón', 'cbsdp']
resultado4 = [''.join(map(lambda c: chr(ord(c) + 1) if c.isalpha() else c, palabra)) for palabra in cadenas]
print(resultado4)  # ['dbtb', 'dpdif', 'npup', 'bwjón', 'cbsdp']


# ejemplo lambda con reduce
from functools import reduce
suma_total = reduce(lambda x, y: x + y, numeros)
print(suma_total)  # 55

# usando una operación built-in
suma_total2 = sum(numeros)
print(suma_total2)  # 55

concatena = reduce(lambda total, x: total + str(x), numeros, "la cadena concatenada es: ")
print(concatena) # 12345678910