frase = "Programo en Python"
# Ejemplos de métodos de cadenas
# Ejemplo find()
# Devuelve la posición de la primera aparición del substring
print(frase.find("o")) # 2
print(frase.find("o", 3)) # 7
print(frase.find("o", frase.find("o") + 1)) # Encuentra la siguiente 'o' después de la primera
# Ejemplo count()
# Devuelve el número de apariciones del substring
print(frase.count("o")) # 3
# Ejemplo in
# Devuelve True si el substring está en la cadena, False en caso contrario
print("Python" in frase) # True
print("Java" in frase) # False
print("python" in frase) # False
print("python" in frase.lower()) # True
# Ejemplo replace()
# Reemplaza las apariciones del substring por otro substring
frase = "Tengo un perro. Me gusta mi perro"
print(frase.replace("perro", "gato")) # Tengo un gato. Me gusta mi gato (todas las apariciones)
print(frase.replace("perro", "gato", 1)) # Tengo un gato. Me gusta mi perro (solo la primera aparición)
# Ejemplos de split()
# Divide la cadena en una lista de substrings usando el separador indicado
frase = "Python es un lenguaje de programación"
palabras = frase.split()
print(palabras) # ['Python', 'es', 'un', 'lenguaje', 'de', 'programación']
frase_csv = "manzana,banana,naranja,pera"
frutas = frase_csv.split(",")
print(frutas) # ['manzana', 'banana', 'naranja', 'pera']
# Ejemplo splitlines()
# Divide la cadena en una lista de líneas
texto = "Primera línea\nSegunda línea\nTercera línea"
lineas = texto.splitlines()
print(lineas) # ['Primera línea', 'Segunda línea', 'Tercera línea']

# Ejemplos de partition()
# Divide la cadena en tres partes: antes del separador, el separador, y después del separador
traduce = "silla:chair"
#print(traduce.partition(":")) # ('silla', ':', 'chair')
palabra_es, separador, palabra_en = traduce.partition(":")
traduccion_inversa = palabra_en + separador + palabra_es
print(traduccion_inversa)
traduccion_inversa = traduce.partition(":")[2] + traduce.partition(":")[1] + traduce.partition(":")[0]
print(traduccion_inversa)