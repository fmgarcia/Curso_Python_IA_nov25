# edad = int(input("Dime tu edad: "))
# print(f"¿Eres menor de edad?: {edad < 18}")

# password = "hola"
# resp = input("Adivina la contraseña: ")
# print(f"¿Has acertado?: {password == resp}")

# password = "hola"
# resp = input("Adivina la contraseña: ")
# if resp == password:
#     print("¡Has acertado!")
# else:
#     print("Lo siento, contraseña incorrecta.")
    

# Ejemplo con operador ternario
# password = "hola"
# resp = input("Adivina la contraseña: ")
# print("¡Has acertado!") if resp == password else print("Lo siento, contraseña incorrecta.")

# Ejemplo simplificado
# print("¡Has acertado!") if input("Adivina la contraseña: ") == "hola" else print("Lo siento, contraseña incorrecta.")

a = [1,2,3]
b = a
c = [1,2,3]
print(a == c) # True (Python puede comparar listas con ==)
print(a is c) # False (objetos diferentes)
print(a is b) # True (apuntan al mismo objeto)
