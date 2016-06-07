#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import logging

#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.ERROR)

def find_file(p,s,l=0):
    logging.debug('%d----%s' %(l, p))
    l+=1
    for x in os.listdir(p):
        fp=os.path.join(p,x)
        logging.debug('%d++%s' %(l,fp))
        if os.path.isdir(fp):
            find_file(fp,s,l)
        elif os.path.isfile(fp):
            if x.find(s) > 0:
                print(fp)

find_file('.', 'dict')

import stat
from datetime import datetime

def printfileinfo(f):
    fstat=os.stat(f)
    print('%o\t%d\t%d\t%d\t%s\t%s'
            % (fstat[stat.ST_MODE], 
                fstat[stat.ST_UID], 
                fstat[stat.ST_GID], 
                fstat[stat.ST_SIZE], 
                datetime.fromtimestamp(fstat[stat.ST_MTIME]).strftime('%Y-%m-%d %H:%M'), 
                f))

def dirl(p):
    for x in os.listdir(p):
        printfileinfo(x)

dirl('.')
