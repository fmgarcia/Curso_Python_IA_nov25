# day = "Monday"

# Match the day to predefined patterns
# match day:
#     case "Saturday" | "Sunday":
#         print(f"{day} is a weekend.")  # Match weekends
#     case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
#         print(f"{day} is a weekday.")  # Match weekdays
#     case _:
#         print("That's not a valid day of the week.")  # Default case

# Monday is a weekday.

# Equivalent if-elif-else structure
# if day in ["Saturday", "Sunday"]:
#     print(f"{day} is a weekend.")
# elif day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
#     print(f"{day} is a weekday.")
# else:
#     print("That's not a valid day of the week.")

# Ejercicio Match-Case
# Ejercicio: operaciones básicas matemáticas
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
print("Elige una operación:"
        "\n1) Suma"
        "\n2) Resta"
        "\n3) Multiplicación"
        "\n4) División")
operacion = input("Introduce el número de la operación (1-4): ")
match operacion:
    case "1":
        resultado = num1 + num2
        print(f"La suma de {num1} y {num2} es: {resultado}")
    case "2":
        resultado = num1 - num2
        print(f"La resta de {num1} y {num2} es: {resultado}")
    case "3":
        resultado = num1 * num2
        print(f"La multiplicación de {num1} y {num2} es: {resultado}")
    case "4":
        if num2 != 0:
            resultado = num1 / num2
            print(f"La división de {num1} entre {num2} es: {resultado}")
        else:
            print("Error: No se puede dividir entre cero.")
    case _:
        print("Operación no válida. Por favor, elige una opción entre 1 y 4.")