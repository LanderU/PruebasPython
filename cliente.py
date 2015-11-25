#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Programa Cliente
 
import socket
import sys
import os 
# Creando un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# Conecta el socket en el puerto cuando el servidor esté escuchando
server_address = ('localhost', 10000)
print >>sys.stderr, 'conectando a %s puerto %s' % server_address
sock.connect(server_address)
try:
     
    # Enviando datos
    message = open('ip', 'r')
    #print >> sys.stderr, "El valor del archivo es %s" % message
    #print >>sys.stderr, 'enviando "%s"' % message
    sock.sendall(message.read())
    message.close()
 
    # Buscando respuesta
   # amount_received = 0
   # amount_expected = len(message)
     
   # while amount_received < amount_expected:
    #    data = sock.recv(19)
     #   amount_received += len(data)
      #  print >>sys.stderr, 'recibiendo "%s"' % data
 
finally:
    print >>sys.stderr, 'cerrando socket'
    sock.close()
