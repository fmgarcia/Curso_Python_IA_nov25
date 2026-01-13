'''
Trabajo con listas y colecciones en Python.
'''
# Trabajo con listas

# Definición de una lista
frutas = ['manzana', 'banana', 'cereza', 'durazno']
numeros = [1, 2, 3, 4, 5]
numeros2 = list(range(1, 11))  # Números del 1 al 10
pares = list(range(2, 101, 2))  # Números pares del 2 al 100
letras = list('Python') #  ['P', 'y', 't', 'h', 'o', 'n']

# Acceso a elementos
primera_fruta = frutas[0]  # 'manzana'
ultima_fruta = frutas[-1]  # 'durazno'
# print(frutas[4])  # IndexError: list index out of range

# Las listas son mutables
frutas[1] = 'kiwi'  # Cambia 'banana' por 'kiwi'

# Insertar en listas
frutas.append('naranja')  # Agrega 'naranja' al final ['manzana', 'kiwi', 'cereza', 'durazno', 'naranja']
frutas.insert(2, 'mango')  # Inserta 'mango' en la posición 2 ['manzana', 'kiwi', 'mango', 'cereza', 'durazno', 'naranja']
frutas.insert(-2, 'uva')  # Inserta 'uva' en la penúltima posición ['manzana', 'kiwi', 'mango', 'cereza', 'uva', 'durazno', 'naranja']

# Eliminar de listas
frutas.remove('cereza')  # Elimina 'cereza' ['manzana', 'kiwi', 'mango', 'uva', 'durazno', 'naranja']. Borra la primera ocurrencia
fruta_eliminada = frutas.pop()  # Elimina y devuelve el último elemento 'naranja' ['manzana', 'kiwi', 'mango', 'uva', 'durazno']
fruta_eliminada_pos = frutas.pop(1)  # Elimina y devuelve el elemento en la posición 1 'kiwi' ['manzana', 'mango', 'uva', 'durazno']
del frutas[0]  # Elimina el elemento en la posición 0 ['mango', 'uva', 'durazno']
# fruta_eliminada_no_existe = frutas.remove('piña')  # ValueError: list.remove(x): x not in list
frutas.clear()  # Elimina todos los elementos de la lista []

frutas = ['manzana', 'kiwi', 'mango', 'uva', 'pera']  # Restaurar lista para siguientes ejemplos

# invertir listas
frutas.reverse()  # Invierte el orden de la lista ['pera', 'uva', 'mango', 'kiwi', 'manzana']. La lista original se modifica.
print(frutas) # Imprime la lista invertida.
lista_invertida = frutas[::-1]  # Crea una nueva lista invertida ['manzana', 'kiwi', 'mango', 'uva', 'pera']. La lista original no se modifica.
print(lista_invertida) # Imprime la nueva lista invertida.
lista_invertida2 = list(reversed(frutas))  # Crea una nueva lista invertida ['manzana', 'kiwi', 'mango', 'uva', 'pera']. La lista original no se modifica.
print(lista_invertida2) # Imprime la nueva lista invertida.

# Recorrer listas
# Cuando no me importa el índice
for fruta in frutas:
    print(f"{fruta} tiene {len(fruta)} letras.")
# Cuando me importa el índice con enumerate
for indice, fruta in enumerate(frutas):
    print(f"La fruta en la posición {indice} es {fruta}.")
# Uso de range para generar índices. Similar a como se hace en otros lenguajes.
for i in range(len(frutas)):
    print(f"La fruta en la posición {i} es {frutas[i]}.")
    
# Trabajo con sublistas (slicing)
# Lista[inicio:fin:salto]. El inicio y el fin son opcionales. El salto es opcional y por defecto es 1. inicio y fin pueden ser índices negativos.
print(frutas)  # ['pera', 'uva', 'mango', 'kiwi', 'manzana']
frutas_sublista = frutas[1:4]  # Sublista desde el índice 1 hasta el 3 ['uva', 'mango', 'kiwi']
print(frutas_sublista)
frutas_sublista_inicio = frutas[:3]  # Sublista desde el inicio hasta el índice 2 ['pera', 'uva', 'mango']
print(frutas_sublista_inicio)
frutas_sublista_final = frutas[2:]  # Sublista desde el índice 2 hasta el final ['mango', 'kiwi', 'manzana']
print(frutas_sublista_final)
frutas_sublista_toda = frutas[:]  # Copia de toda la lista ['pera', 'uva', 'mango', 'kiwi', 'manzana']
print(frutas_sublista_toda)
frutas_sublista_saltos = frutas[::2]  # Sublista con saltos de 2 ['pera', 'mango', 'manzana']. Los elementos en posiciones con índice par.
print(frutas_sublista_saltos)
frutas_sublista_invertida_saltos = frutas[::-2]  # Sublista invertida con saltos de 2 ['manzana', 'mango', 'pera']
print(frutas_sublista_invertida_saltos)
frutas_sublista_invertida_saltos_limitada = frutas[-1:-4:-2]  # Sublista invertida desde el final hasta el índice -4 ['manzana', 'mango']
print(frutas_sublista_invertida_saltos_limitada)

# Modificación de sublistas
numeros = [1, 2, 3, 4, 5]
numeros[1:4] = [20, 30, 40]  # Cambia los elementos en las posiciones 1 a 3 [1, 20, 30, 40, 5]
numeros[::2] = [10, 30, 50]  # Cambia los elementos en posiciones pares [10, 20, 30, 40, 50]
# numeros[::2] = [10, 30, 50, 70]  # Cambia los elementos en posiciones pares [10, 20, 30, 40, 50]. Te lo permite hacer pero no es recomendable ya que si te pasas dará error.

# Operaciones con listas
longitud_numeros = len(numeros)  # 5
suma_numeros = sum(numeros)  # 150
maximo_numeros = max(numeros)  # 50
minimo_numeros = min(numeros)  # 10
avg_numeros = sum(numeros) / len(numeros)  # 30.0
print(f"Longitud: {longitud_numeros}, Suma: {suma_numeros}, Máximo: {maximo_numeros}, Mínimo: {minimo_numeros}, Promedio: {avg_numeros}")

import statistics
media_numeros = statistics.mean(numeros)  # 30.0
mediana_numeros = statistics.median(numeros)  # 30
moda_numeros = statistics.mode([1, 2, 2, 3, 4])  # 2
varianza_numeros = statistics.variance(numeros)  # 400.0
desviacion_estandar_numeros = statistics.stdev(numeros)  # 20.0
print(f"Media: {media_numeros}, Mediana: {mediana_numeros}, Moda: {moda_numeros}, Varianza: {varianza_numeros}, Desviación Estándar: {desviacion_estandar_numeros}")

import numpy as np
np_numeros = np.array(numeros)
np_media = np.mean(np_numeros)  # 30.0
np_mediana = np.median(np_numeros)  # 30.0
np_varianza = np.var(np_numeros, ddof=1)  # 400.0
np_desviacion_estandar = np.std(np_numeros, ddof=1)  # 20.0
print(f"Numpy - Media: {np_media}, Mediana: {np_mediana}, Varianza: {np_varianza}, Desviación Estándar: {np_desviacion_estandar}")

# Repetición y combinación de listas
numeros = [1, 2, 3, 4, 5]
numeros2 = [6, 7, 8, 9, 10]
numeros_repetidos = numeros * 3  # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5] Repite la lista 3 veces
numeros_combinados = numeros + [6, 7, 8]  # [1, 2, 3, 4, 5, 6, 7, 8] Combina dos listas
combinacion_multiple = numeros + numeros2  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] Combina dos listas
#numeros = numeros + numeros2  # Actualiza la lista original combinándola con otra lista
#numeros += numeros2  # Actualiza la lista original combinándola con otra lista
numeros.extend(numeros2)  # Actualiza la lista original combinándola con otra lista
print(numeros)

# ordenar una lista
print("Listas modificadas y ordenadas")
palabras = ['banana', 'manzana', 'kiwi', 'cereza', 'durazno']
# Ordenar modificando la lista original
palabras.sort()  # Ordena alfabéticamente ['banana', 'cereza', 'durazno', 'kiwi', 'manzana']
print(palabras)
palabras.sort(reverse=True)  # Ordena en orden inverso ['manzana', 'kiwi', 'durazno', 'cereza', 'banana']
print(palabras)

palabras = ['banana', 'manzana', 'kiwi', 'cereza', 'durazno']
# No modificar la lista original
print("Listas sin modificar el original")
palabras_ordenadas = sorted(palabras)  # Nueva lista ordenada alfabéticamente ['banana', 'cereza', 'durazno', 'kiwi', 'manzana']
print(palabras_ordenadas)
print(sorted(palabras, reverse=True))  # Nueva lista ordenada en orden inverso ['manzana', 'kiwi', 'durazno', 'cereza', 'banana']
print(palabras)  # Lista original sin modificar ['banana', 'manzana', 'kiwi', 'cereza', 'durazno']

# ordenaciones personalizadas
palabras = ['Banana', 'manzana', 'Kiwi', 'cereza', 'durazno']
print("Ordenaciones personalizadas")
palabras.sort() # Ordena alfabéticamente considerando mayúsculas y minúsculas ['Banana', 'Kiwi', 'cereza', 'durazno', 'manzana']
print(palabras)
palabras.sort(key=len) # Ordena por longitud de palabra ['Kiwi', 'Banana', 'cereza', 'durazno', 'manzana']
print(palabras)
palabras.sort(key=str.lower) # Ordena ignorando mayúsculas y minúsculas ['banana', 'cereza', 'durazno', 'kiwi', 'manzana']
print(palabras)
palabras.sort(key=lambda x: x[-1]) # Ordena por la última letra de cada palabra ['banana', 'manzana', 'cereza', 'kiwi', 'durazno']
print(palabras)
palabras.sort(key=lambda x: x.count('a')) # Ordena por la cantidad de letras 'a' en cada palabra ['kiwi', 'cereza', 'durazno', 'banana', 'manzana']
print(palabras)
palabras.sort(key=str.casefold) # Ordena ignorando mayúsculas y minúsculas de forma más agresiva ['banana', 'cereza', 'durazno', 'kiwi', 'manzana']
print(palabras)

# Comparación de listas
print("Comparación de listas")
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = [4, 5, 6]
lista4 = lista1
print(lista1 == lista2)  # True. Mismo contenido.
print(lista1 is lista2)  # False. Diferentes objetos en memoria.
print(lista1 is lista4)  # True. Mismo objeto en memoria.
print(lista1 != lista3)  # True. Diferente contenido.
print(lista1 < lista3)   # True. Comparación lexicográfica.

# Creación de listas a partir de otras listas
print("Creación de listas a partir de otras listas")
lista_original = [1, 2, 3, 4, 5]
dobles = []
for x in lista_original:
    dobles.append(x * 2)  # [2, 4, 6, 8, 10]
print(dobles)
dobles_comp = [x * 2 for x in lista_original]  # Usando comprensión de listas [2, 4, 6, 8, 10]
cuadrado = [x ** 2 for x in lista_original]  # Usando comprensión de listas para cuadrados [1, 4, 9, 16, 25]
cuadrado_numeros_1_a_9 = [x ** 2 for x in range(1, 10)]  # Cuadrados de números del 1 al 9 [1, 4, 9, 16, 25, 36, 49, 64, 81]
pares = [x for x in lista_original if x % 2 == 0]  # Números pares [2, 4]
palabras = ['hola', 'mundo', 'python', 'es', 'genial']
mas_de_tres_letras = [e for e in palabras if len(e) > 3]  # Palabras con más de 3 letras ['hola', 'mundo', 'python', 'genial']
iniciales_palabras_mas_de_tres_letras = [e[0] for e in palabras if len(e) > 3]  # Iniciales de palabras con más de 3 letras ['h', 'm', 'p', 'g']