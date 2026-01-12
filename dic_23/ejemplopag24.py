lista = ["gato", "ciervo", "mesa", "circo"]
vocales = 0
for palabra in lista:
    for l in palabra:
        if l in ["a", "e", "i", "o", "u"]:
            vocales += 1
print(f"Total vocales: {vocales}")