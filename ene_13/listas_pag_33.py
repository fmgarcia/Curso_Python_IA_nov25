'''
●Crea una lista con nombres de alumnos
●Después crea otra lista con las mismas posiciones. Cada posición contendrá a su vez otra lista con al menos 4 notas
–Cada posición de esta lista se corresponde con la misma posición en la lista de alumnos
●Muestra el nombre de cada alumno con su nota media al lado
'''

import random

def alumnos_notas_pablo():
    alumnos = ["Ana", "Luis", "María", "Carlos", "Sofía"]
    notas =[
        [7, 8, 9, 7],
        [6, 7, 8, 9],
        [8, 9, 7, 8],
        [9, 7, 8, 6],
        [7, 8, 9, 8], 
    ]
    for alumno, nota in zip(alumnos, notas):
        media = sum(nota) / len(nota)
        print(f"{alumno}: {media:.2f}")
        
def alumnos_notas_fran():
    alumnos = ["Ana", "Luis", "María", "Carlos", "Sofía"] # Lista de alumnos
    notas = [[random.randint(0, 10) for _ in range(4)] for _ in range(len(alumnos))] # Lista de listas de notas aleatorias
    medias = [sum(grupo_notas) / len(grupo_notas) for grupo_notas in notas] # Lista de medias
    resultado_texto = [f"{alumno}: {media:.2f}" for alumno, media in zip(alumnos, medias)] # Lista de cadenas con el resultado
    print('\n'.join(resultado_texto)) # Imprime el resultado

if __name__ == "__main__":
    alumnos_notas_pablo()
    alumnos_notas_fran()