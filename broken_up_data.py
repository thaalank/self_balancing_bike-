import numpy as np 
import matplotlib.pyplot as plt

data=np.genfromtxt('25000_step.csv', delimiter=',')

xvalues=data[:,][:,0]
yvalues=data[:,][:,1]
omegavalues=data[:,][:,2]
omegadtvalues=data[:,][:,3]
thetavalues=data[:,][:,4]
thetadtvalues=data[:,][:,5]
psivalues=data[:,][:,6]

print (thetavalues[1])
