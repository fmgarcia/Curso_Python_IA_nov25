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

def mezcla(obligatorio1,obligatorio2, opcional1=10, opcional2=20):
    return obligatorio1 + obligatorio2 + opcional1 + opcional2

def info_persona(nombre, *aficiones):
    if aficiones: # Si la tupla no está vacía
        print(f"La primera afición de {nombre} es: {aficiones[0]}")
    print(f"Las aficiones de {nombre} son: {', '.join(aficiones)}")
    
# Empaquetado de parámetros nominales
def info_persona_nominal(nombre, **datos):
    print(
    f"""{nombre}:
    DNI = {datos['dni']}
    correo = {datos['correo']}
    edad = {datos['edad']}"""
    )
    
    
def info_persona_nominal2(nombre, diccionario):
    print(
    f"""{nombre}:
    DNI = {diccionario['dni']}
    correo = {diccionario['correo']}
    edad = {diccionario['edad']}"""
    )
    
def info_persona_nominal3(nombre, **datos):
    for k, v in datos.items():
        print(f"{k} = {v}")
    
# Caso extraño
def f(a1, *args, n1, **kwargs):
    print(a1, args, n1, kwargs)
    
def suma_resta(x, y, *, resta=False):
    return x - y if resta else x + y

def suma_resta2(x, y,/, *, resta=False):
    return x - y if resta else x + y

def suma_desempaquetada(a,b,c):
    print(a+b+c)


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
print(mezcla(1,2,opcional2=3)) # 16

# Empaquetado de parámetros
info_persona("Ana", "leer", "viajar", "cine") # Las aficiones de Ana son: leer, viajar, cine
info_persona("Luis") # Las aficiones de Luis son:
info_persona("Marta", *["deporte", "música"]) # Las aficiones de Marta son: deporte, música

# Desempaquetado de parámetros nominales
info_persona_nominal("Pedro", edad= 43, dni="23454365G", correo="pedro@gmail.com")
diccionario = {"edad": 43, "dni": "23454365G", "correo": "pedro@gmail.com"}
info_persona_nominal2("Pedro", diccionario)
info_persona_nominal3("Laura", dni="12345678A", correo="laura@gmail.com")
f(1, 2, 3, n1=4, a=5, b=6)
print(suma_resta(4, 7)) # 11
print(suma_resta(y=6, x=10)) # 16 (Pueden ser de ambos tipos)
print(suma_resta(8, 3, resta=True)) # 5
#print(suma_resta(4, 7, True)) # TypeError: suma_resta() takes 2 positional arguments but 3 were given

# Uso de / y *
print(suma_resta2(4, 7)) # 11
print(suma_resta2(8, 3, resta=True)) # 5
#print(suma_resta2(y=6, x=10)) # TypeError: suma_resta() got some positional-only arguments passed as keyword arguments: 'x, y'

# Desempaquetado de listas/tuplas
tupla = (1,2,3)
suma_desempaquetada(*tupla) # 6