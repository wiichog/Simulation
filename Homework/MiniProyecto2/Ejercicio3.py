# -*- coding: utf-8 -*-
"""
Created on Mon Sep 05 18:30:30 2016

@author: wiichog
"""
import random
import math

def e(lam): return -(1/lam)*math.log(random.random(),math.exp(1))
    
def normal(M,sigma):
    while True:
        y1 = e(1)
        y2 = e(1)
        if (y2 - (y1-1)**2)/2 > 0:
            u = random.random()
            if u <= 0.5:
                return M + sigma*y1
            else:
                return M - sigma*y1
    
def uniform(a,b):
    x = random.random()
    r = (b-a)*x+a
    return r  
    
def valuePN(V,t):
    r = 0
    for i in range(0,len(V)):
        r += V[i]/((1+t)**i)
    return r
    
t= 0.10
VNHotel = VnComercial = 0
numero = 10000
for i in range(0,numero):
    Lista1 = [-800, normal(-800,50), normal(-800,100), normal(-700,150), normal(300,200), normal(400,200), normal(500,200), uniform(200,8440)]
    Lista2 = [-900,normal(-600,50),normal(-200,50),normal(-600,100),normal(250,150),normal(350,150),normal(400,150),uniform(1600,6000)]     
    VNHotel = VNHotel + valuePN(Lista1,t)
    VnComercial = VnComercial + valuePN(Lista2,t)


print ("El valor neto del Hotel es de: "+ str(VNHotel/numero))
print ("El valor neto del Centro Comercial es de: "+ str(VnComercial/numero))

if VnComercial > VNHotel:
    print ("Se deberia de invertir en el centro comercial")
else:
    print("Se deberia de invetir en el hotel")
        
