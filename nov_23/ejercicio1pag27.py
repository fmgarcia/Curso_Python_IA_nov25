lado = int(input("Lado del cuadrado: "))
creci=1
for alto in range(lado):
    for ancho in range(creci):
        print("*", end="")
    print()
    creci+=1