palabra = input("Introduce una palabra: ").lower() # Convertir a minúsculas
tiene_vocal = ('a' in palabra) or ('e' in palabra) or ('i' in palabra) or ('o' in palabra) or ('u' in palabra) # Verificar si tiene al menos una vocal
print(f"¿La palabra tiene al menos una vocal?: { tiene_vocal }") # Mostrar el resultado