import math
import random

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

def dimensiones_esfera(radio):
    volumen = (4 * math.pi /3) * radio ** 3
    superficie = (4 * math.pi) * radio **2
    print(f"Esfera\n volumen = {volumen:.2f}\n superficie = {superficie:.2f}")

def distancia(x1, y1, x2, y2):
    """
    Calcula y devuelve la distancia euclidiana que separa los puntos (x1, y1) y (x2, y2)
    """
    return math.sqrt(((x2-x1) ** 2) + ((y2-y1) ** 2))

def muestra_pares(numero):
    """
    Muestra los primeros n números pares.
    * numero: int
    """
    n = 0
    cont = 2
    while n < numero:
        print(cont)
        cont += 2
        n += 1

def calcular_segundos(dias, horas, minutos):
    segundos = (minutos*60) + (horas * 3600) + (dias * 3600 * 24)
    return segundos

def hora_correcta(hora):
    return hora <24 and hora >= 0

def minuto_correcto(minuto):
    return minuto < 60 and minuto >= 0

def diferencia_min(hora1, minuto1, hora2, minuto2):
    if not (hora_correcta(hora1) and hora_correcta(hora2) and minuto_correcto(minuto1) and minuto_correcto(minuto2)):
        raise ValueError("Hora o minuto incorrecto")

    minutos = (hora2 - hora1) * 60
    minutos += minuto2 - minuto1
    return minutos

def divisores_primos(numero):
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

def aleatorios(cantidad, min, max):
    """
    Imprime la cantidad indicada de numeros aleatorios entre min y max
    """
    i = 0
    while i < cantidad:
        print(random.randint(min,max))
        i += 1

def aleatorios(cantidad):
    """
    Imprime la cantidad indicada de numeros aleatorios entre 0 y 1
    """
    i = 0
    while i < cantidad:
        print(random.random())
        i += 1