from visual import *

bike=frame()

wheelone= ring(frame=bike, pos=(1,1,1), axis=(1,0,0), radius=0.3, thickness=0.041)

wheeltwo= ring(frame=bike, pos=(1,1,2), axis=(1,0,0), radius=0.3, thickness=0.041)

horizontalbody= cylinder(frame=bike, pos=(1,1.3,1), axis=(0,0,1), radius=.04)

verticalbody= cylinder(frame=bike, pos=(1,1.3,1), axis=(0,.4,0), radius=.04)

handle= cylinder(frame=bike, pos=(.8,1.7,1), axis=(.4,0,0), radius=.04)

floor = box(pos=(0,0,0), length=100, height=.01, width=100, color=color.gray(0.5))

insidepath=ring(pos=(0,0,0), axis=(0,1,0), radius=30, thickness=.2)

outsidepath=ring(pos=(0,0,0), axis=(0,1,0), radius=40, thickness=.2)

start=text(text='Start', pos= (0,0,35), align='center', depth=.3, axis=(1,0,0),color=color.green)
start.rotate(angle=(-pi/2), axis=(1,0,0))

finish=text(text='Finish', pos= (0,0,-35), align='center', depth=.3, axis=(1,0,0),color=color.red)
finish.rotate(angle=(-pi/2), axis=(1,0,0))

bike.pos=(-1,-.65,0)

bike.velocity = vector(0,0,-50)

deltat = 0.0005
t = 0

feta1=0 #controls tilt of bike
feta2=0 #controls tilt of handlebar
feta3=0 #controls tilt of front wheel
feta4=0 #controls turning angle of entire bike

while t < 3:
    rate(100)
    if bike.pos.z > -35:
        bike.pos = bike.pos + bike.velocity*deltat
        t = t + deltat
        scene.center=bike.pos
    if feta4< (pi/3000):
        feta4= feta4 + ((pi/1000)*deltat)
        t=t+deltat
        bike.rotate(angle=feta4, axis=(0,.001,0))
##    if feta3< (pi/3000):
##       feta3= feta3 + ((pi/1000)*deltat)
##       t=t+deltat
##       wheelone.rotate(angle=feta3, axis=(0,.0001,0))
##    #if feta1 < (pi/4000):
####        feta1= feta1 + ((pi/1000)*deltat)
##        t=t+deltat
##        bike.rotate(angle=feta1, axis=(0,0,.000001))
##    if feta2< (pi/4000):
##        feta2= feta2 + ((pi/1000)*deltat)
##        t= t + deltat
##        handle.rotate(angle=feta2, axis=(0,0,.1) )
       
