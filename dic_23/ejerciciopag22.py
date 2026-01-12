import random
n = random.randint(1, 10)
final = False
NUM_INTENTOS = 3
sw = 0
while (not final):
    intento = int(input(f"Adivina un número entre 1 y 10 (te quedan {NUM_INTENTOS - sw} intentos): "))
    if (intento == n):
        print(f"!Has adivinado el número¡ El número era: {n}")
        final = True
    else:        
        sw += 1
        if (sw == NUM_INTENTOS):
            print(f"No te quedan más intentos. El número era: {n}")
            final = True
        else:
            print("Número incorrecto. Inténtalo de nuevo.")