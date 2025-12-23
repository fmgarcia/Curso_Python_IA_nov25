final=False
almacen=0
while(not final):
    valor = float(input("introduce un numero: "))
    almacen += valor
    termina = input("¿quieres mas numeros? ").lower()
    if (termina == "no"):
        final=True
print(f"la suma de los numeros es {almacen}")