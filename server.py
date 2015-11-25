#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import socket
import os
#Creamos el socket.
#os.system('echo "hola" > salida' )
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Dirección del servidor

server_address = ('localhost', 10000)

#Levantamos el socket.

print >> sys.stderr, 'Levantamos el servidor %s puerto %s' % server_address

#Nos enlazamos

s.bind(server_address)

#Nos ponemos a escuchar el número de conexiones simultaneas, que especifiquemos.

s.listen(50)

#Empezamos a esperar las conexiones

while True:

	#Esperamos la conexión
	print >> sys.stderr, 'Esperando una conexion entrante'
	connection, client_address = s.accept()

	try:

		print >> sys.stderr,'Conexión desde: ', client_address
		#Recibimos los datos
		while True:
			
			data = connection.recv(1024)

			
			writeFile = open ('serverescritura', 'a')
			writeFile.write(data)
			writeFile.close()

			

	finally:
		connection.close()


