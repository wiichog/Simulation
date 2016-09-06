# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 07:41:43 2016

@author: wiichog
"""
from matplotlib.pylab import hist, show
import random
import time
def f(x): return ((5**5)*x)%((2**35)-1)#Primer Generador
def g(x): return ((7**5)*x)%((2**31)-1)#Segundo Generados
def h(x): return random.random()#Tercer Generador

print "Primer Generador para 100 iteraciones"
numbers = []
Xn = time.clock()#Numero Aleatorio con el reloj del sistema
for i in range(100):
    Xn1 = f(Xn)#evaluamos el numero aleatorio en el primer generador
    numbers.append(Xn1/((2**35)-2))#ingresamos lo que regreso el generador dividio el numero mas grande -1 
    Xn = Xn1#cambiamos de numero
hist(numbers)#graficamos el vector
show()#mostramos el histograma

print "Primer Generador para 10,000 iteraciones"
numbers = []#vaciamos el vector
Xn = time.clock()#numero aleatorio con el reloj
for i in range(10000):
    Xn1 = f(Xn)#evaluamos el numero aleatorio en el primer generador
    numbers.append(Xn1/((2**35)-2))#ingresamos lo que regreso el generador dividio el numero mas grande -1 
    Xn = Xn1#cambiamos de numero
hist(numbers)#graficamos el vector
show()#mostramos el histograma

print "Primer Generador para 100,000 iteraciones"
numbers = []#vaciamos el vector
Xn = time.clock()
for i in range(100000):
    Xn1 = f(Xn)#evaluamos el numero aleatorio en el primer generador
    numbers.append(Xn1/((2**35)-2))#ingresamos lo que regreso el generador dividio el numero mas grande -1 
    Xn = Xn1#cambiamos de numero
hist(numbers)#graficamos el vector
show()#mostramos el histograma

print "Segundo Generador para 100 iteraciones"
numbers = []#vaciamos el vector
Xn = time.clock()
for i in range(100):
    Xn1 = g(Xn)#evaluamos el numero aleatorio en el segundo generador
    numbers.append(Xn1/((2**31)-2))#ingresamos lo que regreso el generador dividio el numero mas grande -1 
    Xn = Xn1#cambiamos de numero
hist(numbers)#graficamos el vector
show()#mostramos el histograma

print "Segundo Generador para 10,000 iteraciones"
numbers = []#vaciamos el vector
Xn = time.clock()
for i in range(10000):
    Xn1 = g(Xn)#evaluamos el numero aleatorio en el segundo generador
    numbers.append(Xn1/((2**31)-2))#ingresamos lo que regreso el generador dividio el numero mas grande -1 
    Xn = Xn1#cambiamos de numero
hist(numbers)#graficamos el vector
show()#mostramos el histograma

print "Segundo Generador para 100,000 iteraciones"
numbers = []#vaciamos el vector
Xn = time.clock()
for i in range(100000):
    Xn1 = g(Xn)#evaluamos el numero aleatorio en el segundo generador
    numbers.append(Xn1/((2**31)-2))#ingresamos lo que regreso el generador dividio el numero mas grande -1 
    Xn = Xn1#cambiamos de numero
hist(numbers)#graficamos el vector
show()#mostramos el histograma