try:
    numero = int(input("Introduce un número entero: "))
    print(f"El numero * 2 es: {numero * 2}  y el numero al cuadrado es: {numero ** 2} y la división de 10 entre el número es: {10 / numero}")
except Exception as e:
    print(f"Se ha producido un error: {e}")
print("Programa finalizado.")