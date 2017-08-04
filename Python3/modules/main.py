#!/usr/bin/env python


import funciones as f

def pedirNumero():
    while True:
        try:
            n = int(input("Escriba el número: "))
            return n
            break
        except:
            print("Número no válido...")
            print("Vuelva a intetnarlo...")


if __name__ == "__main__":

    num = pedirNumero()
    print("El cuadrado de %d es: %d, y el cubo de %d es: %d" % (num,f.cuadrado(num), num, f.cubo(num)))
