import numpy as np

# t -> contador generaciones
# n -> cantidad de variables
# m -> maximo de generaciones
# k -> frecuencia de actualizacopj



#generar individuo 
def individuo(n):
	return np.random.uniform(-2.048, 2.048,n)

#mutar
def mutar(x,sigma):
	aux = x+np.random.normal(scale=sigma)
	# if aux[0] > 2.048:
	# 	aux[0]= 2.048
	# elif aux[0] < -2.048:
	# 	aux[0]= -2.048
	
	# if aux[1] > 2.048:
	# 	aux[1]= 2.048
	# elif aux[1] < -2.048:
	# 	aux[1]= -2.048

	return aux 

def mutar_2(xl,sigma):
	aux=xl.shape[0]
	arr=np.zeros((aux*2,xl.shape[1]))
	for i in range (0, xl.shape[0]):
	# 	print(xl[i,:],"\n")
		arr[i,:]=(mutar(xl[i,:],sigma))
		arr[i+aux,:]=(mutar(xl[i,:],sigma))
		# print(i)

	#  	# arr.append(mutar(i,sigma))
	 	# arr.append(mutar(i,sigma))
	return arr
	# return arr

#funcion1
def func1(x):
	return 100*(x[0]**2 -x[1]**2) + ((1-x[0])**2)

def func2(x):
	arr=np.zeros((x.shape[0],x.shape[1]+1))
	# print(arr[1,0])
	for i in range (0, x.shape[0]):
		arr[i,:]=[func1(x[i,:]),x[i,0],x[i,1]]

	return arr

def mejor(x,fx,x_p,fx_p):	
		if fx > fx_p:
			return x,fx
		else:
			return x_p,fx_p
def mejor2(x):
	arr=np.sort(x,axis=0)
	# print(arr)
	# print("asd",arr[5:10])
	tmp=arr[5:10]
	return (tmp)
	# print("asd",arr[5:10,0])
	# return arr[5:10]
#estrategia(1+1)−EE
def est_evolutiva_1(n,m,k):
	sigma=3.0
	c=0.817
	x=individuo(n)
	print('x:',x)
	fx=func1(x)
	ps=0
	print('fx: ',fx)


	for t in range(m):
		x_p=mutar(x,sigma)
		fx_p=func1(x_p)
			
		#evaluar
		#print('x_p:',1-x_p)
		x,fx = mejor(x,fx,x_p,fx_p)
		
		if np.array_equal(x,x_p)==True:	
			ps += 1
		
		print(t,':',x,"->",round(fx,2))

		if t % k == 0:
			aux=ps/k

			if aux < 0.2:
				sigma /= c
			elif aux > 0.2:
				sigma *=c

#estrategia (μ+λ)−EE



def est_evolutiva_2(n,m,k,mu,landa):
	sigma=3.0
	c=0.817
	x_l=np.array([individuo(n) for i in range (mu)])
	# print(x_l)

	fx_l=np.array([func1(i) for i in x_l])
	# print(fx_l)
	
	ps=0
	for t in range(m):
		# x_p_l=np.array([mutar_2(x_l,sigma)])
		x_p_l=mutar_2(x_l,sigma)
		# print("\n",x_p_l)
		fx_l=func2(x_p_l)

		# x_l=mejor2(fx_l) importa
		x_l=mejor2(fx_l)[:,1:3]
		print(x_l,"\n")

		#evaluar
		#print('x_p:',1-x_p)
		# x,fx = mejor(x,fx,x_p,fx_p)
		
		# if np.array_equal(x,x_p)==True:	
		# 	ps += 1
		
		# print(t,':',x,"->",round(fx,2))

		if t % k == 0:
			aux=ps/k

			if aux < 0.2:
				sigma /= c
			elif aux > 0.2:
				sigma *=c

if __name__ == '__main__':
	# est_evolutiva_1(2,40,10)
	est_evolutiva_2(2,10,10,5,10)
