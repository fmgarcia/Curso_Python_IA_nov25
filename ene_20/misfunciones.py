from dateutil.relativedelta import relativedelta
from datetime import datetime

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