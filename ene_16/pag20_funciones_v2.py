'''
● Crea una función con 2 parámetros. El primero será una cadena y representa
al nombre de una persona, mientras que el segundo agrupará el resto de
parámetros recibidos, que serán cadenas con los trabajos que la persona ha
realizado.
●Imprime por consola el nombre de la persona seguido de la lista de trabajos
realizados por la misma. Si no hay ningún trabajo, indica que no ha trabajado
nunca. Prueba la función varias veces, al menos una de ellas no le pases
ningún trabajo.
●Ejemplo de llamada:
–muestra_info("Pepe", "Capataz", "Equilibrista", "Cobrador del frac")
'''

def info_persona(nombre, *trabajos):
    if len(trabajos)>0: # Si la tupla no está vacía. Hago tratamiento de prurales
        print(f"Los trabajos realizados por {nombre} son: {', '.join(trabajos)}" if len(trabajos)>1 else f"El trabajo realizado por {nombre} es: {trabajos[0]}")
    else:
        print(f"{nombre} no ha trabajado nunca.")

if __name__ == "__main__":
    info_persona("Ana", "Ingeniera", "Arquitecta", "Diseñadora")
    info_persona("Luis", "Profesor")
    info_persona("Marta")