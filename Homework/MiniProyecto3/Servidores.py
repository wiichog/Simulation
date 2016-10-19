import random
import math

def PoissonHomogeneo(s,Lambda): return s - (1/Lambda)*math.log(random.random())
def Exponencial(Lambda):  return -float((1./Lambda)*math.log(random.random()))
def sigEvento2(s, lamda): return s-(1/lamda)*math.log(random.random())

def Gorilla():
    inf = float('inf')
    TasaXSegundos = 2400./60
    t = 0                               #tiempo inicial
    T = 3600                            #tiempo final
    A = []                              # contiene los tiempos de llegada
    D = []                              # contiene los tiempos de salida
    Na = 0                              # numero de llegadas
    Nd = 0                              # numero de salidas
    ta = 0                              # tiempo de llegada
    td = 0                              # tiempo de salida
    n = 0                               # numero de procesos en el servidor
    Tp= 0                            
    while t<=T:
        if(ta<=td and ta<=T):
            t = ta
            Na = Na +1
            n = n+1
            ta = sigEvento2(t,TasaXSegundos)
            if n==1:
                Y = Exponencial(TasaXSegundos)
                td = t + Y
            A.append(t)
        elif(td<ta and td<=T):
            t =td
            n =n -1
            Nd = Nd +1
            if n==0:
                td = inf
            else:
                Y = Exponencial(TasaXSegundos)
                td = t + Y
                t = td
            D.append(t)
        elif(min(ta,td)>T and n>0):
            t =td
            n = n-1
            Nd = Nd +1
            if n>0:
                Y = Exponencial(TasaXSegundos)
                td = t + Y
                t = td
            D.append(t)
        elif(min(ta,td)>T and n==0):
            Tp = max(t - T,0)
            break
    
    
    print "ESTE ES EL RESULTADO PARA EL SERVIDOR GORILLA"
    print "El numero de llegadas al servidor fue de: ", Na
    print "El tiempo que estuvo ocupado el servidor fue: ", td
    print "El tiempo que estuvo libre el servidor fue de: ", td - ta
    print "El tiempo estuvieron las solicitudes en cola", 
    

def simulacionHormigas(num):
    t = 0                               # tiempo inicial
    T = 3600                            # tiempo final
    A = []                              # contiene los tiempos de llegada
    D = []                              # contiene los tiempos de salida
    S = []                              # contiene los tiempos de sevicio
    Na = 0                              # numero de llegadas
    Nd = 0                              # numero de salidas
    ta = Exponencial(40)             # tiempo de la siguiente llegada
    tp = 0                              # tiempo extra de servicio
    td = [100000]*num                   # tiempo de salida
    n = 0                               # numero de procesos en el servidor
    PS = [0]*num                        # Procesos servidores
    SS = [0]*(1+num)                    # (solicitudes en el sistema, sol. atendida serv. 1, ..., serv n)
    
    while t < T or SS[0] > 0:           # mientras no se ha llegado al final o haya +1 solicitud en cola 
        m = min(td)
        minimo = td.index(m)            # se busca el tiempo minimo de las salidas
        
        if ta < td[minimo] and ta< T:   # si la ultima llegada es antes del cierre y aun se puede atender
            t = ta                      # se mueve al tiempo de llegada
            Na = Na +  1                # se aumenta el contador de llegadas
            ta = ta + Exponencial(40)# se actualiza el nuevo tiempo de llegada con una var. exp.
            A.append(t)                   # se agrega el tiempo actual (de llegada) a el registro de llegadas A
            
            if SS[0] == 0:              # si no hay solicitudes en cola
                S.append(t)             # se agrega el tiempo se servicio de la solicitud
                SS[0] += 1              # contador de solicitudes en cola aumenta
                SS[1] = Na              # se coloca la llegada en el primer servidor
                td[0] = t + Exponencial(10) # se calcula el nuevo tiempo de salida como var. exp.
                
            elif SS[0] < num:            # si aun hay servidores para atender las solicitudes
                notBusy = SS.index(0) - 1 # se busca un servidor disponible (se resta el espacio del contador de solicitudes siendo atendidas)
                S.append(t)             # se agrega el tiempo se servicio de la solicitud
                SS[0] += 1              # contador de solicitudes en cola aumenta
                SS[notBusy+1] = Na      # se agrega la llegada al servidor disponible
                td[notBusy] = t + Exponencial(10) # se calcula el nuevo tiempo de salida como var. exp.
            
            else:                       # si no hay disponibilidad de servidor
                SS[0] += 1              # se agrega a la cola
            
        else:                           # si lo siguiente es una salida o ya se llegó al tiempo de cierre
            t = td[minimo]              # tiempo actual es el minimo tiempo de salida
            PS[minimo] += 1             # se agrega el proceso al contador de procs. del servidor
            D.append(t)                 # se agrega el tiempo actual a las salidas
            
            if SS[0] <= num:            # si aun hay servidores para atender las solicitudes
                SS[0] -= 1              # se retira la solicitud de la cola
                td[minimo] = 100000     # no se conoce la siguiente salida, por lo que es un tiempo muy grande
                SS[minimo + 1] = 0      # se retira la solicitud del servidor que la atendió
            
            else:                       # si no hay disponibilidad  (sigue en cola)
                SS[0] *= -1
                siguiente = max(SS)+1   # la siguiente sol. en entrar es el máximo de los que están siendo atendidos
                SS[0] *= -1
                S.append(t)             # se agrega el tiempo actual al de espera                
                SS[0] -= 1              # se retira la solicitud de la cola
                td[minimo] = t + Exponencial(10) # se calcula el nuevo tiempo de salida como var. exp.
                SS[minimo + 1] = siguiente # entra la siguiente solicitud a un servidor disponible
            
    print "Solicitudes atendididas por cada servidor:"
    print "-----------------------------------------"
    for i in range (len(PS)):
        print "\t"+"Servidor "+str(i+1)+":", PS[i], "solicitudes."
    print "-----------------------------------------"
    print "Tiempo total: ", sum(td), "segundos."
    print "Solicitudes atendidas: ", Na
    tot=0
    for k in range(len(A)):
        resta=S[k]-A[k]
        tot=tot+resta
    prom = tot/len(A)
    print "Ultima llegada:", A[-1], "s."
    print "Ultima salida:", D[-1], "s."
    print "Promedio de tiempo en cola: ", prom, "segundos."


    
simulacionHormigas(16)
print ""
print ""
print ""
Gorilla()
