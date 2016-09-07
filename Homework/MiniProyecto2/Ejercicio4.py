# -*- coding: utf-8 -*-
"""
Created on Tue Sep 06 11:43:18 2016

@author: wiichog
"""
import random

def CompraPeriodicos(Tiempo,NumeroPeriodicos,NumeroPeriodicosTotal):
    CompraInicial = -(1.5*NumeroPeriodicos*Tiempo)#Compra Inicial de Periodicos    
    for i in range(0,Tiempo):
        x = random.random()
        if (x<0.30):#Para probalbilidad debajo de 30% compra de 11 periodicos
            CompraInicial = CompraInicial + 2.5*(NumeroPeriodicos)#Suma de ganancia
            if (NumeroPeriodicos != 9):
                CompraInicial = CompraInicial - 2*(NumeroPeriodicos-9)
        elif (0.30<x<=0.70):#compra de 10 periodicos
            CompraInicial = CompraInicial + 2.5*(NumeroPeriodicos)#Suma de ganancia
            CompraInicial = CompraInicial + 0.50*(NumeroPeriodicosTotal-NumeroPeriodicos)#reembolso
            if (NumeroPeriodicos==11):
                CompraInicial = CompraInicial - 2 #Ya que compramos uno mas le restamos 2 para que 2.50-2 = .5 me quedan .5 a mi devuelvo 2
        else:#compra de 9 periodicos
            CompraInicial = CompraInicial + 2.5*(NumeroPeriodicos)#Suma de ganancia
            CompraInicial = CompraInicial + 0.50*(NumeroPeriodicosTotal-NumeroPeriodicos)#reembolso
            
    return CompraInicial
print ("")
for i in range(9,12):
    print ("La ganancia para " + str(i) + " periodicos es "+ str(CompraPeriodicos(30,i,11)) + " esto es para 1 mes")
    print ("La ganancia para " + str(i) + " periodicos es "+ str(CompraPeriodicos(365,i,11)) + " esto es para 1 año")
    print ("La ganancia para " + str(i) + " periodicos es "+ str(CompraPeriodicos(3650,i,11)) + " esto es para 10 años")
    if (i == 9): print ("")
    if (i == 10): print ("")
    if (i == 11): print ("")