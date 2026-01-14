import json
import urllib.request as requests
url="https://swapi.info/api/people/1/"
luke_dict = json.loads(requests.urlopen(url).read())
print(f"{luke_dict['name']} tiene los ojos de color {luke_dict['eye_color']} y ha aparecido en {len(luke_dict['films'])} películas que son:")
for pelicula in luke_dict['films']:
    pelicula_dict = json.loads(requests.urlopen(pelicula).read())
    print(f"- {pelicula_dict['title']} ({pelicula_dict['release_date']})")