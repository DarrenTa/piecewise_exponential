#!/usr/bin/python3

import math

prices = [85,100,105]

prop = [0.98,0.40,0.1]

def pexp(xs,ys,p):
#xs is an array of "x" values
#ys is an array of "y" values
#p is the value that you want to evaluate your function at
	#Break if arreys aren't the same length
	if len(xs) != len(ys):
		sys.exit("Arrays not same length")
	#piece used for determining which part of the piecewise 
	#exponential function is relevant.
	piece = 0
	for k in range(0,len(xs)-1):
		if p > xs[k]:
			piece += 1
	if piece == 0:
		output = ys[piece]
	elif piece == len(xs) -1:
		output = ys[piece]
	else:
		r = (math.log(ys[piece-1])-math.log(ys[piece]))/(xs[piece-1]-xs[piece])
		print("r=",r)
		A = ys[piece-1] * math.e**(-r*xs[piece-1])
		print("A=",A)
		output = A*(math.e**(r*p))
	return output

print(pexp(prices,prop,70))

print("at 95",pexp(prices,prop,95))
print("at 102",pexp(prices,prop,102))


print(pexp(prices,prop,200))
