# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 14:25:11 2016

@author: wiichog
"""
import random
from math import *

def g(x): return e**(-(x**2))#declaramos la funcion original
def f(x): return 2*(g((1/x)-1)/(x**2))#ponemos la funcion con montecarlo para evaluarlo en 1/x -1

suma =0#variable para sumatoria
for i in range(1,100):
    number = random.random()
    number1 = f(number)#enviamos a la funcion el numero aleatorio
    suma = suma + number1#lo sumamas
    promedio = suma /i#hacemos un promedio
print promedio#imprimimos el promedio

suma =0#variable para sumatoria
for i in range(1,10000):
    number = random.random()
    number1 = f(number)#enviamos a la funcion el numero aleatorio
    suma = suma + number1#lo sumamas
    promedio = suma /i#hacemos un promedio
print promedio#imprimimos el promedio

suma =0#variable para sumatoria
for i in range(1,100000):
    number = random.random()
    number1 = f(number)#enviamos a la funcion el numero aleatorio
    suma = suma + number1#lo sumamas
    promedio = suma /i#hacemos un promedio
print promedio#imprimimos el promedio