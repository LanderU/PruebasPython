#!/usr/bin/env python

# -*- coding: UTF-8 -*

# Abrimos el fichero
archivo = open("ficheronumero","r")
# Leemos la primera linea
numero = archivo.readline()
# Cerramos el archivo
archivo.close()
# Casteamos el numero para mostrarlo como un String
str(numero)
# Mostramos el valor por pantalla
print ("El contenido del archivo es: %s" %(numero))