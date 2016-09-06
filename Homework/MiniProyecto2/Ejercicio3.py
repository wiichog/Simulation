# -*- coding: utf-8 -*-
"""
Created on Mon Sep 05 18:30:30 2016

@author: wiichog
"""
import random
from math import *

def Normal(M,Sig):#esti es para calcular una distribucion normal
    while True:
        Y1 = random.random()#generamos aleatorio
        Y2 = random.random()#generamos aleatorios
        if (Y2-((Y1-1)**2))/2 >0:#calculamos una exponencial
            U = random.random()#calculamos otro random
            if U<= 0.05:#si ese random esta por debajo de la media
                return M + (Sig*Y1)
            else:
                return M - (Sig*Y1)

def e(X, lam): return -(1/lam)*(ln(X))#definimos para la exponencial
    
def uniforme(a,b):#deifinimos para la uniforme
    x = random.random()#declaramos random
    r = (b-a)*(x+a)#calculamos uniforme
    return r#retornamos la r

def ValorNeto(V,t):#funcion del valor neto 
    r = V[0]
    for i in range(len(V)):
        r += V[i]/(1+t)**7
    return r       
        
t= 0.10
NoIteraciones = 10000
VNHotel = VnComercial = 0
Lista1 = [-800,Normal(-800,50),Normal(-800,100),Normal(-700,150),Normal(300,200),Normal(400,200),Normal(500,200),uniforme(200,8440)]
Lista2 = [-900,Normal(-600,50),Normal(-200,50),Normal(-600,100),Normal(250,150),Normal(350,150),Normal(400,150),uniforme(1600,1600)]
for i in range(0,NoIteraciones):          
    VNHotel = ValorNeto(Lista1,t)
    VnComercial = ValorNeto(Lista2,t)


print ("El valor neto del Hotel es de: "+ str(VNHotel))
print ("El valor neto del Centro Comercial es de: "+ str(VnComercial))

if VnComercial > VNHotel:
    print ("Se deberia de invertir en el centro comercial")
else:
    print("Se deberia de invetir en el hotel")
        
