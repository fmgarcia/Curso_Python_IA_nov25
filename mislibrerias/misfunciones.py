from dateutil.relativedelta import relativedelta
from datetime import datetime
import re
import csv

reg_dni = r'(\d{8})[-]?([A-Z])' # Expresión regular para un DNI español: 8 dígitos seguidos de una letra mayúscula (12345678A o 12345678-A)
reg_telefono = r'(\d{3})[-\s]?(\d{3})[-\s]?(\d{3})' # Expresión regular para un número de teléfono español: 9 dígitos, puede llevar espacios o guiones (600123456, 600-123-456, 600 123 456)
reg_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}' # Expresión regular para un correo electrónico básico (letras, números, puntos, guiones o guion bajo antes de la @, luego dominio con letras, números, puntos o guiones, y finalmente un TLD de 2 a 6 letras) Ejemplos: (a@a.com, usuario.nombre@dominio.es, usuario_nombre@dominio.com)
reg_fecha = r'(\d{2})[\/-](\d{2})[\/-](\d{4})' # Expresión regular para fechas en formato dd/mm/yyyy o dd-mm-yyyy


def siguiente_letra(palabra):
    '''
    Esta función recibe una palabra y devuelve la misma palabra
    sustituyendo cada letra por la siguiente en el alfabeto.
    palabra: Palabra a transformar
    return: Palabra transformada
    '''
    return ''.join(map(lambda c: chr(ord(c) + 1) if c.isalpha() else c, palabra))

def misuma(a, b):
    '''
    Esta función recibe dos números y devuelve su suma.
    a: Primer número
    b: Segundo número
    return: Suma de a y b
    '''
    return a + b

def tu_edad(cadena: str) -> tuple:
    '''
    Esta función recibe una cadena de texto que representa una fecha
    y me devuelve tres enteros: años, meses y días de vida.
    cadena: Cadena de texto con la fecha de nacimiento en formato dd/mm/yyyy
    return: Edad como entero o -1 si no es válida
    '''
    try:
        anyos = relativedelta(datetime.now(), datetime.strptime(cadena, "%d/%m/%Y")).years
        meses = relativedelta(datetime.now(), datetime.strptime(cadena, "%d/%m/%Y")).months
        dias = relativedelta(datetime.now(), datetime.strptime(cadena, "%d/%m/%Y")).days
        return anyos, meses, dias
    except ValueError:
        return (-1, -1, -1)
    
def comprobar_fecha(fecha: str) -> bool:
    try:
        datetime.strptime(fecha, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def dni_correcto(numero: int, letra: str) -> bool:
    '''
    Esta función recibe un número de DNI y una letra y devuelve
    True si la letra es correcta para el número de DNI, False en caso contrario.
    numero: Número de DNI
    letra: Letra del DNI
    return: True si la letra es correcta, False en caso contrario
    '''
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    indice = numero % 23
    letra_correcta = letras[indice]
    return letra_correcta.upper() == letra.upper()

def telefono_correcto(telefono: str) -> bool:
    '''
    Esta función valida que un número de teléfono español sea correcto.\n
    telefono: Cadena con el número de teléfono (9 dígitos)\n
    return: True si es válido, False en caso contrario
    '''
    # Un teléfono español válido tiene 9 dígitos y empieza por 6, 7, 8 o 9
    return len(telefono) == 9 and telefono.isdigit() and telefono[0] in '6789'

def extraer_dnis(texto: str) -> list[str]:
    '''
    Esta función extrae y valida los DNI de una cadena de texto.\n
    texto: Cadena de texto a procesar\n
    return: Lista de DNI válidos encontrados
    '''
    return [f"{c[0]}{c[1]}" for c in re.findall(reg_dni, texto) if dni_correcto(int(c[0]), c[1])]

def extraer_telefonos(texto: str) -> list[str]:
    '''
    Esta función extrae y valida los números de teléfono de una cadena de texto.\n
    texto: Cadena de texto a procesar\n
    return: Lista de números de teléfono válidos encontrados
    '''
    return [f"{t[0]}{t[1]}{t[2]}" for t in re.findall(reg_telefono, texto) if telefono_correcto(f"{t[0]}{t[1]}{t[2]}")]

def extraer_correos(texto: str) -> list[str]:
    '''
    Esta función extrae y valida los correos electrónicos de una cadena de texto.\n
    texto: Cadena de texto a procesar\n
    return: Lista de correos electrónicos válidos encontrados
    '''
    return [f"{email}" for email in re.findall(reg_email, texto)]

def extraer_fechas(texto: str) -> list[str]:
    '''
    Esta función extrae y valida las fechas de una cadena de texto.\n
    texto: Cadena de texto a procesar\n
    return: Lista de fechas válidas encontradas
    '''
    return [f"{f[0]}/{f[1]}/{f[2]}" for f in re.findall(reg_fecha, texto) if comprobar_fecha(f"{f[0]}/{f[1]}/{f[2]}")]


def procesar_texto(texto_entrada: str) -> dict:
    '''
    Esta función procesa una cadena de texto para extraer y validar
    números de teléfono, DNI, correos electrónicos y fechas.\n
    texto_entrada: Cadena de texto a procesar\n
    return: Diccionario con listas de datos extraídos y validados
    '''
    # 1. Extracciones
    dnis = extraer_dnis(texto_entrada)
    teléfonos = extraer_telefonos(texto_entrada)
    emails = extraer_correos(texto_entrada)
    fechas = extraer_fechas(texto_entrada)
    
    # 2. Empaquetado
    datos_completos = {
        "dnis": dnis,
        "teléfonos": teléfonos,
        "emails": emails,
        "fechas": fechas
    }

    # 3. Retorno
    return datos_completos

def procesar_personas(texto_entrada: str) -> list[dict]:
    '''
    Esta función procesa una cadena de texto para extraer y validar
    números de teléfono, DNI, correos electrónicos y fechas.\n
    texto_entrada: Cadena de texto a procesar\n
    return: Diccionario con listas de los datos extraídos y validados por persona
    '''
    
    lineas = [l for l in texto_entrada.splitlines() if l.strip()] # Eliminar líneas vacías. Obtengo una lista donde cada elemento es una línea
    registros = []
    for linea in lineas:
        registro = {}
        dnis = extraer_dnis(linea)
        teléfonos = extraer_telefonos(linea)
        emails = extraer_correos(linea)
        fechas = extraer_fechas(linea)
        registro["dni"] = dnis[0] if dnis else ""
        registro["telefonos"] = teléfonos
        registro["emails"] = emails
        registro["fecha_nacimiento"] = fechas[0] if fechas else ""
        registros.append(registro)
       
    return registros


def guardar_datos_csv(nombre_archivo: str, datos: dict):
    '''
    Esta función guarda los datos extraídos en un archivo CSV.\n
    nombre_archivo: Nombre del archivo CSV\n
    datos: Diccionario con listas de datos a guardar
    '''
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        # Escribir la cabecera
        escritor_csv.writerow(datos.keys())
        # Obtener la longitud máxima de las listas para iterar correctamente
        max_len = max(len(v) for v in datos.values())
        for i in range(max_len):
            fila = []
            for clave in datos.keys():
                lista = datos[clave]
                if i < len(lista):
                    fila.append(lista[i])
                else:
                    fila.append('')  # Rellenar con vacío si no hay más datos
            escritor_csv.writerow(fila)
            
def guardar_personas(nombre_archivo: str, personas: list[dict]) -> bool:
    '''
    Esta función guarda los datos de las personas extraídas en un archivo CSV.\n
    nombre_archivo: Nombre del archivo CSV\n
    personas: Lista de diccionarios con los datos de cada persona
    '''
    
    if not personas:
        print("No hay datos para guardar.")
        return False  # No hay datos para guardar
    
    # Crear el encabezado dinámicamente a partir de las claves del primer diccionario
    encabezado = list(personas[0].keys())
    
    try:
        with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            # Escribir la cabecera (la primera fila)
            escritor_csv.writerow(encabezado)
            for persona in personas:
                escritor_csv.writerow([
                    persona.get("dni", ""),
                    ';'.join(persona.get("telefonos", [])),  # Unir múltiples teléfonos con ;
                    ';'.join(persona.get("emails", [])),     # Unir múltiples emails con ;
                    persona.get("fecha_nacimiento", "")
                ])
        print(f"{len(personas)} personas guardadas correctamente en {nombre_archivo}")
        return True
    except Exception as e:
        print(f"Error al guardar los datos en el archivo CSV: {e}")
        return False