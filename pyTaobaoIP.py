#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on Oct 20, 2013
@summary: geography info about an IP address
@author: Jay <smile665@gmail.com> http://smilejay.com/
'''

import json, urllib2
import re

def get_host_ip():
    urlobj = urllib2.urlopen('http://ipecho.net/plain')
    ip = urlobj.read()
    #pprint('HOST IP:', data,ip)
    return ip
     
class location_taobao():
    '''
build the mapping of the ip address and its location
the geo info is from Taobao
e.g. http://ip.taobao.com/service/getIpInfo.php?ip=112.111.184.63
The getIpInfo API from Taobao returns a JSON object.
'''
    def __init__(self, ip):
        self.ip = ip
        self.api_url = 'http://ip.taobao.com/service/getIpInfo.php?ip=%s' % self.ip
        self.get_geoinfo()

    def get_geoinfo(self):
        """ get the geo info from the remote API.
return a dict about the location.
"""
        urlobj = urllib2.urlopen(self.api_url)
        data = urlobj.read()
        datadict = json.loads(data, encoding='utf-8')
        self._datadict = datadict['data']
        return self._datadict

    def get_country(self):
        key = u'country'
        return self._datadict[key]

    def get_region(self):
        key = 'region'
        return self._datadict[key]

    def get_city(self):
        key = 'city'
        return self._datadict[key]

    def get_isp(self):
        key = 'isp'
        return self._datadict[key]

 
if __name__ == '__main__':
    #ip = '183.32.190.115'
    ip=get_host_ip()
    print('host ip:',ip)
    iploc = location_taobao(ip)
    print iploc.get_country()
    print iploc.get_region()
    print iploc.get_city()
    print iploc.get_isp()
