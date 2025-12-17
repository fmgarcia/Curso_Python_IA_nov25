numero_segundos = int(input("Introduce el número de segundos a convertir: "))
dias = numero_segundos // (3600*24) # Calcular días completos
resto_segundos = numero_segundos % (3600*24) # Segundos restantes después de días
horas = resto_segundos // 3600 # Calcular horas completas
resto_segundos = resto_segundos % 3600 # Segundos restantes después de horas
minutos = resto_segundos // 60 # Calcular minutos completos
segundos = resto_segundos % 60 # Segundos restantes después de minutos

print(f"{numero_segundos} segundos son equivalentes a {dias} días, {horas} horas, {minutos} minutos y {segundos} segundos.")