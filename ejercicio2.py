#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
	Inicializar una variable con un valor entero comprendido entre 1 y 100. Generar luego un valor aleatorio también comprendido entre 1 y 100. 
	Mostrar un mensaje si el valor generado coincide con el valor de la variable.
'''

import random

aleatorio=random.randint(1,100)

n = 69

if aleatorio == n:
	print 'El número aleatorio %d, es el mimso que el que hemos introducido %d' %(aleatorio,n)
else:
	print 'El número aleatorio sacado es %d y no se corresponde con el introducido %d' %(aleatorio,n)