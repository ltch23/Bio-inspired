import numpy as np
import math as m
import random 

np.set_printoptions(suppress=True)

f = open("datos.txt", "r")
fout = open("out", "w+")
data = [x.split() for x in f ]

dimension = int(data[0][1]) # dimensiones
len_po = int(data[1][1]) # tamaño de población
n_gen = int(data[2][1]) # generaciones
len_exper = int(data[3][1])  # experimentos
v_min = int(data[4][1]) # limite minimo
v_max = int(data[5][1]) # limite maximo
t_fun = int(data[6][1]) # tipo de funcion


A = 0.5 #0.5  intensidad de sonido 
r = 0.5  #0.5 frecuencias de emisión de pulsos
Qmin = 0.0 # frecuencia minima
Qmax = 2.0 # frecuencia maxima
f_min = 0.0 # aptitud minima
l_min = np.zeros(dimension) # arreglo limite minimo
l_max = np.zeros(dimension) # arreglo limite maximo 
Q = np.zeros(len_po) # frecuencia
velocidad = np.zeros((len_po,dimension)) # velocidad
po_sol = np.zeros((len_po,dimension)) # poblacion de soluciones 
aptitud = np.zeros(len_po) 
mejor = np.zeros(dimension) 

def schwefel(x):
    suma=0.0
    for i in range(dimension):
        suma += x[i]*m.sin(m.sqrt(abs(x[i])))
    return 418.9829*dimension-suma

def fun3(x):
    pow_xs =0
    for i in range(dimension):
        pow_xs += x[i]**2

    num = m.sin(pow_xs)**2-0.5
    den = (1.0+0.001*pow_xs)**2
    return 0.5 - num/den


def lim_restr(val, minimo, maximo):
    if val < minimo:
        return minimo
    if val > maximo:
        return maximo
    return val


if __name__ == '__main__':

    if t_fun == 1:
        Fun = fun3
    elif t_fun == 2:
        Fun =schwefel

    for exp in range(len_exper):
        #iniciando bat
        for i in range(dimension):
            l_min[i] = v_min
            l_max[i] = v_max

        for i in range(len_po):
            Q[i] = 0
            for j in range(dimension):
                rnd = np.random.uniform(0, 1)
                velocidad[i][j] = 0.0
                po_sol[i][j] = l_min[j] + (l_max[j] - l_min[j]) * rnd
            aptitud[i] = Fun(po_sol[i])

        #mejor bat
        i = j = 0
        for i in range(len_po):
            if aptitud[i] < aptitud[j]:
                j = i
        for i in range(dimension):
            mejor[i] = po_sol[j][i]
        f_min = aptitud[j] 

        #mover bat
        S = np.zeros((len_po,dimension)) # poblacion de soluciones 

        for t in range(n_gen):
            for i in range(len_po):
                rnd = np.random.uniform(0, 1)
                Q[i] = Qmin + (Qmax - Qmin) * rnd
                
                for j in range(dimension):
                    velocidad[i][j] = velocidad[i][j] + (po_sol[i][j] - mejor[j]) * Q[i]
                    S[i][j] = po_sol[i][j] + velocidad[i][j]
                    S[i][j] = lim_restr(S[i][j], l_min[j],l_max[j])

                rnd = np.random.random_sample()

                if rnd > r:
                    for j in range(dimension):
                        S[i][j] = mejor[j] + 0.001 * random.gauss(0, 1)
                        S[i][j] = lim_restr(S[i][j], l_min[j],l_max[j])
                        
                f_new = Fun(S[i])
                rnd = np.random.random_sample()

                if (f_new <= aptitud[i]) and (rnd < A):
                    for j in range(dimension):
                        po_sol[i][j] = S[i][j]
                    aptitud[i] = f_new

                if f_new <= f_min:
                    for j in range(dimension):
                        mejor[j] = S[i][j]
                    f_min = f_new

        print("exp:" ,exp," f_min: ",f_min)
