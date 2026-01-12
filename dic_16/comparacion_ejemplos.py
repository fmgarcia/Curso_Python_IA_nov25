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

# Comparaciones de identidad
a = [1,2,3]
b = a
c = [1,2,3]
print(a == c) # True (Python puede comparar listas con ==)
print(a is c) # False (objetos diferentes)
print(a is b) # True (apuntan al mismo objeto)

# Comparaciones de pertenencia
print('ca' in 'casa')  # True
print(3 in [1,2,3,4,5])  # True (valor en una lista)
print([1,2] in [1,2,3,4])  # False (lista dentro de otra lista)
print(3 not in [1,2,3,4,5])  # False (valor en una lista)
print([1,2] in [[1,2],[3,4]])  # True (lista dentro de otra lista)

# Comparaciones encadenadas
n = 5
print(0 < n < 10)  # True (n está entre 0 y 10)
print(0 < n and n < 10)  # True (n está entre 0 y 10, versión larga)

# operadores lógicos con comparaciones
edad = 25
activo = True
pase_de_oro = False
print(18 <= edad <= 65)  # True (edad entre 18 y 65)
print(edad >= 18 and edad <= 65)  # True (edad entre 18 y 65, versión larga). And es True si ambos son True
print(edad < 18 or edad > 65)  # False (edad no es menor de 18 ni mayor de 65). Or es True si alguno es True
print(18 <= edad <= 65 and activo)  # True (edad entre 18 y 65 y activo)
print((18 <= edad <= 65 and activo) or pase_de_oro)  # True (cumple la primera condición)
print(not activo)  # False (negación de activo)


# num = int(input("Número entre 1 y 100 que sea par: "))
# ok = num > 0 and num <= 100 and num % 2 == 0
# print(f"¿El número es válido?: { ok }")

num = int(input("Número entre 1 y 100 que sea par: "))
print(f"¿El número es válido?: {'El número es válido' if num > 0 and num <= 100 and num % 2 == 0 else 'El número no es válido' }")