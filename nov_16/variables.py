nombre = "Pepe"
edad = 68
sueldo = 2300.50
jubilado = False
print("Nombre:", nombre, "Edad:", edad, "Jubilado:", jubilado, "Sueldo:", sueldo)
a,b=10,5
suma = a + b
print("La suma de", a, "y", b, "es", suma)
a=b=c=10
print("Valor de a:", a, "Valor de b:", b, "Valor de c:", c)
print(a,b,c, sep=", ")
print('''Línea 1
Línea 2
Línea 3
Linea 4''')
print("Linea 1\nLínea 2\nLínea 3\nLínea 4")
print(f"Nombre: {nombre}, Edad: {edad}, Jubilado: {jubilado}, Sueldo: {sueldo}")
nombre = "Fran"
Apellido = "García"
print(f"Nombre completo: {nombre} {Apellido}") # Interpolación de variables, f-string
print("Nombre completo: {} {}".format(nombre, Apellido)) # Método format, Fran García
print("Nombre completo: {1} {0}".format(nombre, Apellido)) # Método format con índices, García Fran
print("Nombre completo: {n} {a}".format(n=nombre, a=Apellido)) # Método format con nombres, Fran García
print("Sueldo con dos decimales: {:.2f}".format(sueldo)) # Sueldo con dos decimales: 2300.50
nombre = "Francisco"
edad = 45
print((f"{nombre:>10s}{edad:>5d}"))  # Alineación a la derecha
a=None # Variable sin valor asignado
print("Valor de a:", a)  # Valor de a: None
print(type(nombre))  # <class 'str'>
print(type(a))    # <class 'NoneType'>

# Operaciones con variables
x = 10
y = 3
suma = x + y
resta = x - y
producto = x * y
division = x / y
division_entera = x // y
potencia = x ** y
modulo = x % y
print("Suma:", suma)  # Suma: 13
print("Resta:", resta)  # Resta: 7
print("Producto:", producto)  # Producto: 30
print("División:", division)  # División: 3.3333333333333335
print("División entera:", division_entera)  # División entera: 3
print("Potencia:", potencia)  # Potencia: 1000
print("Módulo:", modulo)  # Módulo/Resto: 1

# Precedencia de operadores y conversiones de tipo
print((4+5)*2)  # 18
print(4+5*2)    # 14
#print('4'+5) # TypeError: can only concatenate str (not "int") to str
print('4'+str(5))  # 45
print(int('4')+5)  # 9
print(float('4.5')+5)  # 9.5
print('4'*5)  # 44444
print(bool(0))  # False
print(bool(1))  # True
print(bool(-3))  # True, cualquier número distinto de 0 es True
