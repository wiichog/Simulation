# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 07:13:56 2016

@author: wiichog
"""
import random
from math import *

def Poison(S, Lambda):
    return S - (1/Lambda) * log(random.random())

#Ya que es homogeneo lambda del proceso de poisson es igual a lambda
def exponencial(Lambda): return -(1.0/Lambda)*log(random.random())
    
def ServidorDisponible(Array,Valor):#Aqui vamos a encontrar los NumeroDeServidores que esten disponible
    for i in range(len(Array)):
        if(Array[i]==Valor):
            return i
    return -1
    
b = 6000/float(60) #lambdapp
NumeroDeSolicitudes = b/float(10)
colaPendientes = []
    
NumeroDeServidores=10
if(NumeroDeServidores==1):
    NumeroDeSolicitudes = b
    
inf = float('Inf')
t = Na = Nd = n = 0
ta = exponencial(b)#primer tiempo de llegada
td = [inf]*NumeroDeServidores #cantidad de NumeroDeServidores
tdind = [0]*NumeroDeServidores#vector con indices
T = 3600#tiempo limite
A = []#inicio atencion
D = []#final atencion
constante = 0
tx = []
#indTemporal = 0
#No se que diablos paso aqui




while ((t <= T) or (n > 0)):
    if((ta<= min(td)) and (ta<= T)):#CasoNumero1
        t = ta#tiempo va a ser igual al tiempo generado
        Na += 1#aumentamos
        n+= 1#aumentamos
        ta = t + exponencial(b) #Generamos un nuevo tiempo
        if(ServidorDisponible(td,inf)!= -1):
            indTemporal = ServidorDisponible(td,inf) #Vamos a guarda la posicion en donde se encuentra el
            #Servidor disponible
            Y = exponencial(NumeroDeSolicitudes)#Generamos Y
            td[indTemporal] = Y + t #Aqui ocupamos el servidor disponible
            tx.append(Y) #agregamos cuanto tiempo estuvo ocupado el servidor
            tdind[indTemporal] = Na
    A.append(t)#Tiempo de llegada de la solicitud
    D.append(0)#Tiempo de salida
    if(min(td)< ta and min(td)<=T):#CasoNumero2
        t = min(td)
        Nd+= 1
        indtemporal = ServidorDisponible(td,t)
        D[tdind[indtemporal]-1] = t#como ya ingreso, se guarda la hora de salida
        if(n<=len(td)):
            td[indtemporal] = inf
        else:
            Y = exponencial(NumeroDeSolicitudes)#Generamos Y
            tx.append(Y)   #agregamos cuanto tiempo estuvo ocupado el servidor
            td[indtemporal] = t + Y#Aqui ocupamos el servidor disponible
            tdind[indtemporal] = max(tdind)+1#Guardamos el tiempo maximo 
            if ((td[indtemporal] - ta)>0):#Aqui miramos si el servicio se acabo o no
                encola = td[indtemporal] - ta #si no se termino lo guardamos en la cola
                colaPendientes.append(encola)#lo guardamos en la cola
        n+=-1
    if((min(ta,min(td))) > T and (n >0)):
        t = min(td)
        Nd+=1
        if n <= len(td):#se queda vacio 
            td[indtemporal] = inf
        else:
            #aun hay en cola, entonces nuevo tiempo
            Y = exponencial(NumeroDeSolicitudes)
            td[indtemporal] = t + Y
            tx.append(Y)            
            tdind[indtemporal] = max(tdind)+1
        n += -1  
    elif ((min(ta,min(td))) > T and (n == 0)): #Caso 4
        break
        Tp = max(t-T,0)
        
    
prom = []
for i in range(len(A)):
    dif = D[i] - A[i]
    prom.append(dif)

prome = sum(prom)/len(prom)
promC = sum(colaPendientes)/len(colaPendientes)
    
print "Numero de Ocurrencias ",Na/NumeroDeServidores
print "Tiempo que servidor estuvo ocupado: ",sum(tx)/NumeroDeServidores
print "Tiempo que estuvo desocupado: ",(sum(tx)-T)
print "Tiempo en colo: ",sum(colaPendientes)
print "En promedio, tiempo que estuvo solicitud en colo: ",promC
print "En promedio, solicitud en colo: ",len(colaPendientes)/sum(colaPendientes)
print "Las solicitudes en cola: ",len(colaPendientes)






            



