# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 21:16:08 2020

@author: BerkeAyevi
"""

import numpy as np
import matplotlib.pyplot as plt


pi = np.pi

def f(x):
    y1= 0.0
    x0= float(x)
    a0 = (np.exp(pi)-np.exp(-pi)) / pi
    
    for n in range(1,100):
        ancosnx= ((-1)**n) * (1/((n**2)+1)) * np.cos(n * x0)
        bnsinnx=  (-1*n)* ((-1)**n) * 1/((n**2)+1) * np.sin(n * x0)
        
        y0 = (1/pi)*(np.exp(pi)-np.exp(-pi))* (ancosnx +bnsinnx)
        y1 = y1 + y0
        
    y = (a0/2)+ y1
    return y

x =np.linspace(-pi,pi,100)
y =[]
e = []
for i in x:
    eq1= f(i)
    eq2 = np.exp(i)    
    y.append(eq1)
    e.append(eq2)    


fig, ax = plt.subplots()
print(y)

ax.plot(x,e)
ax.plot(x,y)

    
    
        
        

