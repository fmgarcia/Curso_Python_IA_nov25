def modificar3numeros(a,b,c):
    a += 10
    b += 20
    c += 30
    return a, b, c

def modificar_lista(lista):
    for i in range(len(lista)):
        lista[i] += 10


a = 1
b = 2
c = 3
print(f"Antes de modificar3numeros: a={a}, b={b}, c={c}")
a, b, c = modificar3numeros(a,b,c)
print(f"Después de modificar3numeros: a={a}, b={b}, c={c}")
lista = [1,2,3]
print(f"Antes de modificar_lista: lista={lista}")
modificar_lista(lista)
print(f"Después de modificar_lista: lista={lista}")