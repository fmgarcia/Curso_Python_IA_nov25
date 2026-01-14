import time
import requests
import json
import csv

api_key = "6bff5b66e01940a4a4730dad785bbab3"
ruta_fichero = './ficheros/clasificacion_liga.csv'


def obtener_clasificacion(url):
    headers = {"X-Auth-Token": api_key}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        standings = data.get("standings", [])
        if standings:
            table = standings[0].get("table", [])
            print("Clasificación de La Liga:")
            for position in table:
                team_name = position["team"]["name"]
                points = position["points"]
                played_games = position["playedGames"]
                won = position["won"]
                drawn = position["draw"]
                lost = position["lost"]
                goals_for = position["goalsFor"]
                goals_against = position["goalsAgainst"]
                goal_difference = position["goalDifference"]
                # Guardar datos en csv
                with open(ruta_fichero, mode="a", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerow([url[-4:], position['position'], team_name, points, played_games, won, drawn, lost, goals_for, goals_against, goal_difference])
            time.sleep(6)  # Pausa para evitar saturar la API
        else:
            print("No se encontraron datos de clasificación.")
    else:
        print(f"Error al obtener los datos: {response.status_code}")


if __name__ == "__main__":
    for anyo in range(2015, 2026):   
        url = f"http://api.football-data.org/v4/competitions/PD/standings?season={anyo}"
        obtener_clasificacion(url)