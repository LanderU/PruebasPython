#!/usr/bin/python3
import sys

try:
    n1 = int(input("Introduzca un numero: "))
except NameError:
    print("No es un numero")
    sys.exit(1)
try:
    n2 = int(input("Introduzca un numero: "))
except NameError:
    print("No es un numero")
    sys.exit(1)

if n1+n2 > 0:
    print("El numero es positivo")
elif n1+n2 < 0:
    print("El numero es negativo")
else:
    print("La suma es 0")
