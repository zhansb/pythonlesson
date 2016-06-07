#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def yanghui1(max):
    n=0
    N = [1]
    while n < max:
        yield N
        N.append(0)
        N = [N[i-1] + N[i] for i in range(len(N))]
        n +=1

def yanghui(max):
    n=0
    l=[1]
    while n < max:
        yield l
        pl=list(l)
        n +=1

        l.append(1)
        i=1
        while i < n:
            l[n-i]=l[i]=pl[i-1]+pl[i]
            i += 1
    
y=yanghui1(20)

while True:
    try:
        print(next(y))
    except StopIteration as e:
        print('DONE')
        break
