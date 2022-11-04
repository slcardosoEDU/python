"""Diseña una aplicación que dibuje el triángulo de Pascal, para n filas. Numerando las filas y elementos desde 0, 
la fórmula para obtener el m-ésimo elemento de la n-ésima fila es
E(n, m) = n!  /  m!(n - m)!
Donde n! es el factorial de n.
Un ejemplo de triángulo de Pascal con 5 filas (n = 4) es :
"""
from mi_libreria import *

def elemento_pascal(n,m):
    """Calcula el valor del elemento (n,m) del triángulo de Pascal.
    E(n, m) = n!  /  m!(n - m)!
    *n: int
    *m: int
    """
    salida = 0
    factorialN = factorial(n)
    factorialM = factorial(m)
    factorialN_M = factorial(n-m) 
     
    return factorialN / (factorialM*factorialN_M)


numero = leer_entero("Profundidad triángulo: ")

n = 0

while n < numero:
    m = 0
    while m <= n:
        elemento = int(elemento_pascal(n,m))
        print(elemento, end=" ")
        m += 1
    print("\n")
    n += 1
