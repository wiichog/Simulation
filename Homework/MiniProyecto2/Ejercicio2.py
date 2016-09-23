# -*- coding: utf-8 -*-
"""
Created on Tue Sep 06 17:01:32 2016

@author: wiichog
"""
import random
from matplotlib.pylab import hist, show
import numpy as np

def Acumulada(distribucion,N):
    if(sum(distribucion)==1):#miramos que la distribucion sume
        Intervalo = []#si si suma una creamos una lista en la cual meteremos los intervlaos
        for i in distribucion:
            if len(Intervalo) != 0:
                Intervalo.append(i+Intervalo[-1])#ingresamos la suma del anterior
            else:
                Intervalo.append(i) #ingresamos la posicion
            x = np.random.random(N) 
            c = [0]*len(Intervalo) #creamos un array lleno de ceros para que lleve el contador de cada itnerrvalo
            for xn in x:
                for i in range(0,len(Intervalo)):
                    if xn < Intervalo[i] and xn > Intervalo[i-1]:
                        c[i]+=1
                    if i == 0 and xn < Intervalo[0]:
                        c[i]+=1

        print c
        hist(c)#graficamos el vector
        show()#mostramos el histograma
        
Lista1 = [0.5,0.15,0.15,0.20]
Acumulada(Lista1,100)
