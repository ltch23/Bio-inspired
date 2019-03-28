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
	# if aux > 2.048:
	# 	return 2.048
	# elif aux < -2.048:
	# 	return -2.048
	# else:
	return aux 

#funcion1
def func1(x):
	return 100*(x[0]**2 -x[1]**2) + ((1-x[0])**2)

def mejor(x_p,x):	
	return max((x_p,x))


def est_evolutiva(n,m,k):
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
		print('x_p:',1-x_p)
		fx_next = mejor(fx_p,fx)
		fx = fx_next	
		ps += 1
		print(t,':',round(x[0],2),' ',round(x[1],2),"->",round(fx,2),round(sigma,2))

		if t % k == 0:
			aux=ps/k

			if aux > 1/5:
				sigma /= c
			elif aux <1/5:
				sigma *=c

if __name__ == '__main__':
	est_evolutiva(2,40,10)
