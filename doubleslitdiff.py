# -*- coding: utf-8 -*-
"""
Created on Sat May 30 17:42:23 2020

@author: BerkeAyevi
"""

import math
import numpy as np
import matplotlib.pyplot as plt

pi= math.pi
def sinc(x):    
    func = ((np.sin(x))**2)/ (x**2)    
    return func
def alfa(a,teta):    
    landa = 589.6*(10**-9) #set landa
    ab = 1/2*b* (2*pi/landa)*np.sin(teta)
    return ab
def beta(b,teta):    
    landa = 589.6*(10**-9) #set landa
    ab = 1/2*b* (2*pi/landa)*np.sin(teta)
    return ab


x= np.linspace(-1*10**-1,1*10**-1,1000)
I0= 1
a = float(input("speration between slitsin mikrom"))*(10**-6)
b= float(input("wide of the slits in mm"))*(10**-3)
I=[]
ty=[]
for i in x:
    angle = i
    Beta = beta(b,angle)
    Alfa = alfa(a,angle)
    result =  4*I0 * (np.cos(Alfa)**2)* (np.sin(Beta)**2)/ Beta**2
    I.append(result)
    ty.append(angle)
plt.figure(figsize=(20,5))
plt.grid(True)    
plt.plot(ty,I)
    