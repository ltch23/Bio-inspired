import numpy as np
import math as m
from matplotlib import pyplot

dig=6
left = -100
right = 100
l=0
def individuo():
	n_bin = np.random.randint(2, size=(l*2,))
	num_r=codBintoR(n_bin)
	return num_r

def gen_l(p):
	return m.ceil(m.log2(right-left)+p*m.log2(10))

def codBintoR(n_bin):
	print("bin: ",n_bin)
	rpta1=rpta2=0
	for i in range(l):
		rpta1 += (2**i)*n_bin[i]
	rpta1 = left+rpta1*((right-left)/((2**l)-1))
	print("R1: ",rpta1)

	for i in range(l,l*2):
		rpta2 += (2**i)*n_bin[i]
	rpta2 = left+rpta2*((right-left)/((2**l)-1))
	print("R2: ",rpta2)
	return [rpta1,rpta2]

def function(x):
	pow_xs = x[0]**2 + x[1]**2
	num = m.sin(pow_xs)**2-0.5
	den = (1.0+0.001*pow_xs)**2
	return 0.5 - num/den

if __name__ == '__main__':
	l=gen_l(dig)
	x=individuo()
	print("x: ",x)
	fx=function(x)
	print("fxs: ",fx)

	# print(codBintoR())
	
	##
# print(codRtobin(6))


