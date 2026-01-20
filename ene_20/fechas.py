# Fichero donde explicaremos todo los relacionado con funciones con fechas en Python
from datetime import date, time, datetime, timedelta

hoy = date.today() # Fecha de hoy
print("Hoy es:", hoy)  # Hoy es: 2024-06-15 (por ejemplo)
print("Año:", hoy.year)  # Año: 2024
print("Mes:", hoy.month)  # Mes: 6
print("Día:", hoy.day)  # Día: 15

print(datetime.now())  # Fecha y hora actual: 2024-06-15 14:30:45.123456 (por ejemplo)
fecha = datetime.now()
print("Año:", fecha.year)  # Año: 2024
print("Mes:", fecha.month)  # Mes: 6
print("Día:", fecha.day)  # Día: 15
print("Hora:", fecha.hour)  # Hora: 14
print("Minuto:", fecha.minute)  # Minuto: 30
print("Segundo:", fecha.second)  # Segundo: 45
print("Microsegundo:", fecha.microsecond)  # Microsegundo: 123456

# Crear una fecha específica
fecha_especifica = date(2023, 12, 25)  # Navidad 2023
print("Fecha específica:", fecha_especifica)  # Fecha específica: 2023-12-25
# Crear una fecha y hora específica utilizando ISO 8601
# https://en.wikipedia.org/wiki/ISO_8601
fecha_hora_especifica = datetime.fromisoformat("2023-12-25T15:30:00")
print("Fecha y hora específica:", fecha_hora_especifica)  # Fecha y hora
fecha_especifica = datetime(2023, 12, 25, 15, 30, 0)
print("Fecha y hora específica:", fecha_especifica)  # Fecha y hora específica: 2023-12-25 15:30:00
# en formato español
fecha_especifica = datetime.strptime("25/12/2023 15:30:00", "%d/%m/%Y %H:%M:%S")
print("Fecha y hora específica (formato español):", fecha_especifica)  # Fecha y hora específica (formato español): 2023-12-25 15:30:00

# Dentro de 10 horas
diez_horas_despues = datetime.now() + timedelta(hours=10)
print("Dentro de 10 horas será:", diez_horas_despues)
diez_horas_despues = datetime.fromtimestamp(datetime.now().timestamp() + 10 * 3600)
print("Dentro de 10 horas será (método alternativo):", diez_horas_despues)

# Incrementar días, semanas, meses, años
ahora = datetime.now()
print("Ahora:", ahora)
diez_dias_despues = ahora + timedelta(days=10)
print("Dentro de 10 días será:", diez_dias_despues)
ayer = ahora - timedelta(days=1)
print("Ayer fue:", ayer)
incrementar_tiempo = ahora - timedelta(days=365, hours=12, minutes=30)

# Diferencia entre dos fechas
from dateutil.relativedelta import relativedelta
ahora = datetime.now()
nacimiento = datetime.fromisoformat("1990-05-15 10:00:00")
diferencia_in_years = relativedelta(ahora, nacimiento).years
print(f"Diferencia en años: {diferencia_in_years} años")  # Diferencia en años: 35 años (por ejemplo)

# Fechas en formato español utilizando locale
import locale
locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')  # Configurar, la cadena es_ES.UTF-8 representa el locale español en sistemas Unix/Linux
fecha = datetime.today()
fecha_formateada = fecha.strftime("%A, %d de %B de %Y") # Formato largo en español
print("Fecha formateada en español:", fecha_formateada)  # Fecha formateada en español: sábado, 15 de junio de 2024 (por ejemplo)
print(fecha.strftime("Día %d del mes %B del año %Y (%A)"))  # Día 15 del mes junio del año 2024 (sábado)

# Zonas horarias con tz dentro de dateutil
from dateutil import tz
spain = tz.gettz("Europe/Madrid")
canarias = tz.gettz("Atlantic/Canary")
evento = datetime.fromisoformat("2026-01-24 22:00:00")
donde_estoy = datetime.now(tz=tz.tzlocal()) # Zona horaria local: Europe/Madrid por ejemplo
ahora_spain = datetime.now(tz=spain)
ahora_canarias = datetime.now(tz=canarias)
evento_canarias = evento.astimezone(canarias)
print("Evento en Madrid:", evento)
print("Evento en Canarias:", evento_canarias)
print("Ahora en mi zona horaria:", donde_estoy)
print("Ahora en España:", ahora_spain)
print("Ahora en Canarias:", ahora_canarias)

