persona = {
"nombre": "Juan",
"edad": 32,
}

''' Otras formas de crear diccionarios
persona = dict(nombre="Juan", edad=32) # clave=valor
d = dict(["a1", "b2", "c3", "a4"])
print(d)
persona = dict([["nombre", "Juan"], ["edad", 32]])
'''

# Acceder a los valores
print(persona["nombre"]) # Juan
#print(persona["mail"]) # KeyError

print(persona.get("nombre")) # Juan
print(persona.get("mail")) # None

if "mail" in persona:
    print(persona["mail"])
if persona.get("mail") is not None:
    print(persona["mail"])
if persona.get("nombre") is not None:
    print(persona["nombre"])
    
print("persona['mail']" if "mail" in persona else "No tiene mail")

# Ordenar diccionarios

notas = [
    {"asignatura": "Matemáticas", "nota": 8},
    {"asignatura": "Historia", "nota": 6},
    {"asignatura": "Lengua", "nota": 7},
    {"asignatura": "Inglés", "nota": 9},
]

notas.sort(key=lambda x: x["nota"]) # Ordena por nota ascendente
print(notas)
notas.sort(key=lambda x: x["nota"], reverse=True) # Ordena por nota descendente
print(notas)

# Recorrer diccionarios

alumnos = [
    { "nombre": "Ana", "matematicas": 8, "historia": 7, "lengua": 9, "ingles": 6 },
    { "nombre": "Luis", "matematicas": 6, "historia": 8, "lengua": 7, "ingles": 9 },
    { "nombre": "Maria", "matematicas": 9, "historia": 6, "lengua": 8, "ingles": 7 },
    { "nombre": "Carlos", "matematicas": 7, "historia": 9, "lengua": 6, "ingles": 8 },
]

for alumno in alumnos:
    print("Nombre:", alumno["nombre"])
    print(f"  Matemáticas: {alumno['matematicas']}, Historia: {alumno['historia']}, Lengua: {alumno['lengua']}, Inglés: {alumno['ingles']}")
    
diccionario = [
    {"espanol": "rojo", "ingles": "red", "frances": "rouge"},
    {"espanol": "verde", "ingles": "green", "frances": "vert"},
    {"ingles": "blue", "frances": "bleu"},
    {"espanol": "amarillo", "ingles": "yellow", "frances": "jaune"},
]

# Mostrar todas las palabras en español
idioma = 'espanol'
for palabra in diccionario:
    print(palabra.get(idioma, "N/A"))


# Buscar la traducción de una palabra dada en español
termino = 'verde'
idioma = 'espanol'
encontrado = False    
for palabra in diccionario:
    if termino in palabra.values():
        print(f"Traducción de '{termino}' en inglés: {palabra.get('ingles', 'N/A')}")
        encontrado = True
        break
if not encontrado:
    print(f"La palabra '{termino}' no se encontró en el diccionario.")
    
# Modificar el contenido de un diccionario
persona = {
    "nombre": "Juan",
    "edad": 32,
}
persona["edad"] = 33 # Modifica la edad
persona["mail"] = "juan@example.com" # Agrega el mail
print(persona) # {'nombre': 'Juan', 'edad': 33, 'mail': 'juan@example.com'}

diccionario_vacio = {}
cantidad_elementos = 10
for i in range(1, cantidad_elementos + 1):
    diccionario_vacio[i] = i ** 2
print(diccionario_vacio)

# Búsqueda en diccionarios. Diferencias entre keys() y values()
traducciones = {
    "rojo": "red",
    "verde": "green",
    "azul": "blue",
}

print("rojo" in traducciones.keys()) # True
print("rojo" in traducciones) # True
print("red" in traducciones) # False
print("red" in traducciones.values()) # True

# moverte por las claves de un diccionario
for clave in traducciones:
    print(f"{clave} => {traducciones[clave]}")
# moverte por los valores de un diccionario
for valor in traducciones.values():
    print(valor)
# moverte por las claves y valores de un diccionario
for k,v in traducciones.items():
    print(f"{k} => {v}")
    
# Mejora sobre las búsquedas en un diccionario español-inglés
# Buscar la traducción de una palabra dada en español
idioma_origen = 'espanol'
idioma_destino = 'ingles'
#termino = input(f"Ingrese una palabra en {idioma_origen} para traducir al {idioma_destino}: ").strip().lower()
termino = 'rojo'
encontrado = False    
for palabra in diccionario:
    if termino in palabra.values() and palabra[idioma_origen] == termino:
        print(f"Traducción de '{termino}' en {idioma_destino}: {palabra.get(idioma_destino, 'N/A')}")
        encontrado = True
        break
if not encontrado:
    print(f"La palabra '{termino}' no se encontró en el diccionario.")
  
# Modificar el contenido de un elemento de una lista de diccionarios  
alumnos = [
    { "nombre": "Ana", "matematicas": 8, "historia": 7, "lengua": 9, "ingles": 6 },
    { "nombre": "Luis", "matematicas": 6, "historia": 8, "lengua": 7, "ingles": 9 },
    { "nombre": "Maria", "matematicas": 9, "historia": 6, "lengua": 8, "ingles": 7 },
    { "nombre": "Carlos", "matematicas": 7, "historia": 9, "lengua": 6, "ingles": 8 },
]

print(type(alumnos)) # <class 'list'>
print(type(alumnos[0])) # <class 'dict'>
alumnos[1]["matematicas"] = 10 # Cambia la nota de matemáticas de Luis a 10
print(alumnos[1]) # {'nombre': 'Luis', 'matematicas': 10, 'historia': 8, 'lengua': 7, 'ingles': 9}
for alumno in alumnos:
    print(alumno.get("nombre", "N/A"))
# Listado de los alumnos junto con su nota media
for alumno in alumnos:
    nombre, *notas = list(alumno.values())
    print(f"{nombre}: {sum(notas)/len(notas):.2f}")
    
alumnos_notas = [
    { "Ana": [8, 7, 9, 6] },
    { "Luis": [6, 10, 7, 10] },
    { "Maria": [9, 6, 8, 7] },
    { "Carlos": [7, 9, 6, 8] },
]

for alumno in alumnos_notas:
    for nombre, notas in alumno.items():
        print(f"{nombre}: {sum(notas)/len(notas):.2f}")

# Calcular la nota media de las asignaturas si tenemos una lista de valores y otra de nombres de alumnos
alumnos = ["Ana", "Luis", "Maria", "Carlos"]
notas = [
    [8, 7, 9, 6],  # Notas de Ana
    [6, 10, 7, 10],# Notas de Luis
    [9, 6, 8, 7],  # Notas de Maria
    [7, 9, 6, 8],  # Notas de Carlos
]

# Recorrer solo las notas
for grupo_notas in notas:
    print(f"Media: {sum(grupo_notas)/len(grupo_notas):.2f}")
# Recorrer los nombres y las notas
for nombre, grupo_notas in zip(alumnos, notas):
    print(f"{nombre}: {sum(grupo_notas)/len(grupo_notas):.2f}")
    
# Combinación de diccionarios
colores = { "rojo": "red", "verde": "green" }
mas_colores = { "azul": "blue", "amarillo": "yellow" }
todos_los_colores = { **colores, **mas_colores } # Lo que hace es crear un nuevo diccionario combinando los dos
print(todos_los_colores) # {'rojo': 'red', 'verde': 'green', 'azul': 'blue', 'amarillo': 'yellow'}
colores.update(mas_colores) # Modifica el diccionario original colores agregando los elementos de mas_colores
print(colores) # {'rojo': 'red', 'verde': 'green', 'azul': 'blue', 'amarillo': 'yellow'}
valor_borrado = colores.pop("rojo") # Elimina el elemento con clave 'rojo'
print(f"Valor borrado: {valor_borrado}") # Valor borrado: red
print(colores) # {'verde': 'green', 'azul': 'blue', 'amarillo': 'yellow'}
del colores["verde"] # Elimina el elemento con clave 'verde'
print(colores) # {'azul': 'blue', 'amarillo': 'yellow'}

# Diccionarios por comprensión
palabras = ["rojo", "verde", "azul"]
longitudes = { palabra: len(palabra) for palabra in palabras if 'e' in palabra }
print(longitudes) # {'verde': 5}

# A partir de un texto, crear un diccionario con las palabras y su longitud (sin signos de puntuación y en minúsculas)
import re
texto = "En un lugar de La Mancha, de cuyo nombre no quiero acordarme: Existía una persona... y más"
diccionario = {}
separadores = "[,;:\".\\n ]"  # Espacios, comas, puntos, saltos de línea
for palabra in re.split(separadores, texto):
    if len(palabra) > 0:
        diccionario[palabra.lower()] = len(palabra)
print(diccionario)

# El mismo ejercicio sin expresiones regulares
texto = "En un lugar de La Mancha, de cuyo nombre no quiero acordarme: Existía una persona... y más"
diccionario = {}
for palabra in texto.split():
    diccionario[palabra.lower()] = len(palabra)
print(diccionario)

# A partir de un texto, crear un diccionario con las palabras y el número de veces que aparecen (sin signos de puntuación y en minúsculas)
# Análisis de sentimiento básico
import re
texto = '''
Hoy decidí despertar con gratitud, reconociendo que cada amanecer es un regalo extraordinario. Al abrir los ojos, sentí una profunda paz interior y la certeza de que este día está lleno de posibilidades maravillosas.
Tengo la confianza plena en que soy capaz de alcanzar mis sueños. Afrontaré cualquier reto con valentía y entusiasmo, sabiendo que cada paso es un progreso hacia mi éxito personal. Elijo rodearme de armonía, compartir bondad con los demás y mantener una actitud brillante ante la vida.
Mi corazón está lleno de esperanza y alegría, porque entiendo que mi fortaleza reside en mi capacidad de amar y de ver el lado luminoso de las cosas. Hoy es una oportunidad perfecta para florecer.
'''
palabras_positivas = ["mola", "genial", "bueno", "excelente", "fantástico", "gratitud", "paz", "éxito", "armonía", "bondad", "brillante", "esperanza", "alegría", "fortaleza", "amar", "luminoso", "florecer"]
palabras_negativas = ["malo", "horrible", "terrible", "pésimo", "horroroso", "odio", "tristeza", "fracaso", "conflicto", "oscuridad", "debilidad", "temor", "desesperanza", "llorar", "sufrir"]
diccionario = {}
separadores = "[,;:\".\\n ]"  # Espacios, comas, puntos, saltos de línea
numero_minimo_letras = 2
diferencia_positivas_negativas = 2
for palabra in re.split(separadores, texto):
    if len(palabra) > numero_minimo_letras:
        diccionario[palabra.lower()] = diccionario[palabra.lower()] + 1 if palabra.lower() in diccionario else 1
numero_palabras_positivas = sum(diccionario[palabra] for palabra in diccionario if palabra in palabras_positivas)
numero_palabras_negativas = sum(diccionario[palabra] for palabra in diccionario if palabra in palabras_negativas)
print("El texto es: ", "POSITIVO" if numero_palabras_positivas > numero_palabras_negativas+diferencia_positivas_negativas else "NEGATIVO" if numero_palabras_negativas > numero_palabras_positivas+diferencia_positivas_negativas else "NEUTRO")