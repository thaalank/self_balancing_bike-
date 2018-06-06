import numpy as np 
import matplotlib.pyplot as plt
from visual import *

data=np.genfromtxt('finaldata.csv', delimiter=',')

xvalues=data[:,][:,0]
yvalues=data[:,][:,1]
omegavalues=data[:,][:,2]
omegadtvalues=data[:,][:,3]
thetavalues=data[:,][:,4]
thetadtvalues=data[:,][:,5]
psivalues=data[:,][:,6]

bike=frame()

wheelone= ring(frame=bike, pos=(1,1,1), axis=(1,0,0), radius=0.3, thickness=0.041)

wheeltwo= ring(frame=bike, pos=(1,1,2), axis=(1,0,0), radius=0.3, thickness=0.041)

horizontalbody= cylinder(frame=bike, pos=(1,1.3,1), axis=(0,0,1), radius=.04)

verticalbody= cylinder(frame=bike, pos=(1,1.3,1), axis=(0,.4,0), radius=.04)

handle1= cylinder(frame=bike, pos=(1,1.7,1), axis=(-.2,0,0), radius=.04)
handle2= cylinder(frame=bike, pos=(1,1.7,1), axis=(.2,0,0), radius=.04)

floor = box(pos=(0,.65,0), length=25, height=.01, width=200, color=color.gray(0.5))

#insidepath=ring(pos=(0,.65,0), axis=(0,1,0), radius=30, thickness=.2)

#outsidepath=ring(pos=(0,.65,0), axis=(0,1,0), radius=40, thickness=.2)

start=text(text='Start', pos= (0,.65,0), align='center', depth=.3, axis=(1,0,0),color=color.green)
start.rotate(angle=(-pi/2), axis=(1,0,0))

finish=text(text='Finish', pos= (0,.65,-50), align='center', depth=.3, axis=(1,0,0),color=color.red)
finish.rotate(angle=(-pi/2), axis=(1,0,0))

bike.pos=(0,0,0)

t=0             

while t<=25000:
	rate(10)
	bike.pos.x=xvalues[t]
	bike.pos.z=yvalues[t]*-1 #Maybe multiply position values by 10 for emphasis
	scene.center=bike.pos
	bike.rotate(angle=((omegavalues[(t+1)])-(omegavalues[(t)])), axis=(0,0,-.000001))
	handle1.rotate(angle=((thetavalues[t+1])-(thetavalues[t])), axis=(0,1,0))
	handle2.rotate(angle=((thetavalues[t+1])-(thetavalues[t])), axis=(0,1,0))
	wheelone.rotate(angle=((thetavalues[t+1])-(thetavalues[t])), axis=(0,.4,0))
	t=t+1





