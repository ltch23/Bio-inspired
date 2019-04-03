import numpy as np
np.set_printoptions(suppress=True)
# t -> contador generaciones
# n -> cantidad de variables
# m -> maximo de generaciones
# k -> frecuencia de actualizacopj



#generar individuo 
def individuo(n):
	return np.random.uniform(-2.048, 2.048,n)

#mutar
def mutar(x,sigma):
	aux0 = x[0]+np.random.normal(0,sigma)
	aux1 = x[1]+np.random.normal(0,sigma)
	while aux0 > 2.048 or aux0 < -2.048:
		aux0 = x[0]+np.random.normal(0,sigma)
	while (aux1 > 2.048 or aux1 < -2.048):
		aux1 = x[1]+np.random.normal(0,sigma)

	return np.array([aux0,aux1]) 

def mutar_2(xl,sigma):
	print("muta_",xl)
	aux=xl.shape[0]
	arr=np.zeros((aux*2,xl.shape[1]))
	for i in range (0, xl.shape[0]):
	# 	print(xl[i,:],"\n")
		arr[i,:]=(mutar(xl[i,:],sigma))
		arr[i+aux,:]=(mutar(xl[i,:],sigma))
	return arr

#funcion1
def func1(x):
	return 100*(x[0]**2 -x[1]**2) + ((1-x[0])**2)

def func2(x):
	arr=np.zeros((x.shape[0],x.shape[1]+1))
	# print(arr[1,0])
	for i in range (0, x.shape[0]):
		arr[i,:]=[x[i,0],x[i,1],func1(x[i,:])]

	return arr

def mejor(x,fx,x_p,fx_p):	
		# maximizar
		if fx > fx_p:
			return x,fx
		else:
			return x_p,fx_p
def mejor2(x):
	temp=np.sort(x,axis=0)
	#selecciona los 5 mejores
	arr=temp[5:10]
	arr = arr[::-1]
	return arr
	

#estrategia(1+1)−EE
def est_evolutiva_1(n,m,k):
	sigma=3.0
	c=0.817
	x=individuo(n)
	fx=func1(x)
	ps=0


	for t in range(m):
		x_p=mutar(x,sigma)
		fx_p=func1(x_p)
			
		# evaluar
		x,fx = mejor(x,fx,x_p,fx_p)
		
		if np.array_equal(x,x_p)==True:	
			ps += 1
		# resultados		
		print(t,'\n',x,"->",round(fx,2))

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
	# generando poblacion
	x_l=np.array([individuo(n) for i in range (mu)])
	# almacenar los funciones
	fx_l=np.array([func1(i) for i in x_l])
	
	ps=0
	for t in range(m):
		print(t)
		# generar los mu individuos mutados
		x_p_l=mutar_2(x_l,sigma)
		# evaluar su funcion
		fx_l=func2(x_p_l)
		# tener correlativo de x0,x1 y fx en x_all mediante mejor2
		x_all=mejor2(fx_l)
		x_l=x_all[:,0:2]
		fx_l=x_all[:,2:3]

		# resultados
		for i in range(x_all.shape[0]):
			print(np.round(x_l[i],2),"->",np.round(fx_l[i],2))
		print("\n")

if __name__ == '__main__':
	# est_evolutiva_1(2,40,10)
	est_evolutiva_2(2,40,10,5,10)
