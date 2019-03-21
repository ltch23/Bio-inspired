import math
import numpy as np

def shanon(vect):
	suma = 0.0
	for i in range(len(vect)):
		suma = suma + (vect[i]* np.log2(vect[i]))
	return -1*suma;
	
def hartley(vect):
	return np.log2(len(vect))

#vector=np.array([0.5,0.2,0.1,0.1,0.1])
#vector_2=np.array([0.2,0.2,0.2,0.2,0.2])


def get_frecuency():
	file_tmp= open("fin.txt","r")
	file= open("fin.txt","r")
		
	lenfile=len(file_tmp.read())

	vec_frec=np.empty(0)
	dicc={}
	for line in file:
		for char in line.lower(): 
			if char not in dicc:
				dicc[char]=1
			else:
				dicc[char]+=1
	for k,v in dicc.items():
		#print(k,v)
		vec_frec=np.append(vec_frec,v)

	#normalizar)
	vect_frec_fin=np.true_divide(vec_frec,lenfile)
	#print(vect_frec_fin)
	return vect_frec_fin

vector_frec=get_frecuency()

print("shanon: ",shanon(vector_frec))
print("hartley: ",hartley(vector_frec))



