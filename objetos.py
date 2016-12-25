#!/usr/bin/env python

#-*- coding: utf-8 -*- 

class Prueba:
	def __init__(self, nombre, apellido):
		self.nombre = nombre
		self.apellido = apellido
	def comparacion(self, otherObject):
		if self.nombre == otherObject.nombre and self.apellido == otherObject.apellido:
			print "Igual"
		else:
			print "Distinto"

if __name__ == '__main__':

	ob1 = Prueba("LAnder","Usategui")
	ob2 = Prueba("Lander","Usategui")

	ob1.comparacion(ob2)