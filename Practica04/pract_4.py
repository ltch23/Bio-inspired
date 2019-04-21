import numpy as np
import math as m
from random import *

np.set_printoptions(suppress=True)

f = open("datos.txt", "r")
fout = open("out", "w+")
data=[x.split() for x in f ]

n_x=int(data[0][1])
m_size=int(data[1][1])
g=int(data[2][1])
exper= int(data[3][1])
t_sele=data[4][1]
t_cruce=data[5][1]
p_cruce=float(data[6][1])
p_mute=float(data[7][1])
eli=data[8][1]
nor=data[9][1]
v_min=int(data[10][1])
v_max=int(data[11][1])
# print(data)

l=0
total=0
dig=6
left = -100
right = 100
i_max=0
act_mean=0
sum_mejor=0
v_best=	np.zeros((exper,g))
v_off=	np.zeros((exper,g))
v_on=	np.zeros((exper,g))

curvas = np.zeros((g,3))


def gen_l(p):
	return m.ceil(m.log2(right-left)+p*m.log2(10))

def individuo():
	n_bin = np.random.randint(2, size=(l*n_x,))
	return n_bin
	
def popul(m_size):
	return np.array([individuo() for i in range(m_size)])

def codBintoR(n_bin):
	rptas=np.zeros(n_x)
	for k in range(n_x):
		rpta=0
		for i in range(k*l,(k+1)*l):
			rpta += (2**(i-k*l))*n_bin[i]
		rpta = left+rpta*((right-left)/((2**l)-1))
		rptas[k]=rpta
	return rptas

def inv(x):
	if x == 0: return 1
	else: return 0

def function(x_bin):
	x=codBintoR(x_bin)
	
	pow_xs =0
	for i in range(n_x):
		pow_xs += x[i]**2

	num = m.sin(pow_xs)**2-0.5
	den = (1.0+0.001*pow_xs)**2
	return x, 0.5 - num/den

def functions(xs):
	fx=np.zeros(m_size)
	x=np.zeros((m_size,n_x))

	for i in range(m_size):
		x[i],fx[i]=function(xs[i])
	return x, fx

def max_():
	maximo=0
	ind=0
	for i in range(m_size):
		temp=all_x[i,n_x*l+n_x]
		# print("temp: ",temp)
		if np.greater(temp,maximo) ==True:
			maximo=temp
			ind=i
	i_max=ind
	ind_mejor=all_x[i_max,:]
	return ind_mejor

def swap(x1,x2):
	temp=x1
	x1=x2
	x2=temp
	return x1,x2

def elitism(xs,ind):
	rand = randint(0,m_size-1)
	xs[rand,:]=	ind[:-(n_x+4)]
	return xs	

def normalization(min_,max_):
	np.sort(all_x[:,n_x*l+n_x+1],axis=0)
	for i in range(m_size):
		all_x[i,n_x*l+n_x+1]= min_ +((max_-min_)/(m_size-1))*(i-1)

def ruleta(total):
	n_rand = np.random.rand(1)*total
	for i in range(m_size):
		# print(n_rand,"  ",all_x[i,2*l+3])
		if np.greater_equal(n_rand,all_x[i,n_x*l+n_x+1])==True:
			continue
		else: return i-1
	return i-1

def select_ruleta():
	selected = np.zeros((m_size,2*l))
	tmp=0
	normalization(10,60)

	total=np.sum(all_x[:,2*l+2])
	# aptitud
	for i in range(m_size):
		tmp+=all_x[i,2*l+2]
		all_x[i,2*l+3] = tmp
		all_x[i,2*l+4] = all_x[i,2*l+2]/total

	for j in range(m_size):
		i_sel = ruleta(total)
		selected[j,:]=all_x[i_sel,:-6]

	return selected

def select_estocast():
	# print("estocast")
	selected = np.zeros((m_size,(n_x*l)+n_x+1))
	tmp=cont=0
	total=np.sum(all_x[:,n_x*l+n_x])
	for i in range(m_size):
		all_x[i,n_x*l+n_x+1] = (m_size*all_x[i,n_x*l+n_x])/total
		all_x[i,n_x*l+n_x+2] = int(all_x[i,n_x*l+n_x+1])
		all_x[i,n_x*l+n_x+3] = all_x[i,n_x*l+n_x+1]-all_x[i,n_x*l+n_x+2]
	
	# print("selected valores")
	# print(all_x[:,:-(n_x+1)])
	for j in range(m_size):
		if np.greater_equal(all_x[j,n_x*l+(n_x+2)],1.0)==True:
			selected[cont,:] = all_x[j,:-3]
			cont+=1
	tmp=0
	for i in range(m_size):
		tmp+=all_x[i,n_x*l+n_x+3]
		all_x[i, n_x*l+n_x+1] = tmp

	for k in range(cont,m_size):
		i_sel = ruleta(total)
		selected[k,:]=all_x[i_sel,:-3]
	

	return selected

def cruce_1(select):
	# print("**cruce**")
	sel_1=sel_2=ind_12=np.zeros(2*l)
	cruced=np.zeros((m_size,2*l))
	for j in range(m_size):
		n_rand = random()
		sel_1 = select[j,:2*l]
		if n_rand > p_cruce:
			rand = randint(0,m_size-1)
			sel_2 = select[rand,:2*l]
			cut = randint(1,2*l-1)
			ind_12 = np.concatenate((sel_1[:cut],sel_2[cut:]))
			cruced[j,:]=ind_12
		else:
			cruced[j,:]=select[j,:2*l]
	return cruced

def cruce_2(select):
	# print("**cruce**")
	sel_1=sel_2=ind_12=np.zeros(n_x*l)
	cruced=np.zeros((m_size,n_x*l))
	for j in range(m_size):

		n_rand = random()

		sel_1 = select[j,:n_x*l]
		if n_rand > p_cruce:
			rand = randint(0,m_size-1)
			sel_2 = select[rand,:n_x*l]
			cut1 = randint(1,n_x*l-1)
			cut2 = randint(1,n_x*l-1)
			if  cut1 > cut2:
				swap(cut1,cut2)

			ind_12 = np.concatenate((sel_2[:cut1],sel_1[cut1:]))
			ind_12 = np.concatenate((ind_12[:cut2],sel_2[cut2:]))

			## print("crecu: ",sel_1[:cut],"+",sel_2[cut:])
			# print("cruce: ",ind_12)
			cruced[j,:]=ind_12
		else:
			cruced[j,:]=select[j,:n_x*l]
			# print("here")

	# print("__cruce__")
	return cruced

def cruce_3(select):
	# print("**cruce**")
	sel_1=sel_2=ind_12=np.zeros(n_x*l)
	cruced=np.zeros((m_size,n_x*l))
	# print("before\n",selected.astype(int))
	for j in range(m_size):

		n_rand = random()
		# print("n_rand: ", n_rand)

		sel_1 = select[j,:n_x*l]
		if n_rand > p_cruce:

			for k in range(n_x*l):
				n_rand = random()
				if n_rand >= 0.5:
					ind_12[k]=sel_1[k]
				else:
					ind_12[k]=sel_2[k]

			## print("crecu: ",sel_1[:cut],"+",sel_2[cut:])
			# print("cruce: ",ind_12)
			cruced[j,:]=ind_12
		else:
			cruced[j,:]=select[j,:n_x*l]
			# print("here")

	# print("__cruce__")
	# print("after\n",cruced.astype(int))
	return cruced

def cruce_4(select):

	# print("**cruce**")
	sel_1=sel_2=ind_12=np.zeros(n_x*l)
	cruced=np.zeros((m_size,n_x*l))
	for j in range(m_size):

		n_rand = random()

		sel_1 = select[j,:n_x*l]
		if n_rand > p_cruce:
			rand = randint(0,m_size-1)
			sel_2 = select[rand,:n_x*l]

			tmp=0
			for i in range(n_x*l-1,1,-1):
				cruced[j,i]=sel_1[i]+sel_2[i]+tmp
				if cruced[j,i] == 2:
					cruced[j,i] = 0
					tmp=1
				elif cruced[j,i] == 3:
					cruced[j,i] = 1
					tmp=1
		else:
			cruced[j,:]=select[j,:n_x*l]
			# print("here")

	# print("__cruce__")
	# print(cruced)
	return cruced

def cruce_5(select):
	# print("**cruce**")
	sel_1=sel_2=ind_12=np.zeros(n_x*l)
	cruced=np.zeros((m_size,n_x*l))
	for j in range(m_size):

		n_rand = random()

		sel_1 = select[j,:n_x*l]
		if n_rand > p_cruce:

			sel_2 = select[i_max,:n_x*l]
			cut1 = randint(1,n_x*l-1)
			cut2 = randint(1,n_x*l-1)
			if  cut1 > cut2:
				swap(cut1,cut2)

			ind_12 = np.concatenate((sel_2[:cut1],sel_1[cut1:]))
			ind_12 = np.concatenate((ind_12[:cut2],sel_2[cut2:]))

			## print("crecu: ",sel_1[:cut],"+",sel_2[cut:])
			# print("cruce: ",ind_12)
			cruced[j,:]=ind_12
		else:
			cruced[j,:]=select[j,:n_x*l]
			# print("here")

	# print("__cruce__")
	return cruced



def mute_1(cruced):

	for i in range(m_size):
		n_rand = random()
		if n_rand > p_mute:
			cut = randint(1,n_x*l-1)
			cruced[i,cut]=inv(cruced[i,cut])


if __name__ == '__main__':
	
	for it in range(exper):

		print("\n0ra generacion")

		l=gen_l(dig)
		all_x=np.zeros((m_size,n_x*l+(n_x+4)))

		gen_x = popul(m_size)
		all_x[:,:-(n_x+4)] = gen_x
		x,gen_fx = functions(gen_x)

		for ii in range(n_x):
			all_x[:,n_x*l+ii] = x[:,ii]
			

		all_x[:,n_x*l+n_x] = gen_fx
		#los mejores	
		# print(all_x[:,n_x*l:])

		ind_mejor=max_()
		mejor=ind_mejor[n_x*l+n_x]
		v_best[it,0]=mejor

		act_mean=np.mean(all_x[:,n_x*l+n_x])
		v_on[it,0]=act_mean
			
		sum_mejor=mejor
		v_off[it,0]=sum_mejor



		# print(all_x[:,n_x*l:2*l+2])

		if t_sele=="1": selected=select_ruleta()
		elif t_sele=="2":selected=select_estocast()

		if t_cruce=="1": cruced=cruce_1(selected)
		elif t_cruce=="2": cruced=cruce_2(selected)
		elif t_cruce=="3": cruced=cruce_3(selected)
		elif t_cruce=="4": cruced=cruce_4(selected.astype(int))
		elif t_cruce=="5": cruced=cruce_5(selected)

		mute_1(cruced)

		if eli=="1": cruced = elitism(cruced,ind_mejor)
		# print(cruced)
			
	# '''
	# 	print("\n",cruced)
	# '''
		for i in range(1,g):
			
			print ("\n",i," generacion")

			all_x[:,:-(n_x+4)] = cruced
			x,gen_fx = functions(cruced)
			
			for ii in range(n_x):
				all_x[:,n_x*l+ii] = x[:,ii]

			all_x[:,n_x*l+n_x] = gen_fx
			
			# print(all_x[:,n_x*l:])	

			ind_mejor=max_()
			mejor=ind_mejor[n_x*l+n_x]

			v_best[it,i] = mejor

			sum_mejor+=mejor
			v_off[it,i]=sum_mejor/(i+1)

			act_mean += np.mean(all_x[:,n_x*l+n_x])
			v_on[it,i] = act_mean/(i+1)
			# print("mean: ",np.mean(all_x[:,n_x*l+n_x]))
		
			# print(all_x[:,n_x*l:n_x*l+n_x])
			
			if t_sele=="1": selected=select_ruleta()
			elif t_sele=="2":selected=select_estocast()

			if t_cruce=="1": cruced=cruce_1(selected)
			elif t_cruce=="2": cruced=cruce_2(selected)
			elif t_cruce=="3": cruced=cruce_3(selected)
			elif t_cruce=="4": cruced=cruce_4(selected.astype(int))
			elif t_cruce=="5": cruced=cruce_5(selected)

			mute_1(cruced)
			
			if eli=="1": cruced = elitism(cruced,ind_mejor)

	# '''		
	# 		# print("\n",cruced)	
	# 		# print(v_cruce)
	# '''	

	curvas[:,0]=np.mean(v_best,axis=0)
	curvas[:,1]=np.mean(v_off,axis=0)
	curvas[:,2]=np.mean(v_on,axis=0)

	name=str(n_x)+"-"+str(t_sele)+"-"+str(p_mute)+"-"+str(p_cruce)+"tc"+str(t_cruce)+str(eli)+str(nor)
	np.savetxt("curvas"+name+".txt",np.around(curvas,decimals=6),fmt="%.8g")
	fout.write(name)