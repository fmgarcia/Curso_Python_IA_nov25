frutas = { "fresa", "plátano", "pera" } # Crear un conjunto con tres frutas
print(frutas) # {'plátano', 'fresa', 'pera'}
frutas = set(["fresa", "plátano", "pera", "plátano", "pera", "pera"]) # Los duplicados se eliminan
print(frutas) # {'plátano', 'fresa', 'pera'}
letras = set("esternocleidomastoideo") # Convertir la cadena en un conjunto de letras únicas
print(letras) # {'c', 'a', 'm', 'r', 's', 'n', 't', 'd', 'o', 'l', 'e', 'i'}
palabras = set({ "silla": "chair", "mesa": "table", "cuchara": "spoon"}) # Convertir las claves del diccionario en un conjunto
print(palabras) # {'silla', 'mesa', 'cuchara'}
frutas.add("manzana") # Agregar un elemento
print(frutas) # {'plátano', 'fresa', 'pera', 'manzana'}
frutas.remove("fresa") # Eliminar un elemento. Si no existe, lanza KeyError
print(frutas) # {'plátano', 'pera', 'manzana'}
print("manzana" in frutas) # True
print("fresa" in frutas) # False

frutas1 = { "fresa", "plátano", "pera" }
frutas2 = { "fresa", "manzana", "coco"}
# Intersección (elementos en ambos conjuntos)
print(frutas1 & frutas2) # {'fresa'}
# Union (combinacion de todos los elementos)
print(frutas1 | frutas2) # {'coco', 'manzana', 'plátano', 'fresa', 'pera'}
# Diferencia (elementos que están en A pero no en B)
print(frutas1 - frutas2) # {'pera', 'plátano'}
# Diferencia simétrica (Elementos que no están en ambos)
print(frutas1 ^ frutas2) # {'coco', 'manzana', 'plátano', 'pera'}

frutas1 = { "fresa", "plátano", "pera", "manzana" }
frutas2 = { "fresa", "manzana"}
# subconjunto (A es subconjunto de B)
print(frutas2 < frutas1) # True
print(frutas2 <= frutas1) # True (subconjunto o iguales)
# superconjunto (A es subconjunto de B)
print(frutas2 > frutas1) # False
print(frutas1 > frutas2) # True