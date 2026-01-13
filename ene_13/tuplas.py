punto1 = (4, 8)
punto2 = 5, 3
nombres = ("Juan", "Pedro", "Marcos")
ordenado = sorted(nombres) # Ok, no modifica la tupla
print(ordenado) # ['Juan', 'Marcos', 'Pedro']
#nombres[2] = "María" # TypeError: 'tuple' object does not support item assignment