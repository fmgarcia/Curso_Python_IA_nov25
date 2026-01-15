import time
import requests
import json
import csv
import os

x_rapidapi_key = "b94737c6e3msh63499126071ca4ep11324cjsn4e2da04e268f"
x_rapidapi_host = "imdb236.p.rapidapi.com"

url_base = "https://imdb236.p.rapidapi.com"
endpoint_id_base = "/api/imdb/"
ruta_fichero = './ficheros/imdb.csv'
peticiones_api = 5  # Número máximo de peticiones API permitidas por hora
tiempo_entre_peticiones = 5  # segundos
valor_inicial_id = 1000000
headers = {"x-rapidapi-key": x_rapidapi_key, "x-rapidapi-host": x_rapidapi_host, "User-Agent": "PostmanRuntime/7.51.0"}

# CONFIGURACIÓN DE DUPLICADOS
REEMPLAZAR_EXISTENTES = True  # True: actualiza la línea / False: mantiene la vieja y descarta la nueva

# --- 1. Función Auxiliar Mejorada ---
def obtener_valor_profundo(dato, ruta_claves):
    """
    Navega por el JSON. 
    Si encuentra una lista y la siguiente clave es un string, concatena los valores.
    """
    valor_actual = dato
    
    for i, clave in enumerate(ruta_claves):
        if isinstance(valor_actual, list):
            # Si queremos un campo específico de TODOS los elementos de la lista
            if isinstance(clave, str):
                resultados = []
                for item in valor_actual:
                    res = obtener_valor_profundo(item, [clave] + ruta_claves[i+1:])
                    if res is not None: resultados.append(str(res))
                return ", ".join(resultados) if resultados else None
            
            # Si queremos un índice específico
            elif isinstance(clave, int) and 0 <= clave < len(valor_actual):
                valor_actual = valor_actual[clave]
            else:
                return None
        
        elif isinstance(valor_actual, dict):
            valor_actual = valor_actual.get(clave)
        else:
            return None
            
        if valor_actual is None:
            return None
            
    # Si el resultado final es una lista de strings (como ['Drama']), lo unimos
    if isinstance(valor_actual, list) and all(isinstance(x, str) for x in valor_actual):
        return ", ".join(valor_actual)
        
    return valor_actual

# --- 2. Gestión de CSV (Evitar duplicados) ---
def guardar_en_csv(nueva_fila, columnas, ruta_csv):
    """Guarda o actualiza una fila basándose en la primera columna (ID)."""
    os.makedirs(os.path.dirname(ruta_csv), exist_ok=True)
    datos_actuales = {}
    id_nuevo = str(nueva_fila[0])

    # 1. Leer datos existentes
    if os.path.exists(ruta_csv):
        with open(ruta_csv, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                datos_actuales[str(row[columnas[0]])] = list(row.values())

    # 2. Lógica de inserción/reemplazo
    if id_nuevo in datos_actuales:
        if REEMPLAZAR_EXISTENTES:
            datos_actuales[id_nuevo] = nueva_fila
            print(f"ID {id_nuevo} actualizado.")
        else:
            print(f"ID {id_nuevo} ya existe. Saltando...")
            return
    else:
        datos_actuales[id_nuevo] = nueva_fila
        print(f"ID {id_nuevo} insertado como nuevo.")

    # 3. Escribir todo el archivo de nuevo
    with open(ruta_csv, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(columnas)
        for fila in datos_actuales.values():
            writer.writerow(fila)

# --- 3. Función Genérica Principal ---
def procesar_api_generica(url, headers, config_extraccion, ruta_csv, tiempo_espera=1.00):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            
            # Normalizar a lista
            res_busqueda = obtener_valor_profundo(data, config_extraccion['ruta_items'])
            if isinstance(res_busqueda, dict): items = [res_busqueda]
            elif isinstance(res_busqueda, list): items = res_busqueda
            else: items = [data] if not config_extraccion['ruta_items'] else []

            if items:
                columnas = list(config_extraccion['mapeo_campos'].keys())
                for item in items:
                    fila = [obtener_valor_profundo(item, ruta) for ruta in config_extraccion['mapeo_campos'].values()]
                    guardar_en_csv(fila, columnas, ruta_csv)
            
            time.sleep(tiempo_espera)
        else:
            print(f"Error {response.status_code} en {url}")
    except Exception as e:
        print(f"Error en petición: {e}")

if __name__ == "__main__":
    # --- EJEMPLO 1: Football-data.org ---
    # Supongamos que esta es la estructura que mostraste antes
    config_futbol = {
        # Para llegar a la lista de equipos: data['standings'][0]['table']
        "ruta_items": ["standings", 0, "table"], 
        
        # Diccionario: Nombre Columna CSV -> Ruta dentro del item
        "mapeo_campos": {
            "Posición": ["position"],
            "Equipo": ["team", "name"], # Anidado
            "Puntos": ["points"],
            "Ganados": ["won"],
            "Goles a Favor": ["goalsFor"],
            # Puedes añadir claves estáticas o derivadas si modificas ligeramente la función,
            # pero por ahora extraemos puramente del JSON.
        }
    }
    # url_futbol = "https://api-football.../standings?league=140&season=2020"
    # procesar_api_generica(url_futbol, headers, config_futbol, "./ficheros/futbol.csv")
    
# --- EJEMPLO 2: IMDB (ADAPTADO) ---
    
    headers_imdb = {
        "x-rapidapi-key": x_rapidapi_key, 
        "x-rapidapi-host": x_rapidapi_host
    }

   
    # Configuración para IMDB
    config_imdb = {
    "ruta_items": [],  # El JSON de IMDB es el objeto en sí, no hay que navegar a una lista
    "mapeo_campos": {
        "ID": ["id"],
        "Titulo": ["primaryTitle"],
        "Tipo": ["type"],
        "Año Inicio": ["startYear"],
        "Rating": ["averageRating"],
        "Votos": ["numVotes"],
        "Generos": ["genres"],            # Extrae la lista de strings: "Drama, Crimen"
        "Directores": ["directors", "fullName"], # Extrae fullName de TODOS los directores
        "Actores": ["cast", "fullName"],         # Extrae fullName de TODOS los actores
        "Minutos": ["runtimeMinutes"]
         }
    }

    # Tu bucle original usando la nueva función
    for i in range(peticiones_api):
        current_id = f"tt{valor_inicial_id + i}"
        url_completa = f"https://imdb236.p.rapidapi.com/api/imdb/{current_id}"
        
        print(f"[{i+1}/{peticiones_api}] Consultando {current_id}...")
        procesar_api_generica(url_completa, headers_imdb, config_imdb, ruta_fichero, tiempo_espera=tiempo_entre_peticiones)
print("Proceso completado.")