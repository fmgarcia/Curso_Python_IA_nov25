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