numeros = input("Ingrese 5 numeros separados por ; : ")
lista_numeros = numeros.split(";")
suma = 0
for numero in lista_numeros:
    suma += int(numero)
print(f"La suma de los numeros es: {suma}")