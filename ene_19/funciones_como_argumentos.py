suma = lambda n1, n2: n1 + n2

def resta (n1, n2):
    return n1 - n2

def operar(f, n1, n2):
    return f(n1, n2) # Llamamos a la función recibida

print(operar(suma, 6, 4)) # 10
print(operar(resta, 6, 4)) # 2
print(operar(lambda n1, n2: n1 * n2, 6, 4)) # 24