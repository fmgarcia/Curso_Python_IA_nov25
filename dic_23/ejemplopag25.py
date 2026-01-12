lado = int(input("Lado del cuadrado: "))
# Cabeceras del conjunto
for alto in range(0, lado):
    # Cabeceras de cada uno de los elementos de un conjunto
    for ancho in range(0, lado):
        print("*", end="")
    # En esta sección son los subtotales de cada uno de los elementos
    print() # Salto de línea al final de la fila
# El total general