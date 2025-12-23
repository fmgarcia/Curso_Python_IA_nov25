# Opción A
for i in range(9, 0, -1):
    for j in range(i):
        print(f"{j + 1}", end="")
    print()
# Opción B
for i in range(1, 10):
    for j in range(1, 11 - i):
        print(f"{j}", end="")
    print()
# Opción C
for i in range (9):
    for j in range (1, 10 - i):
        print(j, end="")
    print() # Salto de línea al final de la