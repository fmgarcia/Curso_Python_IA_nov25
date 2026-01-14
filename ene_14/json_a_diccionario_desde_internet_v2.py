import json
import urllib.request as requests
import csv

cantidad_datos = 10
# Abrir csv para escribir los datos de varios personajes
with open('./ficheros/personajes_sw.csv', mode='w', newline='', encoding='utf-8') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerow(['Nombre', 'Color de ojos', 'Número de películas'])  # Escribir encabezados

    for i in range(1, cantidad_datos+1):
        url=f"https://swapi.info/api/people/{i}/"
        personaje = json.loads(requests.urlopen(url).read())
        escritor_csv.writerow([personaje['name'],  personaje['eye_color'], len(personaje['films'])])  # Escribir datos del personaje
