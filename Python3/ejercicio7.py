#!/usr/bin/env python

import sys

lista = ["Hola","esto","es","una","prueba"]


cadena=input("Escriba la cadena a buscar en la lista: ")

if cadena in lista:
    print("La cadena %s, esta en la lista, mas concretamente en la posicion: %d" % (cadena,lista.index(cadena)))
else:
    print("La cadena %s, no esta en la lista" % cadena)

try:
    pos = int(input("Posicion en la que cambiar la cadena: "))
except NameError:
    print("No valido...")
    sys.exit(1)

if pos > len(lista) - 1 or pos < 0:
    print("Los numeros de la lista van del 0 al %d" % (len(lista) -1))
else:
    print("La lista antes tenía esta pinta: ")
    for i in lista:
        print(i, end=" ")
    print()
    lista[pos] = cadena
    print("Ahora tiene esta otra: ")
    for i in lista:
        print(i, end= " ")
    print()
