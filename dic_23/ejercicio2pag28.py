# Opción 1: Pirámide de asteriscos centrada recorriendo todas las columnas
# altura = int(input("Introduce la altura del triangulo: "))
# for i in range(altura):
#     for j in range(altura * 2 - 1):
#         if altura - 1 - i <= j <= altura - 1 + i:
#             print("*", end="")  
#         else:
#             print("-", end="")
#     print()
# Opción 2: Pirámide de asteriscos centrada recorriendo solo las columnas necesarias
altura = int(input("Introduce la altura del triangulo: "))
for i in range(altura):
    for j in range(altura + i):
        if altura - 1 - i <= j:
            print("*", end="")  
        else:
            print("-", end="")
    print()
