# -*- coding: utf-8 -*-
"""
Editor de Spyder
Este es un archivo temporal
"""
import matplotlib.pyplot as plt
import random

class Point:#Creamos una clase que maneje el punto
    def __init__(self,x,y):#le mandamos los parametros x y y
        self.x = x#damos valor al parametro
        self.y = y#damos valor al parametro
        
def f1(p): return Point(p.x/2, p.y/2)#primer funciones
def f2(p): return Point(p.x/2 + 0.5, p.y/2)#segunda funcion
def f3(p): return Point(p.x/2 + 0.25, p.y/2 + 0.5)#tercera funcion

p = Point#creamos un objeto
p.x=random.random()#damos valores al objeto para su parametro x
p.y= random.random()#damos valores al objeto para su parametro y
numbers = []#creamos un array para guardar resultados
numbers.append(p)#guardamos en la primera posicion del array el objeto p

for i in range(100000):
    rand = random.randint(1,3)#creamos un random entre 1 y 3
    if rand ==1:#si da 1 evaluamos la primera funcion
        numbers.append(f1(numbers[i-1]))#guardamos el evaluo en el array
    elif rand == 2:#si da 2 evaluaos la segunda funcion
        numbers.append(f2(numbers[i-1]))#guardamos el evaluo en el array
    elif rand == 3:#si da 3 evaluamos la tercera funcion
        numbers.append(f3(numbers[i-1]))#guardamos el evaluo en el array
    
xlist = [points.x for points in numbers]#sacamos las x de los objetos en el vector
ylist = [points.y for points in numbers]#sacamos las y de los objetos en ele vector

plt.plot(xlist, ylist, ".", ms=0.1)#ploteamos x,y, con un . y ms de 0.1