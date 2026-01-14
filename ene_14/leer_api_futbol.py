import requests
import json

api_key = "6bff5b66e01940a4a4730dad785bbab3"
url = f"http://api.football-data.org/v4/competitions/PD/standings?season=2023"


def obtener_clasificacion():
    headers = {"X-Auth-Token": api_key, "User-Agent": "PostmanRuntime/7.51.0"}
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
                print(f"{position['position']}. {team_name} - Puntos: {points}, Partidos jugados: {played_games}")
        else:
            print("No se encontraron datos de clasificación.")
    else:
        print(f"Error al obtener los datos: {response.status_code}")


if __name__ == "__main__":
    obtener_clasificacion()