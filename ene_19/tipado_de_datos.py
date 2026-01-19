def veces(lista: tuple[str, ...], palabra: str) -> int:
    veces = 0
    for p in lista:
        if p == palabra:
            veces += 1
    return veces

palabras = ("casa", "coche", "moto", "casa", "árbol", "casa")
print(f"casa aparece {veces(palabras, 'casa')} veces") # casa aparece 3 veces

def suma(a: int, b: int, c: int) -> int:
    return a + b + c

print(suma(2, 3, 5)) # 10