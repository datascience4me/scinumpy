# -*- coding: utf-8 -*-
import numpy as np 
import math

m = 9.11e-31 #kg
E = 10 #eV
V = 9 #eV
h = 6.582e-16 #eV·s

def probabilityOfTransmission(k1, k2):
	T = (4*k1*k2) / ((k1 + k2)**2)
	return T

def probabilityOfReflection(k1, k2):
	R = ( (k1 - k2) / (k1 + k2) ) ** 2
	return R

def getK1(m, e, h):
	return (math.sqrt(2*m*e) / h)

def getK2(m, e, h, v):
	return (math.sqrt(2*m*(e-v)) / h)

k1 = getK1(m, E, h)
k2 = getK2(m, E, h, V)
T = probabilityOfTransmission(k1, k2)
R = probabilityOfReflection(k1, k2)

print 'Probability of transmission:', T
print 'Probability of reflection:', R
print 'Combined probability should be 1. Combined is: ', R + T
