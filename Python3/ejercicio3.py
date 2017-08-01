#!/usr/bin/python3

''' Par impar ''' 

while True:
    try:
        n = int(input("Introduzca el numero: "))
        break
    except NameError:
        print("No valido...")
        print("Intentalo otra vez...")

if n % 2 == 0:
    print("El numero: %d, es par" % n)
else:
    print("El numero: %d, no es par" % n)
