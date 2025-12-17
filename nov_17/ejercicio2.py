#pedir al usuario que ingrese un numero de tres cifras y ver si la primera cifra es par con true o false
numero = int(input("Ingrese un número de tres cifras: "))
cifra1 = numero // 100 # obtener la primera cifra
print(cifra1 % 2 == 0) # verificar si la primera cifra es par y mostrar el resultado