#!/usr/bin/env python

class Circulo():

    def __init__(self, radio=0):
        self.set_radio(radio)

    def set_radio(self, circunferencia):
        self._radio = circunferencia / (2 * 3.14)

    def get_radio(self):
        return self._radio

def pedirPantalla():
    while True:
        try:
            n = float(input("Escriba la circunferencia: "))
            return n
            break
        except ValueError:
            print("Número no válido...")
            print("Prueba otra vez")

if __name__ == "__main__":

    num = pedirPantalla()
    c = Circulo(num)
    print("El radio en metros de %.2f es: %.2f" % (num, c.get_radio()))
