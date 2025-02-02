import numpy as np
import matplotlib.pyplot as plt

#defines some constants
a = -9.81
v=10
pos=0

tf=10
step_size=0.25

#create array to plot position, velocity, and acceleration vs time

time=np.arange(0,tf+1,step_size)
position=np.array([])
velocity=np.array([])
aceleration=np.array([])

#oops until final time
for i in time:
    pos=pos+(v*i)+((1/2)*a*(i**2))
    v=v+(a*i)
    position=np.append(position,pos)
    velocity=np.append(velocity,v)
    aceleration=np.append(aceleration,a)

#creates two plots
print(time)
print(position)
plt.scatter(time,position, c='r', label='position')
plt.scatter(time,velocity, c='g', label='velocity')


plt.xlabel('time')
plt.title('motion of simple object')

#show legend
plt.legend()

plt.show()