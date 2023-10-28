#!/usr/bin/env python
# coding: utf-8

# In[62]:


import numpy as np
import matplotlib.pyplot as pyplot
import cmath

NumIter = 200
x_size = 20
y_size = 20
delta = 1
T0_top = 1000
T0_bottom = 50
T0_side1 = 40
T0_side2 = 40
T_min_initial = 50
#assume thermally insulated so no heat of the edges is lost.
T_ = []


# In[63]:


colorinterpolation = 50
colorMap = pyplot.cm.jet


###https://www.geeksforgeeks.org/contour-plot-using-matplotlib-python/
#colour function was found from here

X, Y = np.meshgrid(np.arange(0,x_size),np.arange(0,y_size))

Temps = np.zeros((x_size, y_size))
#need to set the initial values


# In[64]:


Temps.fill(T_min_initial) #sets all values to Tmin


# In[97]:


#set bottom row of Temps array = T0_top
Temps[y_size-1] = T0_top
for i in range(0,y_size - 1):
    Temps[i][0] = 40  # sets the left side to 40 units 
for i in range(0,y_size - 1):
    Temps[i][-1] = 40  # sets the right side to 40 units 
    
    


# In[98]:


for k in range(0,NumIter):
    
        for i in range(1,x_size-1, delta):
            for j in range(1,y_size-1, delta):
                Temps[i,j] = (Temps[i+1][j]+Temps[i-1][j]+Temps[i][j+1]+Temps[i][j-1])/4

   


# In[106]:


pyplot.contourf(X,Y,Temps, colorinterpolation,cmap = colorMap)
colorbar = pyplot.colorbar()
pyplot.xlabel("X position")
pyplot.ylabel("Y position")
colorbar.ax.get_yaxis().labelpad = 15
colorbar.ax.set_ylabel('Temperature scale', rotation=270)


# In[103]:


#T_[i] is the temperature matrix for time value i


# In[ ]:




