def saludar(nombre):
    print(f"Hola {nombre}!")

def despedir():
    print("Adiós curso!")
    
def saludar_y_despedir():
    saludar("curso")
    despedir()
    
def suma(x, y): # Variables locales a la función
    z = 10
    resultado = x + y + z
    print(f"{x} + {y} + {z} = {resultado}")

x2 = 10  # Variable global
y2 = 20

def suma2():
    resultado = x2 + y2
    print(f"{x2} + {y2} = {resultado}")
    
def devolver_suma(x,y):
    return x + y

def imprimir_suma(x,y):
    try:
        print(f"La suma de {x} + {y} = {devolver_suma(x,y)}")
        return True
    except TypeError:
        return False

def dividir(a,b):
    try:
        resultado = a / b
        print(f"{a} dividido entre {b} es {resultado}")
    except ZeroDivisionError:
        print("Error: División por cero no permitida.")
    except TypeError:
        print("Error: Tipos de datos no válidos para la división.")
        
def valores_defecto(a, b=2):
    return a + b

def valores_defecto_3(a=1, b=2, c=3):
    return a + b + c


saludar_y_despedir()
saludar("Fran")
# print(nombre) # NameError: name 'nombre' is not defined
suma(5, 7)
# print(x)  # NameError: name 'x' is not defined
suma2()
print(f"x2 fuera de la función: {x2}")
print(f"y2 fuera de la función: {y2}")
if imprimir_suma(7,"hola"):
    print("Suma realizada correctamente")
else:
    print("Error al realizar la suma")
print(devolver_suma(3,4)) # 7
dividir(10,2) # 5.0
dividir(10,0) # Error: División por cero no permitida.
dividir(10,"hola") # Error: Tipos de datos no válidos para la división.
dividir(b=2,a=10) # 5.0
print(valores_defecto(5)) # 7
print(valores_defecto(5, 3)) # 8
print(valores_defecto_3()) # 6
print(valores_defecto_3(10)) # 15
print(valores_defecto_3(10,20)) # 33
print(valores_defecto_3(10,20,30)) # 60