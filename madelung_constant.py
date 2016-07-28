import numpy as np 
import math


catalan = 1.0
index   = 0.0

def calcCatalan(cur, index):
	return (( (4.0*index) + 2 ) / (index + 2))*cur

while catalan <= 1e9:
	cur = catalan
	catalan = calcCatalan(cur, index)
	print 'catalan: ', catalan
	index += 1

	