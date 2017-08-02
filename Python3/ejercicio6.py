#!/usr/bin/python3

import sys

try:
    n = int(input("Introduce el numero: "))
except NameError:
    print("No es un numero...")
    sys.exit(1)

lista = []

while n > 0:
    lista.append(n)
    try:
        n = int(input("Introduce el numero: "))
    except NameError:
        print("No es un numero...")
        sys.exit(1)

# Mostramos el numero mas grande de la lista
print("Numero mayor en la lista: %d" % max(lista))

# Mostramos los numero pares/impares de la lista
for i in lista:
    if i % 2 == 0:
        print("El numero, %d, es par" % i)
    else:
        print("El numero, %d, es impar" % i)
