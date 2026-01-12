# Opción 1: Pirámide de asteriscos de subida (con dos for dentro del for principal)
size = 6
for i in range(1, size + 1):
    for j in range(size - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()
# Opción 2: Pirámide de asteriscos de subida (con un solo for dentro del for principal)
size = 6
for i in range(size):
    for j in range(size):
        if j < size - 1 - i: # La parte superior de la diagonal
            print(" ", end="")
        else:
            print("*", end="")
    print()