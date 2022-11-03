#Decir si un numero es primo o no
esEntero = False
numero = -1
while not  esEntero:
    numero = input("Introduzca número: ")
    try:
        numero = int(numero)
        esEntero = True
    except ValueError:
        print("Eso no es un número.")

aux = 2
while aux < numero:
    if numero % aux == 0:
        break
    aux += 1

if aux == numero:
    print("Es primo")
else:
    print("No es primo")
