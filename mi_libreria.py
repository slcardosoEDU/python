def leer_entero(prompt):
    """Lee de la entrada estandar un entero."""
    esEntero = False
    numero = -1
    while not  esEntero:
        numero = input(prompt)
        try:
            numero = int(numero)
            esEntero = True
        except ValueError:
            print("Eso no es un número.")
    return numero

def factorial(n):
    """Calcula el factorial de n
    *n: int
    """
    contador = 1
    factorial = 1
    while contador <= n:
       factorial = factorial * contador
       contador += 1
    
    return factorial

def mcd(a,b):
    """Calcula el M.C.D de a y b
    *a: int
    *b: int
    """
    n = a
    
    
    while a % n !=0 or b % n != 0:
        print(f"Probando n={n}")
        n = n-1

    return n