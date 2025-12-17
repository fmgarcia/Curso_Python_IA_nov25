''' Comentario multi línea
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
print(f"Hola {nombre}, tienes {edad} años.")
'''
"""
Esto es otro comentario multi línea
y sirve para documentar el código.
"""
# print("Programa de bienvenida")  # Control + K + C para comentar varias líneas
# print("**********************")  # Control + K + U para descomentar varias líneas

# lado = float(input("Introduce el lado del cuadrado: "))
# area = lado ** 2
# print(f"El área del cuadrado es: {area}")

lado = input("Introduce el lado del cuadrado: ")
if lado.isdigit():
    lado = float(lado)
    area = lado ** 2
    print(f"El área del cuadrado es: {area}")
else:
    print("Error: Debes introducir un número válido para el lado del cuadrado.")