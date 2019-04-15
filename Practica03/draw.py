import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import NullFormatter
import sys

otro=open("out", "r")
fname=otro.readline()

f = open("curvas"+fname+".txt", "r")
array=np.loadtxt(f)
x = np.arange(array.shape[0])

plt.plot(x,array[:,0],"red", label="best")
plt.plot(x,array[:,1],"blue", label="off-line")
plt.plot(x,array[:,2],"green", label="on-line")

plt.legend(loc='upper left')
plt.axis([0,array.shape[0], 0.00, 1.00])
plt.grid(True)

plt.savefig(fname+".png")
