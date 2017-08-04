#!/usr/bin/env python


import funciones as f


if __name__ == "__main__":

    num = f.pedirNumero()
    print("El cuadrado de %d es: %d, y el cubo de %d es: %d" % (num,f.cuadrado(num), num, f.cubo(num)))
