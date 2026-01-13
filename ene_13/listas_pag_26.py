'''
1)A partir de una lista de palabras, generar una nueva lista con las palabras que
contengan la letra ‘a’ en mayúsculas
2)A partir de una lista de fechas en formato dd/mm/aaaa. Generar una lista con
las fechas cuyo año sea igual o posterior a 2015
3)Pide al usuario 10 números con decimales (double). Usa un array para
almacenarlos. Muestra la media y los números que están por encima de esa
media.
'''
def palabras_con_a_mayuscula():
    palabras = ["Hola", "Mundo", "Python", "Aprendiendo", "Programación"]
    palabras_con_A = [e for e in palabras if 'A' in e]
    print(palabras_con_A)
    
def fechas_posteriores_2015():
    fechas = ["12/05/2010", "23/11/2016", "01/01/2015", "15/08/2020", "30/09/2014"]
    fechas_validas = [fecha for fecha in fechas if int(fecha.split('/')[-1]) >= 2015]
    print(fechas_validas)
    fechas_validas_2 = [fecha for fecha in fechas if fecha[-4:] >= '2015']
    print(fechas_validas_2)
    fechas_validas_3 = [fecha for fecha in fechas if fecha[6:] >= '2015']
    print(fechas_validas_3)
    fechas_validas_4 = [fecha for fecha in fechas if int(fecha.split('/')[2]) >= 2015]
    print(fechas_validas_4)
    fechas_validas_5 = [fecha for fecha in fechas if int(fecha[-4:]) >= 2015]
    print(fechas_validas_5)
    
def numeros_decimales():
    #numeros = input("Ingrese 10 números decimales separados por ,: ")
    #numeros = [float(n) for n in numeros.split(',')]
    numeros = [3.5, 7.2, 1.8, 4.4, 9.0, 2.3, 6.6, 8.1, 5.5, 0.9]
    media = sum(numeros) / len(numeros)
    print("La media es: ", media)
    print("Números mayores que la media: ", [n for n in numeros if n > media])

if __name__ == "__main__":
    palabras_con_a_mayuscula()
    fechas_posteriores_2015()
    numeros_decimales()