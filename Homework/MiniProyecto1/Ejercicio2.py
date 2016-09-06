#Universidad del Valle de Guatemala
#Ejericicio No.2
#modulos a usar : random y matplotlib
import random 
import matplotlib.pyplot as draw



def dibujar(x,y,n):
    #10000 iteraciones
    while (n <= 10000):
        # se obtiene un valor aletatorio
        valor = random.random()
        # se busca que este dentro de las siguientesfunciones/validaciones
        
        #validacion F1
        if (valor<=0.85):
            # valor dentro del 85% 
            x = x*0.85 + y*0.04
            y = x*-0.04+ y*0.85 + 1.6
            
        #validacion F2
        elif (0.85<valor<=0.92):
            #valor dentro del 7% inferior
            x = -0.15*x + 0.28*y + 0.0
            y = x*0.26 + y*0.24 + 0.44
            
        #Validacion F3
        elif (0.92<valor<=0.99):
            #valor dentro del 7% superior
            x = x*0.2 + y*-0.26 + 0.0
            y = x*0.23 + y*0.22 + 1.6
        #Validacion F4
        elif (0.99<valor<=1):
            #valor dentro del 1%
            x = x*0.0 + y*0.0
            y = x*0.0 + y*0.16

        #imprime las iteraciones para saber en que punto de la corrida va
        #print n-n%100, '......    .......'                   
        draw.plot(x,y,'.',ms = 1.5) 
        n+=1           
#posiciones inciales        
posx = 1
posy = 1
#contador de iteraciones
cont=1
#ingresa a la funcion
dibujar(posx,posy,cont)
#muestra lo obtenido
draw.show()
	
