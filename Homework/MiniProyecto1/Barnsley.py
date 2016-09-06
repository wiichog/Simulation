# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 18:42:56 2016

@author: wiichog
"""

import matplotlib.pyplot as plt
import random

class Point:#Creamos una clase que maneje el punto
    def __init__(self,x,y):#le mandamos los parametros x y y
        self.x = x#damos valor al parametro
        self.y = y#damos valor al parametro
        
def f1(p): return Point(p.x*0.85 + p.y*0.04, p.x*-0.04 + p.y*0.85 + 1.6)#primera funcion
def f2(p): return Point(-0.15*p.x + 0.28*p.y , 0.26*p.x + p.y*0.24 + 0.44)#segunda funcion
def f3(p): return Point(p.x*0.2 + p.y*-0.26, p.x*0.23 + p.y*0.22 + 1.6)#tercera funcion
def f4(p): return Point(0,p.y*0.16)#cuarta funcion
    
p = Point#creamos un objeto de punto
p.x=random.random()#damos valores random a x
p.y= random.random()#damos valores random a y
numbers = []#creamos un array
numbers.append(p)#ingresamos a p en la primera posicion del array

for i in range(1,100000):
    rand = random.random()#generamos un random de 0 a 1
    ran = round(rand,2)# lo rendondeamos a 2 cifras
    if rand >= 0 and rand <= 0.85:#si el random cae entre 0 y 0.85 evaluamos la primera funcion
        numbers.append(f1(numbers[i-1]))#agregamos el evaluo al array
    elif rand >= 0.85 and rand <= 0.92:#si el random cae entre 0.85 y 0.92 con 0.07 de posibilidad
        numbers.append(f2(numbers[i-1]))#evaluamos la segunda funcion
    elif rand >= 0.92 and rand <= 0.99:#si el random cae entre 0.92 y 0.99 con 0.07 de posibilidad
        numbers.append(f3(numbers[i-1]))#evaluamos la tercera funcion
    elif rand >= 0.99 and rand <= 1:#si el random cae entre 0.99 y 1 con posibilidad de 0.01 
        numbers.append(f4(numbers[i-1]))#evaluamos la ultima funcion
     
xlist = [points.x for points in numbers]#obtenemos las x de los objetos en el array
ylist = [points.y for points in numbers]#obtenemos las y de los objetos del array

plt.plot(xlist, ylist, ".", ms=0.1)#graficamos