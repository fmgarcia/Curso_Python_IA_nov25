'''
Crea una lista con 4 valores y realiza lo siguiente:
    – Agrega 2 elementos al principio.
    – Agrega 2 más al final.
    – Elimina las posiciones 3, 4 y 5.
    – Inserta 1 elemento antes del último elemento.
    – En cada cambio, muestra la lista resultante con sus elementos separados por ' => ' (no uses ningún bucle).
● Realiza una versión del ejercicio con métodos y otra usando las técnicas para extraer sublistas y concatenar listas
'''

def metodos():
    lista = [10, 20, 30, 40]
    print("Lista inicial:", ' => '.join(map(str, lista)))

    # Agrega 2 elementos al principio.
    lista.insert(0, 2)
    lista.insert(0, 1)
    print("Después de agregar 2 al principio:", ' => '.join(map(str, lista)))

    # Agrega 2 más al final.
    lista.append(50)
    lista.append(60)
    print("Después de agregar 2 al final:", ' => '.join(map(str, lista)))
    # La lista tiene los siguientes elementos ahora: [1, 2, 10, 20, 30, 40, 50, 60]
    # Los índices son:                                0  1   2   3   4   5   6   7

    # Elimina las posiciones 3, 4 y 5.
    del lista[3:6] # lista.pop(5), lista.pop(4), lista.pop(3)
    print("Después de eliminar posiciones 3, 4 y 5:", ' => '.join(map(str, lista))) # [1, 2, 10, 50, 60]

    # Inserta 1 elemento antes del último elemento.
    lista.insert(-1, 35)
    print("Después de insertar antes del último elemento:", ' => '.join(map(str, lista))) # [1, 2, 10, 50, 35, 60]

def slicing():
    lista = [10, 20, 30, 40]
    print("Lista inicial:", ' => '.join(map(str, lista)))

    # Agrega 2 elementos al principio.
    lista = [1, 2] + lista
    print("Después de agregar 2 al principio:", ' => '.join(map(str, lista)))

    # Agrega 2 más al final.
    lista = lista + [50, 60]
    print("Después de agregar 2 al final:", ' => '.join(map(str, lista)))
    # La lista tiene los siguientes elementos ahora: [1, 2, 10, 20, 30, 40, 50, 60]
    # Los índices son:                                0  1   2   3   4   5   6   7

    # Elimina las posiciones 3, 4 y 5.
    lista = lista[:3] + lista[6:]
    print("Después de eliminar posiciones 3, 4 y 5:", ' => '.join(map(str, lista))) # [1, 2, 10, 50, 60]

    # Inserta 1 elemento antes del último elemento.
    lista = lista[:-1] + [35] + lista[-1:]
    print("Después de insertar antes del último elemento:", ' => '.join(map(str, lista))) # [1, 2, 10, 50, 35, 60]

if __name__ == "__main__":
    metodos() # Es más eficiente usar métodos para modificar listas. Usar en listas gigantes ya que trabajas sobre el mismo objeto siempre. Cuidado al borrar porque los índices se mueven.
    slicing() # Es más legible usar slicing y concatenación para modificar listas. Usar en listas pequeñas ya que se crean nuevos objetos en cada operación.