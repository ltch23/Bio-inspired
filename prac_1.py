import math
import numpy as np
import random

def shannon(vect):
	suma = 0.0
	for i in range(len(vect)):
		suma = suma + (vect[i]* np.log2(vect[i]))
	print("shannon: ",-1*suma)
	
def hartley(vect):
	print("hartley: ", np.log2(len(vect)))


def get_frecuency():
	file_tmp= open("fin.txt","r")
	file= open("fin.txt","r")

	#obtener tamaño de texto	
	lenfile=len(file_tmp.read())

	#donde se pondra las frecuencias 
	vec_frec=np.empty(0)
	
	#similar a un contador de palabras
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

	#normalizar valores entre 0 y 1
	#vect_frec_fin=np.true_divide(vec_frec,lenfile)
	
	# return vect_frec_fin
	return vec_frec


def gener():
	file= open("fout.txt","w+")

	list_char="abcdefghijklmnopqrstuvwxyz "
	for i in range (40000):
		char_sel=random.choice(list_char)
		file.write(char_sel)
	

def permut():
	file_tmp= open("fin.txt","r")
	file= open("fout2.txt","w+")
	data= list(file_tmp.read())
	
	for i in range (40000):
		char_sel= random.choice(data)
		data.remov(echar_sel)
		file.write(char_sel)

vector_frec=get_frecuency()

shannon(vector_frec)
hartley(vector_frec)

