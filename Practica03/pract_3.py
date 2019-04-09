import numpy as np
import math as m
from matplotlib import pyplot
from random import *

dig=6
left = -100
right = 100
l=0
m_size=10
total=0
g=2
def individuo():
	n_bin = np.random.randint(2, size=(l*2,))
	# num_r=codBintoR(n_bin)
	# return num_r
	return n_bin
def popul(size):
	return np.array([individuo() for i in range(size)])

def gen_l(p):
	return m.ceil(m.log2(right-left)+p*m.log2(10))

def codBintoR(n_bin):
	# print("bin: ",n_bin)
	rpta1=rpta2=0
	for i in range(l):
		rpta1 += (2**i)*n_bin[i]
	rpta1 = left+rpta1*((right-left)/((2**l)-1))
	# print("R1: ",rpta1)

	for i in range(l,l*2):
		rpta2 += (2**(i-l))*n_bin[i]
	rpta2 = left+rpta2*((right-left)/((2**l)-1))
	# print("R2: ",rpta2)
	return [rpta1,rpta2]

def function(x_bin):
	x=codBintoR(x_bin)
	pow_xs = x[0]**2 + x[1]**2
	num = m.sin(pow_xs)**2-0.5
	den = (1.0+0.001*pow_xs)**2
	return 0.5 - num/den

def functions(xs):
	arr=np.zeros(m_size)

	all_x=np.zeros((m_size,2*l+3))
	for i in range(xs.shape[0]):
		arr[i]=function(xs[i])
		all_x[:,:-3] = xs[i]
		all_x[i,2*l] = arr[i]
	return arr,all_x

def aptitud():
	tmp=0
	total=np.sum(all_x[:,56])
	for i in range(m_size):
		tmp+=all_x[i,2*l]
		all_x[i,2*l+1] = tmp
		all_x[i,2*l+2] = all_x[i,2*l]/total
	print ("total: ",total)
	return total

def ruleta(total):
	n_rand = np.random.rand(1)*total
	# n_rand = random()*total
	# print("total: ",total)
	print("n_rand: ",n_rand)
	for i in range(m_size):
		# print(n_rand,"  ",all_x[i,2*l+1])
		if np.greater_equal(n_rand,all_x[i,2*l+1])==True:
			continue
		else:
			return i-1

def selection():
	#

def cruce():
	 sel_ind_A = d2b(selected[j],x_size)
        sel_ind_B = d2b(selected[j+1],x_size)
    
    #select point to cross over
        cut_point = randint(1,x_size)
    
    #new individual AB
        ind_AB = sel_ind_A[:cut_point] + sel_ind_B[cut_point:]
def GA():
    #Reseting list for 2nd generation
	for i in range(g):
		total=aptitud()
		selected = np.zeros((m_size,2*l+3))
		print("all_x")
		print(all_x[:,56:])
		for j in range(m_size):
			i_sel = ruleta(total)
			selected[j,:-2]=all_x[i_sel,:-2]
		all_x[:,:-2]=selected[:,:-2]
		print("selected")
		print(selected[:,56:])

	return 0 

if __name__ == '__main__':
	l = gen_l(dig)
	gen_x = popul(m_size)
	gen_fx,all_x = functions(gen_x)
	
	# print(all_x[:,56:])
	
	# selec=ruleta()
	# print("all_x")

	# print(all_x[selec,:])
	# print(all_x[:,56:])
	GA()
	# print("sum: ", sum(all_x[:,56]))
	# print("x: ",x_bin)
	# fx=function(x_bin)
	# print("fxs: ",fx)

	# print(codBintoR())
	
	##
# print(codRtobin(6))


