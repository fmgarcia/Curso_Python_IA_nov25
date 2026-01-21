'''
●A partir de la cadena del ejercicio anterior (contiene 3 fechas en formato
dd/mm/yyyy), crea otra cadena con las fechas en formato yyyy-mm-dd
–Utiliza solo métodos de expresiones regulares para ello
'''
import re
cadena = "Hoy es 21/06/2024, mañana será 22/06/2024 y ayer fue 20/06/2024."
exp = r'(?P<dia>\d{2})/(?P<mes>\d{2})/(?P<anyo>\d{4})'

def cambiar_formato_fecha(match: re.Match) -> str: # función de reemplazo
    dia = match.group(1)
    mes = match.group(2)
    año = match.group(3)
    return f"{año}-{mes}-{dia}"

nueva_cadena = re.sub(exp, cambiar_formato_fecha, cadena)
print(nueva_cadena)
nueva_cadena = re.sub(exp, lambda m: f"{m.group(3)}-{m.group(2)}-{m.group(1)}", cadena)
print(nueva_cadena)
nuevas_fechas = re.sub(exp, r'\3-\2-\1', cadena)
print(nuevas_fechas)
nueva_cadena = re.sub(exp, r'\g<anyo>-\g<mes>-\g<dia>', cadena)
print(nueva_cadena)