import re
import misfunciones as mf

reg_dni = r'\d{8}[A-Z]' # Expresión regular para un DNI español: 8 dígitos seguidos de una letra mayúscula
print(reg_dni) # \d{8}[A-Z]

cadena = "Si sumamos 34 y 27, da como resultado 61"
reg_num = r'\d+' # Expresión regular para encontrar números en una cadena
coincidencia = re.search(reg_num, cadena) # Buscar la primera coincidencia de un número en la cadena
print(coincidencia) # <re.Match object; span=(11, 13), match='34'>
todas = re.findall(reg_num, cadena) # Encontrar todas las coincidencias de números en la cadena
print(todas) # ['34', '27', '61']

# Compilar la expresión regular para mejorar el rendimiento si se va a usar varias veces
compiled = re.compile(reg_num) # Compilar la expresión regular
coincidencia2 = compiled.search(cadena, 14) # Buscar la primera coincidencia de un número en la cadena a partir del índice 14
print(coincidencia2) # <re.Match object; span=(16, 18), match='27'>

cadena = "Mi DNI es 53954044T y mi teléfono es 543582342"
dni = r'(\d{8})([A-Z])'
dni_telefono = r'DNI:\s*(\d{8}[A-Z]),\s*Tel:\s*(\d{9})'
coincidencia = re.search(dni, cadena)
print(coincidencia) # <re.Match object; span=(10, 19), match='53954044T'>
print(coincidencia.groups()) # ('53954044', 'T')
print(mf.dni_correcto(int(coincidencia.group(1)), coincidencia.group(2))) # True or False depending on the correctness of the DNI letter


cadena = "Contacto: Ana, DNI: 12345678Z, Tel: 600123456; Contacto: Luis, DNI: 87654321Z, Tel: 600654321"

coincidencias = re.findall(dni, cadena)
for c in coincidencias:
    if mf.dni_correcto(int(c[0]), c[1]):
        print(f"DNI {c[0]}{c[1]} es correcto")
    else:
        print(f"DNI {c[0]}{c[1]} es incorrecto")

coincidencias = re.findall(dni_telefono, cadena)
print(coincidencias)  # [('12345678Z', '600123456'), ('87654321Z', '600654321')]
for c in coincidencias:
    dni_numero = c[0][:-1]
    dni_letra = c[0][-1]
    telefono = c[1]
    if mf.dni_correcto(int(dni_numero), dni_letra):
        print(f"DNI {dni_numero}{dni_letra} es correcto, Teléfono: {telefono}")
    else:
        print(f"DNI {dni_numero}{dni_letra} es incorrecto, Teléfono: {telefono}")
        
cadena = "Mi DNI es 54323495G y mi teléfono es 543582342"
exp = r'(?P<digitos>\d{8})(?P<letra>[A-Z])'
coincidencia = re.search(exp, cadena)
dict_coincidencia = coincidencia.groupdict() # el diccionario tiene los nombres de los grupos como claves
print(coincidencia.groupdict()) # {'digitos': '54323495', 'letra': 'G'}
print(coincidencia.group("digitos")) # 54323495
print(coincidencia.group("letra")) # G
print(dict_coincidencia) # {'digitos': '54323495', 'letra': 'G'}
print(dict_coincidencia["digitos"]) # 54323495
print(dict_coincidencia["letra"]) # G

