'''
●Escribir un programa que implemente una agenda (diccionario). En la agenda se
podrán guardar nombres (claves) y números de teléfono (valores). El programa nos
dará el siguiente menú:
–1) Añadir: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe
mostrar el teléfono. Si el nombre no se encuentra, pide su número de teléfono y
añádelo.
–2) Buscar: Nos pide una cadena de caracteres, y nos mostrará todos los contactos
cuyos nombres comiencen por dicha cadena.
–3) Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la
agenda.
–4) Listar: Nos muestra todos los contactos de la agenda.
–0) Salir
●Repite el programa hasta que elija salir
El programa debe hacer uso de funciones para cada una de las opciones del menú.
'''
import os
import csv


ruta_fichero = "./ficheros/agenda.csv"
agenda = {} # Diccionario vacío para la agenda

def imprimir_menu():
    print("\n--- Menú de la Agenda ---")
    print("1) Añadir contacto")
    print("2) Buscar contacto")
    print("3) Borrar contacto")
    print("4) Listar contactos")
    print("0) Salir")
    opcion = input("Elige una opción: ")
    while not opcion.isdigit() or int(opcion) not in range(5):
        print("Opción no válida. Inténtalo de nuevo.")
        opcion = input("Elige una opción: ")
    return int(opcion)

def agregar_contacto(nombre, numero):
    if nombre in agenda:
        return False
    else:
        agenda[nombre] = numero
        return True
    
def buscar_cadena(cadena):
    return {nombre: numero for nombre, numero in agenda.items() if nombre.lower().startswith(cadena.lower())}

def borrar_contacto(nombre):
    if nombre in agenda:
        confirmacion = input(f"¿Estás seguro de que quieres borrar el contacto '{nombre}'? (s/n): ")
        if confirmacion.lower() == 's':
            del agenda[nombre]
            return True
        else:
            return False
    else:
        return False

def listar_contactos():
    if not agenda:
        print("La agenda está vacía.")
    else:
        print("\n--- Contactos en la Agenda ---")
        for nombre, numero in agenda.items():
            print(f"{nombre}: {numero}")
            
def cargar_agenda(ruta_csv):
    """Carga la agenda desde un archivo CSV si existe."""  
    agenda_cargada = {}
    if os.path.exists(ruta_csv):
        with open(ruta_csv, mode="r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 2:
                    nombre, numero = row
                    agenda_cargada[nombre] = numero
    return agenda_cargada
    
def guardar_agenda(ruta_csv, agenda):
    """Guarda la agenda en un archivo CSV."""
    with open(ruta_csv, mode="w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        for nombre, numero in agenda.items():
            writer.writerow([nombre, numero])

#----- Comienzo del programa -----
if __name__ == "__main__":
    
    agenda = cargar_agenda(ruta_fichero) # Cargar agenda existente  
    # Recorrer el menú
    salir = False
    while not salir:
                
        opcion = imprimir_menu() # Mostrar el menú
        
        match (opcion):
        
            case 1 :
                nombre = input("Introduce el nombre del contacto: ")
                numero = input("Introduce el número de teléfono: ")
                if agregar_contacto(nombre,numero):
                    print(f"Contacto '{nombre}' añadido con el número {numero}.")
                else:
                    print(f"El contacto '{nombre}' ya existe. Su número es: {agenda[nombre]}")
            case 2 :
                cadena = input("Introduce la cadena para buscar contactos: ")
                contactos = buscar_cadena(cadena)
                for nombre, numero in contactos.items():
                    print(f"{nombre}: {numero}")
            case 3 :
                nombre = input("Introduce el nombre del contacto a borrar: ")
                if borrar_contacto(nombre):
                    print(f"Contacto '{nombre}' borrado.")
                else:
                    print(f"El contacto '{nombre}' no existe o no se ha borrado.")
            case 4 :
                listar_contactos()
            case 0 :
                salir = True
                print("Saliendo de la agenda.")
            case _:
                pass
    guardar_agenda(ruta_fichero, agenda)
    print("Programa finalizado.")