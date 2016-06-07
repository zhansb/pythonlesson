# -*- coding: utf-8 -*-

import math

def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('Bad operand type')
	if x >= 0:
		return x
	else:
		return -x


def quadratic(a, b, c):
	if a == 0:
		return;
	x1=-b + math.sqrt(b*b - 4*a*c)
	x2=-b - math.sqrt(b*b - 4*a*c)

	return x1/2/a,x2/2/a
