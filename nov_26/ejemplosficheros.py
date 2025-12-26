import os

# Sube un directorio (..) y luego entra a 'datos'
ruta_archivo = os.path.join('ficheros', 'fichero1.txt')
print(os.getcwd())
# Ejemplo lectura de fichero y uso de metodos de leer líneas
with open(ruta_archivo) as f:
    lines = [line.strip() for line in f.readlines()]


print(lines)
print(lines[0].encode('utf-8').decode('utf-8'))  # Primera línea