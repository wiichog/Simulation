# -*- coding: utf-8 -*-
"""
Created on Tue Sep 06 11:43:18 2016

@author: wiichog
"""
import random

def CompraPeriodicos(Repiciones,NumeroPeriodicos,NumeroPeriodicosTotal):
    x = random.random()
    CompraInicial = -(1.5*NumeroPeriodicos)
    if (x<0.30):
        CompraInicial = CompraInicial + (2.5*CompraInicial)
    elif (0.30<x<=0.70):
        CompraInicial = CompraInicial + (2.5*CompraInicial)
        CompraInicial = CompraInicial + .50(NumeroPeriodicosTotal-NumeroPeriodicos)#reembolso
    elif (x>0.70):
        CompraInicial = CompraInicial + (2.5*CompraInicial)
        CompraInicial = CompraInicial + .50(NumeroPeriodicosTotal-NumeroPeriodicos)#reembolso
    return CompraInicial

