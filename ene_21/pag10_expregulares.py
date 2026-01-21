'''
Queremos a partir de una cadena de texto extraer:
- Números de teléfono (formato español, 9 dígitos, puede llevar espacios o guiones)
- DNI (8 dígitos seguidos de una letra mayúscula)
- Correos electrónicos (formato básico: letras, números, puntos, guiones o guion bajo antes de la @, luego dominio con letras, números, puntos o guiones, y finalmente un TLD de 2 a 6 letras)
- Fechas en formato dd/mm/yyyy o dd-mm-yyyy
Usa expresiones regulares para extraer esta información e imprimirla por pantalla.
- Para cada tipo de dato, muestra todas las coincidencias encontradas en la cadena.
- Asegúrate de que las expresiones regulares son lo suficientemente robustas para evitar falsos positivos.
- Para cada fecha encontrada, valida que la fecha sea correcta (por ejemplo, no debería aceptar 32/13/2020).
- Mostrar los años, meses y días de vida si la fecha es una fecha de nacimiento válida.
- Para cada DNI encontrado, valida que la letra sea correcta según el número.
- Para cada correo electrónico, valida que el formato sea correcto.
Crea funciones para cada tipo de dato que realicen la extracción y validación, ya que luego las podremos reutilizar en otros programas.
- Guarda toda la información extraída en un fichero csv con columnas para cada tipo de dato.
'''
import re
import os
import sys
import csv
# Añadir la ruta de la carpeta 'mislibrerias' al sys.path para importar misfunciones
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'mislibrerias'))
try:
    import misfunciones as mf
except ImportError:
    print("No se pudo importar la librería 'misfunciones' desde la carpeta 'mislibrerias'. Asegúrate de que la ruta es correcta.")


nombre_archivo = "./ficheros/datos_extraidos.csv"
cadena = """
    Mi teléfono es 643582342 y mi DNI es 53954044T, tengo como mail a@a.com y nací el 27/07/1976 en Alicante
    Otro contacto es Luis, su teléfono es 600-123-456, DNI 87654321-Z, correo luis@example.com y nació el 15-08-1980.
    Contacto adicional: Ana, teléfono 700 654 321, DNI 12345678A, email ana@ana.com y fecha de nacimiento 31/02/1990.
    """

if __name__ == "__main__":   
    diccionario_procesado = mf.procesar_texto(cadena, nombre_archivo)
    print(diccionario_procesado)