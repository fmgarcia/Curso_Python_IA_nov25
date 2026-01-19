suma = lambda n1, n2: n1 + n2

def resta (n1, n2):
    return n1 - n2

def operar(f, n1, n2):
    return f(n1, n2) # Llamamos a la función recibida

print(operar(suma, 6, 4)) # 10
print(operar(resta, 6, 4)) # 2
print(operar(lambda n1, n2: n1 * n2, 6, 4)) # 24

# Calculadora simple
# valor1 = 20
# valor2 = 10
# operando = input("Introduzca la operación (+, -, *, /, **): ")
# print(valor1, operando, valor2, "=", operar(lambda valor1, valor2: eval(f"{valor1} {operando} {valor2}"), valor1, valor2))

# Calculadora con input del usuario
# print(eval(f"{input('Introduce la operación a realizar (por ejemplo: 5 + 3):')}"))


valor1 = 20
valor2 = 0
operaciones_permitidas = ['+', '-', '*', '/', '**']
while True:
    operando = input("Introduzca la operación (+, -, *, /, **) o 'salir' para terminar: ")
    if operando.lower() == 'salir':
        print("Saliendo de la calculadora.")
        break
    if operando not in operaciones_permitidas:
        print("Operación no válida. Intente de nuevo.")
        continue
    try:
        resultado = operar(lambda valor1, valor2: eval(f"{valor1} {operando} {valor2}"), valor1, valor2)
        print(f"{valor1} {operando} {valor2} = {resultado}")
    except Exception as e:
        print(f"Error al realizar la operación: {e}")
