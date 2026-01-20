'''
●Crea una lista de diccionarios que contengan la información de una persona
(nombre, edad y fecha de nacimiento). Crea al menos 4 personas.
–La fecha de nacimiento será un objeto date
–Muestra la información de la lista formateada en una tabla. La fecha de
nacimiento formateala como en el siguiente ejemplo:
○10/05/1990 (jueves)
'''

from datetime import date
import locale

locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')  # Configurar, la cadena es_ES.UTF-8 representa el locale español en sistemas Unix/Linux
personas = [
    {"nombre": "Ana", "edad": 30, "fecha_nacimiento": date(1993, 5, 10)},
    {"nombre": "Luis", "edad": 25, "fecha_nacimiento": date(1998, 8, 22)},
    {"nombre": "Marta", "edad": 40, "fecha_nacimiento": date(1983, 12, 5)},
    {"nombre": "Carlos", "edad": 35, "fecha_nacimiento": date(1988, 3, 15)},
]

print(f"{'Nombre':<10} {'Edad':<5} {'Fecha de Nacimiento':<30}")
print("-" * 50)
for persona in personas:
    fecha_nac = persona["fecha_nacimiento"]
    fecha_formateada = fecha_nac.strftime(f"%d/%m/%Y (%A)")
    print(f"{persona['nombre']:<10} {persona['edad']:<5} {fecha_formateada:<30}")