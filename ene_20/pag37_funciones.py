'''
Crea una lista de diccionarios. Cada diccionario tendrá los datos de un
producto: nombre, precio, stock (entero) y favorito (booleano)
●Imprime la lista de los nombres de los productos favoritos. Utiliza filter y map.
Resuélvelo después con listas por comprensión.
●Imprime el valor total de todos los productos (suma de precio*stock). Utiliza la
función reduce.
'''
from functools import reduce

productos = [
    {"nombre": "Producto1", "precio": 10.5, "stock": 5, "favorito": True},
    {"nombre": "Producto2", "precio": 20.0, "stock": 3, "favorito": False},
    {"nombre": "Producto3", "precio": 15.0, "stock": 10, "favorito": True},
    {"nombre": "Producto4", "precio": 5.0, "stock": 20, "favorito": False},
]

favoritos = list(
                map(lambda p: p["nombre"], 
                    filter(lambda p: p["favorito"], productos)))
print("Productos favoritos (programación funcional): ", favoritos)  # ['Producto1', 'Producto3']

favoritos = [p["nombre"] for p in productos if p["favorito"]]
print("Productos favoritos (compresión): ", favoritos)  # ['Producto1', 'Producto3']  

valor_total = reduce(lambda total, p: total + p["precio"] * p["stock"], productos, 0)  
print("Valor total de todos los productos (programación funcional): ", valor_total)  #  0 + 10.5*5 + 20.0*3 + 15.0*10 + 5.0*20 = 52.5 + 60 + 150 + 100 = 362.5

valor_total = sum(p["precio"] * p["stock"] for p in productos)
print("Valor total de todos los productos (compresión): ", valor_total)  # 362.5

# calculo de valor_total con programación estructurada
valor_total = 0
for p in productos:
    valor_total += p["precio"] * p["stock"]
print("Valor total de todos los productos (programación estructurada): ", valor_total)  # 362.5