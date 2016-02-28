#!/usr/bin/python
# -*- coding: utf-8 -*-

#Generar un valor aleatorio comprendido entre 1 y 5. Luego mostrar en castellano el valor generado.

import random

aleatorio = random.randint(1,5)

if aleatorio == 1:
	print	'UNO'
elif aleatorio == 2:
	print 'DOS'
elif aleatorio == 3:
	print 'TRES'
elif aleatorio == 4:
	print 'CUATRO'
else:
	print 'CINCO'