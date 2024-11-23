
import numpy as np
import matplotlib.pyplot as plt
import copy
from matplotlib import cm

#constants
L = 1  #total length
dx = 0.01 # grid spacing
c = 1.0 #speed of wave
dt = dx/c #info in the code cant travel faster than the wave
#cfl condition



x = np.arange(0,L+dx,dx) #0,L spaced by dx
x_points = len(x)
nsteps = 500


# amp = np.sin(2*np.pi*x/L)
amp = np.zeros((x_points, 3))
#n-1, n, n+1 for finite difference

w = 0.1 # gaussian width
xc = 0.5  #gaussian centre


amp[:, 0] = np.exp(-(x-xc)**2/(w**2)) #initial conditions of gaussian pulse



initial = copy.deepcopy(amp[:,0]) # copy of initial conditions

amp[1:-1 , 1] = amp[1:-1, 0] + 0.5*c**2 *(dt/dx)**2 * (amp[2:,1] + amp[:-2,1] - 2*amp[1:-1,1])
for i in range(0,nsteps):
   # [1:-1] excludes boundary points
    amp[1:-1, 2] = 2*amp[1:-1, 1] - amp[1:-1,0] + c**2 *(dt/dx)**2 * (amp[2:,1] + amp[:-2,1] - 2*amp[1:-1,1])


## this boundary condition simulates the edge being held??
   # amp[1,2] = min(0.01, amp[1,2]) # point is held and can only vibrate 1% of the wave amplitude
    #amp[-1,2] = min(0.01, amp[-1,2])
    #amp[2,2] = min(0.05, amp[2,2]) # point is held and can only vibrate 5% of the wave amplitude
    #amp[-2,2] = min(0.05, amp[-2,2])
    amp[1,2] = 0.1*amp[1,2] # point is held and dampened
    amp[2,2] = 0.2*(amp[2,2]) # point is dampened  - simulates some energy loss
    amp[-2,2] = 0.2*amp[-2,2]
    
    amp[1:-1,0] =  amp[1:-1,1]
    amp[1:-1,1] =  amp[1:-1,2]
    if i % 5 ==0: # plot every 5th frame
        plt.figure(1)
        plt.clf()
        plt.plot(x,amp[:,2])
        plt.plot(x, initial , 'black')
        plt.ylim(-1,1)
        time = round(dt*i , 2)
        plt.title(f't = {time}')
        plt.show()
        plt.pause(0.01)