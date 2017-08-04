#!/usr/bin/env python

def cuadrado(n):
    return (n**2)

def cubo(n):
    return(n**3)

def pedirNumero():
    while True:
        try:
            n = int(input("Escriba el número: "))
            return n
            break
        except:
            print("Número no válido...")
            print("Vuelva a intetnarlo...")
