#!/usr/bin/python3

prices = [85,100,105]

prop = [0.98,0.40,0.1]

def pexp(xs,ys,p):
#xs is an array of "x" values
#ys is an array of "y" values
#p is the value that you want to evaluate your function at
	if p < xs[0]:
		output = ys[0]
	else:
		output = 0.1
	return output

print(pexp(prices,prop,70))

print(pexp(prices,prop,100))



