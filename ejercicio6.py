#!/usr/bin/python
# -*- coding: utf-8 -*-

#Generar un valor aleatorio entre 100 y 200. Luego mostrar los números comprendidos entre 1 y el valor generado.

import random

aleatorio = random.randint(100,200)
i = 1

#print aleatorio

while i <= aleatorio:
	print '------------------------'
	print i
	print '------------------------'
	i +=1
	