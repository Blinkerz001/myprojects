
import numpy as np
import matplotlib.pyplot as plt
import copy
from matplotlib import cm

#constants
L = 1  #total length
dx = 0.01 # grid spacing
c = 1.0 #speed of wave
dt = 0.5*dx/c #info in the code cant travel faster than the wave
#cfl condition



x = np.arange(0,L+dx, dx) #0,L spaced by dx
y = np.arange(0,L+dx, dx)

xx, yy = np.meshgrid(x,y)

x_points = len(x)
nsteps = 500


# amp = np.sin(2*np.pi*x/L)
amp = np.zeros((x_points, x_points, 3))
#n-1, n, n+1 for finite difference

w = 0.1 # gaussian width
xc = 0.5  #gaussian centre


amp[:,:,  0] = np.exp(-(xx-xc)**2/(w**2))*np.exp(-(yy-xc)**2/(w**2)) #initial conditions of 2d gaussian pulse



initial = copy.deepcopy(amp[:,:,0]) # copy of initial conditions

amp[1:-1, 1:-1 , 1] = amp[1:-1, 1:-1 ,0] + 0.5*c**2 *(dt/dx)**2 * (amp[2:,1:-1,0] + amp[:-2,1:-1, 0] - 2*amp[1:-1,1:-1,0])+ 0.5*c**2 *(dt/dx)**2 * (amp[1:-1,:-2,0] + amp[1:-1,2:,0] - 2*amp[1:-1,1:-1,0])

#fixed boundary conditions

#try slight wobbles in boundary.

for i in range(0,nsteps):
   # [1:-1] excludes boundary points
    amp[1:-1,1:-1,2] = -amp[1:-1,1:-1,0] + 2*amp[1:-1,1:-1,1] \
        + c**2*(amp[:-2,1:-1, 1]+amp[2:,1:-1,1]-2.*amp[1:-1,1:-1,1])*(dt**2/dx**2)\
        + c**2*(amp[1:-1,:-2, 1]+amp[1:-1,2:,1]-2.*amp[1:-1,1:-1,1])*(dt**2/dx**2)
        
        
    #amp[:,0,2] = 0.1* amp[:,0,2] #xedge is dampened
    #amp[:,-1,2] = 0.1* amp[:,-1,2] # xedge is dampened
    #amp[0,:,2] = 0.1* amp[0,:,2] # yedge is dampened
    #amp[-1,:,2] = 0.1* amp[-1,:,2] #yedge is dampened
    
    


    amp[:,:,0] =  amp[:,:,1]
    amp[:,:,1] =  amp[:,:,2]
    
    if i % 5 ==0: # plot every 5th frame
        fig =  plt.figure(1)
        fig.clf()
        ax = fig.add_subplot(projection = '3d')
        ax.plot_surface(xx,yy , amp[:,:,2], rstride = 1,  cstride = 1, cmap = cm.coolwarm)
        ax.set_zlim3d(-.25 , 1)
  
        time = round(dt*i , 2)
        plt.title(f't = {time}')
        plt.show()
        plt.pause(0.01)