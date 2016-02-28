#!/usr/bin/python
# -*- coding: utf-8 -*-

#Generar un valor aleatorio entre -10 y 10. Mostrar un mensaje si el valor generado es negativo, nulo o positivo.

import random

aleatorio=random.randint(0,20)-10

if aleatorio == 0:
	print 'El número aleatorio es nulo'
elif aleatorio < 0:
	print 'El número es negativo %d' %aleatorio
else:
	print 'El número es positivo %d' %aleatorio