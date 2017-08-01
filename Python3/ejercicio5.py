#!/usr/bin/python3

''' Factorial '''

while True:
    try:
        n = int(input("Numero: "))
        break
    except NameError:
        print("Error, vuelva a intetnarlo...")

res = 1

for i in range(2, n+1):
    res *=i

print("El factorial de %d, es %d" % (n,res))
