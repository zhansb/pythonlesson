#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    with open('/home/zhansb/tmp/test1.txt','r') as f:
        f.read()
except IOError:
    pass
finally:
    print('finally')
print('Done')

