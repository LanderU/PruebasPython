#!/usr/bin/env python

def factorial(n):
	"""Calcula el factorial de un número"""
	resultado = 1
	for i in range(1,n+1):
		resultado*=i
	return resultado

if __name__ == '__main__':

    while True:
        try:
            num = int(input("Número para sacar el factorial: "))
            break
        except NameError:
            print("No válido...")
            print("Prueba otra vez...")

    print("El factorial de %d, es: %d " % (num,factorial(num)))
