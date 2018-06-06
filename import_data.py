import numpy as np 
import matplotlib.pyplot as plt 

data=np.genfromtxt('25000_step.csv', delimiter=',')

xvalues=data[:,][:,0]
yvalues=data[:,][:,1]

print xvalues[2]


