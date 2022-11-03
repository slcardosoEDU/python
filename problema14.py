"""14. Realiza un programa que convierta un número decimal en su representación binaria. Hay que
tener en cuenta que desconocemos cuántas cifras tiene el número que introduce el
usuario"""
from mi_libreria import leer_entero

decimal = leer_entero("Introduzaca número decimal: ")

binario = ""
while decimal != 1:
    binario = str(decimal % 2) + binario
    decimal = decimal // 2
binario = "1" + binario
print(binario)