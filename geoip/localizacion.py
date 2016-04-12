#!/usr/bin/env python

# -*- coding: UTF-8 -*-
 
import pygeoip
 
def main():
    #geoip_country() 
    geoip_city()
    #print 'done'
 
def geoip_city():
    path = 'GeoLiteCity.dat'
    gic = pygeoip.GeoIP(path)
    print gic.record_by_addr('79.152.252.109')
    #print gic.region_by_addr('79.152.252.109')
 
#def geoip_country(): 
    #path = 'GeoLiteCity.dat'
    #gi = pygeoip.GeoIP(path)
    #print gi.country_code_by_addr('79.152.252.109')
    #print gi.country_name_by_addr('79.152.252.109')
 
if __name__ == '__main__':
    main()
