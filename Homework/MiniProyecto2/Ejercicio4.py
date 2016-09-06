# -*- coding: utf-8 -*-
"""
Created on Tue Sep 06 11:43:18 2016

@author: wiichog
"""
import random

def CompraPeriodicos(Tiempo,NumeroPeriodicos,NumeroPeriodicosTotal):
    CompraInicial = -(1.5*NumeroPeriodicos)#Compra Inicial de Periodicos    
    for i in range(0,Tiempo):
        x = random.random()
        if (x<0.30):#Para probalbilidad debajo de 30%
            CompraInicial = CompraInicial + (2.5*NumeroPeriodicos)#Le sumamos la compra inicial 
        elif (0.30<x<=0.70):
            CompraInicial = CompraInicial + (2.5*NumeroPeriodicos)
            CompraInicial = CompraInicial + 0.50*(NumeroPeriodicosTotal-NumeroPeriodicos)#reembolso
        else:
            CompraInicial = CompraInicial + (2.5*NumeroPeriodicos)
            CompraInicial = CompraInicial + 0.50*(NumeroPeriodicosTotal-NumeroPeriodicos)#reembolso
    return CompraInicial

for i in range(9,12):
    print ("La ganancia para " + str(i) + " periodicos es "+ str(CompraPeriodicos(30,i,11)) + " esto es para 1 mes")
    print ("La ganancia para " + str(i) + " periodicos es "+ str(CompraPeriodicos(365,i,11)) + " esto es para 1 año")
    print ("La ganancia para " + str(i) + " periodicos es "+ str(CompraPeriodicos(3650,i,11)) + " esto es para 10 años")
