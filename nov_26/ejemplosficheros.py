import os

ruta_archivo = os.path.join('ficheros', 'fichero1.txt')

# Ejemplo lectura de fichero y uso de metodos de leer líneas
with open(ruta_archivo, encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines()]

print(lines)
