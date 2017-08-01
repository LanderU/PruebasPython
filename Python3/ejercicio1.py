#!/usr/bin/python3

import sys

try:
    base = float(input("Introduce la base: "))
except NameError:
    print("No has introducido un numero")
    sys.exit(1)
try:
    altura = float(input("Introduzca la altura: "))
except NameError:
    print("No has introducido un numero")
    sys.exit(1)

per = 2*base + 2*altura
area = base * altura

print("Los resulatdos son Perimetro= %.2f Altura= %.2f" % (per,area))
