#Decir si un numero es primo o no
from mi_libreria import leer_entero
numero = leer_entero("Introduzca número: ")

aux = 2
while aux < numero:
    if numero % aux == 0:
        break
    aux += 1

if aux == numero:
    print("Es primo")
else:
    print("No es primo")
