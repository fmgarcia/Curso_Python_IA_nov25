# Ejemplos de uso de la estructura condicional if
# Ejemplo 1: Comprobar si has acertado un número
# numero = 2
# adivina = int(input("Adivina el número: "))
# if adivina == numero:
#     print("¡Has acertado!")
#     print("¡Eres un genio!")

# Ejemplo 2: Uso de la instrucción pass
# numero = 2
# adivina = int(input("Adivina el número: "))
# if adivina == numero:
#     pass # No hacemos nada si acierta
#Aquí podríamos poner código adicional si quisiéramos

# Ejemplo 3: Uso de if-else
# numero = 2
# adivina = int(input("Adivina el número: "))
# if adivina == numero:
#     print("¡Has acertado!")
# else:
#     print("¡Inténtalo de nuevo!")

# Ejercicio 1: Comprobar si un número es par y realizar una acción u otra
# num = int(input("Introduce un número: "))
# if num % 2 == 0: # Si el número es par
#     print(f"El resultado de la división es {num / 2}.")
# else:
#     print(f"El resultado de la multiplicación es {num * 2}.")

# Ejemplo 4: Uso de if-elif-else
# edad = int(input("Dime tu edad: "))
# if edad < 18:
#     edad = 40
#     print("Eres menor de edad")
# elif edad < 67:
#     print("Eres adulto")
# else:
#     print("Estás jubilado")
# print(f"Tu edad es {edad} años.")

# Ejemplo 5: Uso de múltiples elif sin else final
# edad = int(input("Dime tu edad: "))
# if edad < 18:
#     print("Eres menor de edad")
# elif edad < 67:
#     print("Eres adulto")
# elif edad < 100:
#     print("Estás anciano")
# print(f"Tu edad es {edad} años.")

# Ejercicio pág 25 documento 3.

# lado = float(input("Introduce el tamaño del lado del cuadrado: "))
# print("Elige una opción:")
# print("1)Perímetro del cuadrado")
# print("2)Área del cuadrado")
# opcion = int(input("Introduce tu opción: "))
# if opcion == 1:
#     print(f"El perímetro del cuadrado es: {lado * 4}")
# elif opcion == 2:
#     print(f"El área del cuadrado es: {lado * lado}")
# else:
#     print("Opción incorrecta")