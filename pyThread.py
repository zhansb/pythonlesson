#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import logging

#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.ERROR)

print('start %d' % os.getpid())

def child_run(name='child'):
    while True:
        print('%s: this is child(%d), parent is (%d)' % (name, os.getpid(), os.getppid())) 
        time.sleep(1)
def parent_run(cpid=-1,name='parent'):
    while True:
        print('%s: this is parent(%d), child is (%d)' % (name, os.getpid(), cpid)) 
        time.sleep(1)

def fork():
    pid=os.fork()
    if pid==0:
        child_run()
    else:
        parent_run(cpid=pid)

from multiprocessing import Process
def process():
    p=Process(target=child_run,args=('pchild',))
    p.start()
    p.join(timeout=5)
    parent_run()


if __name__=='__main__':
    process()

