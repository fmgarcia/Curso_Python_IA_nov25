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

import functools, operator
numeros = [1, 2, 3, 4, 5]
producto = functools.reduce(operator.mul, numeros, 1)
suma = functools.reduce(operator.add, numeros, 0)
suma2 = sum(numeros)


# Combinación de map, filter y reduce
# primero filtramos los números pares, luego los elevamos al cuadrado y finalmente sumamos todos los cuadrados
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = reduce(lambda x, y: x + y,
                     map(lambda x: x ** 2,
                          filter(lambda x: x % 2 == 0, numeros))) # 220

# Dada una lista de cadenas, obtener la concatenación de las cadenas que tienen más de 4 letras, usando map, filter y reduce
# convirtiendo cada palabra en su palabra encriptada (siguiente letra) y luego concatenándolas
cadenas = ["casa", "coche", "moto", "avión", "barco"]
resultado = reduce(lambda x, y: x + y,
                     map(lambda palabra: siguiente_letra(palabra),
                         filter(lambda s: len(s) > 4, cadenas))) # dpdifbwjóncbsdp

import itertools as it
''' Ejemplos de uso del módulo itertools
for e in it.permutations([1, 2, 3, 4, 5], 3):
    print(e)
'''
for e in it.permutations("abcde", 3):
    print(e)
    
# dropwhile borra los primeros elementos de un iterable mientras se cumpla una condición
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = list(it.dropwhile(lambda x: x < 5, numeros)) # [5, 6, 7, 8, 9, 10]
resultadov2 = [x for x in numeros if x >= 5] # [5, 6, 7, 8, 9, 10]

# takewhile toma los primeros elementos de un iterable mientras se cumpla una condición
resultado2 = list(it.takewhile(lambda x: x < 5, numeros)) # [1, 2, 3, 4]
resultadov22 = [x for x in numeros if x < 5] # [1, 2, 3, 4]

# chain une varios iterables en uno solo
lista1 = [1, 'b', 3]
lista2 = ['a', 'b', 2]
numeros = list(filter(lambda e: str(e).isdigit(), it.chain(lista1, lista2))) # [1, 3, 2]
print(numeros) # [1, 3, 2]
cadenas = list(filter(lambda e: str(e).isalpha(), it.chain(lista1, lista2))) # ['b', 'a', 'b']
print(cadenas) # ['b', 'a', 'b']

# ejemplo uso itertools repeat
lista_cadenas = list(it.repeat("hola", 3)) # ['hola', 'hola', 'hola']
lista_cadenas2 = ["hola" for _ in range(3)] # ['hola', 'hola', 'hola']
lista_cadenas3 = ["hola"] * 3 # ['hola', 'hola', 'hola']
lista_cadenas4 = ["hola"*3] # ['holaholahola']

# ejemplo uso itertools islice
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sublista = list(it.islice(lista, 2, 8, 2)) # [3, 5, 7]
sublista2 = [lista[i] for i in range(2, 8, 2)] # [3, 5, 7]
sublista3 = lista[2:8:2] # [3, 5, 7]

# juntar listas con zip
nombres = ["Ana", "Luis", "María"]
edades = [28, 34, 22]
combinado = list(zip(nombres, edades)) # [('Ana', 28), ('Luis', 34), ('María', 22)]
print(combinado)

modelos_coches = ["Tesla Model S", "BMW i3", "Nissan Leaf"]
precios_coches = [79999, 44450, 31999]
coches = list(zip(modelos_coches, precios_coches)) # [('Tesla Model S', 79999), ('BMW i3', 44450), ('Nissan Leaf', 31999)]
caros = reduce(lambda x, y: x + ' - ' + y,
            map(lambda coche: coche[0],
                filter(lambda coche: coche[1] > 40000, 
                    zip(modelos_coches, precios_coches))))
print(caros) # Tesla Model S - BMW i3
caros2 = ' - '.join([coche[0] for coche in zip(modelos_coches, precios_coches) if coche[1] > 40000])
print(caros2) # Tesla Model S - BMW i3