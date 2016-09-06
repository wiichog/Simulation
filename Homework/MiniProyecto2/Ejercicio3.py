# -*- coding: utf-8 -*-
"""
Created on Mon Sep 05 18:30:30 2016

@author: wiichog
"""
import random
from math import *

def Normal(M,Sig):#algoritmo dado en clase
    while True:
        Y1 = exp(1)#generamos un random con distribucion exponencial
        Y2 = exp(1)#generamos random con distribucion exponencial
        if (Y2-(Y1-1)**2)/2 > 0:#calculamos una exponencial
            U = random.random()#calculamos otro random
            if U <= 0.5:#si ese random esta por debajo de la media
                return M + Sig*Y1
            else:
                return M - Sig*Y1



def exp(lam): return -(1/lam)*log(random.random())#definimos para la exponencial


    
def uniforme(a,b):#deifinimos para la uniforme
    x = random.random()#declaramos random
    r = (b-a)*x+a#calculamos uniforme
    return r#retornamos la r



def ValorNeto(V,t):#funcion del valor neto 
   r = V[0]
   for i in range(len(V)):
       r = r +  V[i]/((1+t)**i)
   return r   
        
t= 0.10
VNHotel = VnComercial = 0
numero = 10
for i in range(0,numero):
    Lista1 = [-800, Normal(-800,50), Normal(-800,100), Normal(-700,150), Normal(300,200), Normal(400,200), Normal(500,200), uniforme(200,8440)]
    Lista2 = [-900,Normal(-600,50),Normal(-200,50),Normal(-600,100),Normal(250,150),Normal(350,150),Normal(400,150),uniforme(1600,6000)]     
    VNHotel = VNHotel + ValorNeto(Lista1,t)
    VnComercial = VnComercial + ValorNeto(Lista2,t)


print ("El valor neto del Hotel es de: "+ str(VNHotel/numero))
print ("El valor neto del Centro Comercial es de: "+ str(VnComercial/numero))

if VnComercial > VNHotel:
    print ("Se deberia de invertir en el centro comercial")
else:
    print("Se deberia de invetir en el hotel")
        
