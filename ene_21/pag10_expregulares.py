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
cadena = "Mi teléfono es 543582342 y mi DNI es 53954044T, tengo como mail a@a.com y nací el 27/07/1976 en Alicante"
reg_dni = r'(\d{8})([A-Z])' # Expresión regular para un DNI español: 8 dígitos seguidos de una letra mayúscula

def extraer_dnis(texto: str) -> list[str]:
    '''
    Esta función extrae y valida los DNI de una cadena de texto.\n
    texto: Cadena de texto a procesar\n
    return: Lista de DNI válidos encontrados
    '''
    return [f"{c[0]}{c[1]}" for c in re.findall(reg_dni, texto) if mf.dni_correcto(int(c[0]), c[1])]


def procesar_texto(texto_entrada: str, nombre_archivo: str) -> dict:
    '''
    Esta función procesa una cadena de texto para extraer y validar
    números de teléfono, DNI, correos electrónicos y fechas.\n
    texto_entrada: Cadena de texto a procesar\n
    return: Diccionario con listas de datos extraídos y validados
    '''
    # 1. Extracciones
    dnis = extraer_dnis(texto_entrada)
    #teléfonos = extraer_telefonos(texto_entrada)
    #emails = extraer_correos(texto_entrada)
    #fechas = extraer_fechas(texto_entrada)
    
    # 2. Empaquetado
    datos_completos = {
        "dnis": dnis,
        #"teléfonos": teléfonos,
        #"emails": emails,
        #"fechas": fechas
    }
    # 3. Guardar en CSV
    #mf.guardar_datos_csv(nombre_archivo, datos_completos)
    # 4. Retorno
    return datos_completos



if __name__ == "__main__":   
    diccionario_procesado = procesar_texto(cadena, nombre_archivo)
    print(diccionario_procesado)