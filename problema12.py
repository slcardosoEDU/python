"""12. Escribe un programa que dado un número entero introducido por el usuario lo descomponga en
factores primos. """


#Leemos el número a descomponer.
from mi_libreria import leer_entero
numero = leer_entero("Introduzca número: ")

#Descomponemos en factores primos
i = 2
veces = 0
while i <= numero:

    while numero % i == 0:
        veces += 1
        numero = int(numero / i)
    
    if veces != 0:
        print(i,"^",veces)
    i += 1
    veces = 0

