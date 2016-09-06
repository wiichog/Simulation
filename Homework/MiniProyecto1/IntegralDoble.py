# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 19:29:15 2016

@author: wiichog
"""

from math import *
import time
import random
def g(x): return ((1/x)-1)#evaluamos para la primera de montecarlo
def f(x,y): return (g(x)*e**-(g(x) + g(x)*y))/x**2#evaluamos para la segunda integral
    
suma = 0
print "Iteraciones para 100 corridas"
for i in range(1,100):
    x = random.random()#generamos numero random
    y = random.random()#generamos numero random
    resultado = f(x,y)#evaluamos en los numeros aleatorios
    suma = suma + resultado#lo sumamos
    promedio = suma /i#hacemos un promedio
print promedio

suma = 0
print "Iteraciones para 10,000 corridas"
for i in range(1,10000):
    x = random.random()#generamos numero random
    y = random.random()#generamos numero random
    resultado = f(x,y)#evaluamos en los numeros aleatorios
    suma = suma + resultado#lo sumamos
    promedio = suma /i#hacemos un promedio
print promedio

suma = 0
print "Iteraciones para 1,000,000 corridas"
for i in range(1,1000000):
    x = random.random()#generamos numero random
    y = random.random()#generamos numero random
    resultado = f(x,y)#evaluamos en los numeros aleatorios
    suma = suma + resultado#lo sumamos
    promedio = suma /i#hacemos un promedio
print promedio