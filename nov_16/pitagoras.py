# El teorema de Pitágoras establece que en un triángulo rectángulo,
# el cuadrado de la hipotenusa (el lado opuesto al ángulo recto) es igual
# a la suma de los cuadrados de los otros dos lados.

import math

a = float(input("Introduce la longitud del cateto a: "))
b = float(input("Introduce la longitud del cateto b: "))
c = (a**2 + b**2) ** 0.5
c2 = math.sqrt(a**2 + b**2)
print(f"La longitud de la hipotenusa c es: {c:.2f}")
print(f"La longitud de la hipotenusa c (usando math.sqrt) es: {c2:.2f}")