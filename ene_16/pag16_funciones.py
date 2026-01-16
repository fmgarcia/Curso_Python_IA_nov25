'''
●Crea una función que reciba una cadena, un carácter de separación y un número n.
–Por defecto el número n tendrá el valor 1
●La función devolverá una cadena con el separador cada n caracteres (ten en
cuenta que al insertar el separador, la siguiente posición se incrementa en 1.
●Por ejemplo, si recibimos “Hay una mosca en mi sopa”, ‘*’ y 3, devolveremos:
“Hay* un*a m*osc*a e*n m*i s*opa”
●Llámala con parámetros posicionales y nominales
'''

def modificador_cadena(cadena, separador='-', n=1):
    cadena_modificada = ""
    contador = 0
    for char in cadena:
        cadena_modificada += char
        contador += 1
        if contador == n:
            cadena_modificada += separador
            contador = 0
    print(cadena_modificada)

# Recorriendo con un índice    
def mezclar_letras(cadena, separador, n=1):
    cadena_modificada = ""
    for i, char in enumerate(cadena):
        cadena_modificada += char
        if (i + 1) % n == 0 and (i + 1) != len(cadena):
            cadena_modificada += separador
    print(cadena_modificada)

# Con slicing    
def mezclar_letras2(cadena, separador, n=1):
    cadena_modificada = cadena[:n]
    for i in range(n, len(cadena), n):
        cadena_modificada += separador + cadena[i:i+n]
    print(cadena_modificada)
    
def mezclar_letras3(cadena, separador, n=1):
    cadena_modificada = ""
    for i in range(0, len(cadena), n):
        if i + n < len(cadena):
            cadena_modificada += cadena[i:i+n] + separador
        else:
            cadena_modificada += cadena[i:i+n]
    print(cadena_modificada)
    
# Con funciones
def mezclar_letras4(cadena, separador, n=1):
    return separador.join([cadena[i:i+n] for i in range(0, len(cadena), n)]) # La lista por comprensión crea los trozos de cadena. Ejemplo: ['Hay', ' un', 'a m', 'osc', 'a e', 'n m', 'i s', 'opa']

texto_largo_en_una_linea = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."


if __name__ == "__main__":
    modificador_cadena("Hay una mosca en mi sopa", "*", 3)
    mezclar_letras(cadena="Hay una mosca en mi sopa", separador='*', n=3)
    mezclar_letras2(cadena="Hay una mosca en mi sopa", separador='*', n=3)
    mezclar_letras3(cadena="Hay una mosca en mi sopa", separador='*', n=3)
    print(mezclar_letras4(cadena="Hay una mosca en mi sopa", separador='*', n=3))
    print(mezclar_letras4(cadena=texto_largo_en_una_linea, separador='\n', n=80))