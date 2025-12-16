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