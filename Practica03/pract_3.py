import numpy as np
import math as m
from matplotlib import pyplot
from random import *

np.set_printoptions(suppress=True)

l=0
total=0
dig=6
left = -100
right = 100
i_max=0
m_size=40
g=100


def gen_l(p):
	return m.ceil(m.log2(right-left)+p*m.log2(10))


def individuo():
	n_bin = np.random.randint(2, size=(l*2,))
	return n_bin
	
def popul(size):
	return np.array([individuo() for i in range(size)])


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

def inv(x):
	if x == 0: return 1
	else: return 0

def function(x_bin):
	x=codBintoR(x_bin)
	pow_xs = x[0]**2 + x[1]**2
	num = m.sin(pow_xs)**2-0.5
	den = (1.0+0.001*pow_xs)**2
	return x, 0.5 - num/den

def functions(xs):
	fx=np.zeros(m_size)
	x=np.zeros((m_size,2))

	for i in range(xs.shape[0]):
		x[i],fx[i]=function(xs[i])
	return x,fx

def max_():
	maximo=0
	ind=0
	for i in range(m_size):
		temp=all_x[i,2*l+2]
		# print("temp: ",temp)
		if np.greater(temp,maximo) ==True:
			maximo=temp
			ind=i
	# print("max ",np.amax(all_x[:,2*l+2]))	
	# return all_x[ind,:]
	i_max=ind
	print("mejor: ",all_x[i_max,2*l:2*l+3])


def elitism(xs):
	rand = randint(0,m_size-1)
	max_()
	xs[rand,:]=	all_x[i_max,:2*l]
	return xs	

def ruleta(total):
	n_rand = np.random.rand(1)*total
	# n_rand = random()*total
	# print("total: ",total)
	# print("n_rand: ",n_rand)
	for i in range(m_size):
		# print(n_rand,"  ",all_x[i,2*l+1])
		if np.greater_equal(n_rand,all_x[i,2*l+3])==True:
			continue
		else:
			return i-1

def select_ruleta():
	selected = np.zeros((m_size,2*l))
	tmp=0
	total=np.sum(all_x[:,2*l+2])
	# aptitud
	for i in range(m_size):
		tmp+=all_x[i,2*l+2]
		all_x[i,2*l+3] = tmp
		all_x[i,2*l+4] = all_x[i,2*l+2]/total

	for j in range(m_size):
		i_sel = ruleta(total)
		selected[j,:]=all_x[i_sel,:-5]

	return selected



def selection_x():
	select_ruleta()
	select_asdsad()

# 	#


def cruce_1(select,porcetanje):
	# print("**cruce**")
	sel_1=sel_2=ind_12=np.zeros(2*l)
	cruced=np.zeros((m_size,2*l))
	for j in range(m_size):

		n_rand = random()
		# print("n_rand: ", n_rand)

		sel_1 = select[j,:2*l]
		if n_rand > porcetanje:
			rand = randint(0,m_size-1)
			sel_2 = select[rand,:2*l]
			## print("sel_1: ",sel_1,"\nsel_2: ",sel_2)
			cut = randint(1,2*l-1)
			ind_12 = np.concatenate((sel_1[:cut],sel_2[cut:]))
			## print("crecu: ",sel_1[:cut],"+",sel_2[cut:])
			# print("cruce: ",ind_12)
			cruced[j,:]=ind_12
		else:
			cruced[j,:]=select[j,:2*l]
			# print("here")

	# print("__cruce__")
	return cruced


def mute_1(cruced,porcetanje):

	# print("**mute**")
	for i in range(m_size):
		n_rand = random()
		# print("n_rand: ", n_rand)
		if n_rand > porcetanje:
			cut = randint(1,2*l-1)
			# print("cut: ",cut,)
			## print("before: ",cruced[i])
			cruced[i,cut]=inv(cruced[i,cut])
	# 		print("mute: ",cruced[i])
	# print("__mute__")


if __name__ == '__main__':
	
#algoritmo genetio
	print("1ra generacion\n")

	l=gen_l(dig)
	all_x=np.zeros((m_size,2*l+5))

	gen_x = popul(m_size)
	all_x[:,:-5] = gen_x
	x,gen_fx = functions(gen_x)
	all_x[:,2*l] = x[:,0]
	all_x[:,2*l+1] = x[:,1]
	all_x[:,2*l+2] = gen_fx
	
	print(all_x[:,2*l:2*l+2])
	# print(all_x[:,2*l:])
	# print("all_x: ",all_x)
	# selection_x()
	selected = select_ruleta()
	cruced = cruce_1(selected,0.5)
	mute_1(cruced,0.5)	

	# print("\n",cruced)
	elitism(cruced)


	for i in range(g):
		
		print (i," generacion\n")

		all_x[:,:-5] = cruced
		x,gen_fx = functions(cruced)
		
		all_x[:,2*l+2] = gen_fx
		all_x[:,2*l] = x[:,0]
		all_x[:,2*l+1] = x[:,1]
		
		print(all_x[:,2*l:2*l+3])
		
		selected = select_ruleta()	
		cruced = cruce_1(selected,0.5)			
		mute_1(cruced,0.5)
		elitism(cruced)
		# print("\n",cruced)	

		# print(v_cruce)
		

