#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools
'''
def log(fun):
    @functools.wraps(fun)
    def wrapper(*args, **kw):
        print("begin call %s"% fun.__name__)
        r=fun(*args,**kw)
        print("end call %s"% fun.__name__)
        return r
    return wrapper
'''
def log(text):
    def decorator(fun):
        @functools.wraps(fun)
        def wrapper(*args, **kw):
            print("%s begin call %s"% (text,fun.__name__))
            r=fun(*args,**kw)
            print("%s end call %s"% (text,fun.__name__))
            return r
        return wrapper
    @functools.wraps(text)
    def wrapper1(*args, **kw):
        print("begin call %s"% (text.__name__))
        r=text(*args,**kw)
        print("end call %s"% (text.__name__))
        return r
    if callable(text):
        return wrapper1
    else:
        return decorator

@log
def ftest():
    print('run ftest=%s'% ftest.__name__)
    #return 'return st'
    return (1,2)

@log('exe')
def ftest1(a,b):
    print('run ftest=%s'% ftest1.__name__)
    #return 'return st'
    return {'a':a,'b':b}

re=ftest()
print('ftest return=',re)
re=ftest1(123,456)
print('ftest1 return=',re)
