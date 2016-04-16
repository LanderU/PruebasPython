#!/usr/bin/env python

# -*- coding: UTF-8 -*-
 
import pygeoip
 
def main():

    geoip_city()

def geoip_city():

    ip = []
    fichero = open('analytics.csv')
    for linea in fichero:
        dato = linea.split(',')
        esta = dato[2] in ip
        if not esta:
            ip.append(dato[2])
    fichero.close()

    path = 'GeoLiteCity.dat'
    gic = pygeoip.GeoIP(path)
    i = 0
    while i < len(ip):
        print gic.record_by_addr(ip[i])['latitude']
        print gic.record_by_addr(ip[i])['longitude']
        i += 1
 
if __name__ == '__main__':
    main()
