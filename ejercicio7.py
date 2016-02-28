#!/usr/bin/python
# -*- coding: utf-8 -*-

def calculos ():
	x = int(raw_input ('Introduzca el primer valor: '))
	y = int(raw_input ('Introduzca el segundo valor: '))


	while x > y:
		print 'El segundo valor tiene que ser mayor que el primero...'
		x = raw_input ('Introduzca el primer valor: ')
		y = raw_input ('Introduzca el segundo valor: ')

	while x <= y:
		print '-----------------'
		print x
		print '-----------------'
		x +=1

calculos()
		


		


