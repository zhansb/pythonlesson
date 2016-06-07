#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().status.user.timeline.list)

class Animal(object):
    _type='Animal'
    def run(self):
        print('%s is running' % self._type)

      
class Dog(Animal):
    _type='Dog'
    def run1(self):
        print('Dog is running')
    def __str__(self):
        return 'This is a Dog'
    def __repr__(self):
        return 'This is a Dog'

