import os

ruta_archivo = os.path.join('ficheros', 'DSQA-full.csv')

# Ejemplo lectura de fichero y uso de metodos de leer líneas
with open(ruta_archivo, encoding="utf-8") as f: # Asegura la codificación correcta
    lines = [line.strip() for line in f.readlines()] # Elimina espacios en blanco al inicio y final de cada línea, incluyendo saltos de línea, crea una lista donde cada elemento es una línea del fichero

print(lines)