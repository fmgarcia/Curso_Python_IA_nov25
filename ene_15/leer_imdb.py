import requests
import csv

api_key = "6ed1c2741emshe568e48d9b8b3e0p12592djsn51b99fe0a3b1"
rapidapi_host = "imdb236.p.rapidapi.com"
url = f"https://imdb236.p.rapidapi.com/api/imdb/top250-movies"
url_pelicula = f"https://imdb236.p.rapidapi.com/api/imdb/"
headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": rapidapi_host
    }

def obtener_datos_peliculas():
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        peliculas = response.json()
        if peliculas:
            print("Top 250 películas de IMDB:")
            # Abrir archivo una sola vez y escribir todos los datos
            with open("peliculas_imdb.csv", mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                # Escribir cabecera
                writer.writerow(["originalTitle", "startYear", "genres", "director", "runtimeMinutes", "averageRating", "numVotes"])
                # Escribir datos
                for pelicula in peliculas:
                    id_pelicula = pelicula.get("id", "")

                    response_detalle = requests.get(url_pelicula + id_pelicula, headers=headers)
                    if response_detalle.status_code == 200:
                        pelicula_detalle = response_detalle.json()
                        if pelicula_detalle:
                            titulo = pelicula_detalle.get("originalTitle", "")
                            anyo = pelicula_detalle.get("startYear", "")
                            genero_principal = pelicula_detalle.get("genres", [""])[0]
                            directors = pelicula_detalle.get("directors", [])
                            director_principal = directors[0].get("fullName", "") if directors else ""
                            duracion = pelicula_detalle.get("runtimeMinutes", "")
                            rating = pelicula_detalle.get("averageRating", "")
                            num_votos = pelicula_detalle.get("numVotes", "")
                            writer.writerow([titulo, anyo, genero_principal, director_principal, duracion, rating, num_votos])
                        else:
                            print(f"No se encontraron datos para la película en {url_pelicula}.")
                    else:
                        print(f"Error al obtener los datos de la película: {response_detalle.status_code}")
        else:
            print("No se encontraron datos.")
    else:
        print(f"Error al obtener los datos: {response.status_code}")


if __name__ == "__main__":
    obtener_datos_peliculas()