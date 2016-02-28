#!/usr/bin/python
# -*- coding: utf-8 -*-

#Generar 3 números aleatorios entre 1 y 100. Mostrar un mensaje si todos son superiores a 10.

import random

n1 = random.randint(1,100)
n2 = random.randint(1,100)
n3 = random.randint(1,100)

if n1 > 10 and n2 > 10 and n3 > 10:
	print 'Todos los números son mayores que 10, siendo estos sus valores= %d,%d,%d' % (n1,n2,n3)
else:
	print 'No todos los números superan el valor 10, estos son sus valores= %d,%d,%d' % (n1,n2,n3)