# -*- coding: utf-8 -*-

def f1(a=1,b=2,*,c,**kw):
    print('a=', a, 'b=', b , 'c=', c, 'kw=', kw)
def f2(a=1,b=2,*,c,**kw):
    print('a=', a, 'b=', b , 'c=', c, 'kw=', kw)

d1={'a':2, 'b':3,'c':4,'e':5,'f':6}
f1(c=2)
f1(**d1)
