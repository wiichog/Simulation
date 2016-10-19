# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 14:51:22 2016

@author: wiichog
"""

import pygame
import random
import math

def FuzzyAngle(ballAngle,dudeAngle,FuzzyStatement):
    if(ballAngle>dudeAngle and FuzzyStatement=="MuyLejos"):
        return dudeAngle + 10
    elif(ballAngle<dudeAngle and FuzzyStatement=="MuyLejos"):
        return dudeAngle - 10
    elif(ballAngle>dudeAngle and FuzzyStatement=="MedioLejos"):
        return dudeAngle + 5
    elif(ballAngle<dudeAngle and FuzzyStatement=="MedioLejos"):
        return dudeAngle - 5
    elif(ballAngle>dudeAngle and FuzzyStatement=="Cerca"):
        return (dudeAngle + 1)
    elif(ballAngle<dudeAngle and FuzzyStatement=="Cerca"):
        return dudeAngle - 1
    
def Draw(done,ballImage,dudeImage,ballX,ballY,dudeX,dudeY):
    while True:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                False
        screen.fill(Green)
        screen.blit(ballImage,(ballX,ballY))
        screen.blit(dudeImage,(dudeX,dudeY))
        pygame.display.flip()
    
def MoveDude(done,ballImage,dudeImage,ballX,ballY,dudeX,dudeY,Angle,FuzzyStatement):
    if(FuzzyStatement == "MuyLejos"):
        for i in range(10):
            dudeX = dudeX + 1
            dudeY = dudeY + 1
            print "Angle ", Angle
            print  "InitposC X ", dudeX," InitposY ", dudeY
            print "posicion X " ,abs(dudeX*math.cos(Angle)), " posicion y ",abs(dudeY*math.sin(Angle))
            Draw(done,ballImage,dudeImage,ballX,ballY,abs(dudeX*math.cos(Angle)),abs(dudeY*math.sin(Angle)))
    

    
    
    
#This is the colors that we are gonna use
Black = (  0,  0,  0)
White = (255,255,255)
Blue  = (  0,  0,255)
Green = ( 34,139, 34)
Red   = (255,  0,  0)
#size keeps the size of the screen we need
size = [400,300]
#We throw some random number between 400 and 300 to have the figure inside the screen
ballXInitPos = random.randint(0,400)
dudeXInitPos = random.randint(0,400)
ballYInitPos = random.randint(0,300)
dudeYInitPos = random.randint(0,300)
#we throw another random between 0 and 360 for the angle of the dude
dudeAngleInit = random.randint(0,360)
#we calculate the distance between the ball and the dude
Distance = round(math.sqrt((ballXInitPos-dudeXInitPos)**2+(ballYInitPos-dudeYInitPos)**2),2)
#we calculate the angle to have the first condition if to have the complement of the angle and the else is to calculate the normal angle
if(ballYInitPos>dudeYInitPos):
    Angulo = round(360 - abs(math.degrees(math.atan2((ballYInitPos-dudeYInitPos),(ballXInitPos-dudeXInitPos)))),0)
else:
    Angulo = round(abs(math.degrees(math.atan2((ballYInitPos-dudeYInitPos),(ballXInitPos-dudeXInitPos)))),0)


        
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Juan Luis Garcia 14189")
#Vamos a utilizar done y clock para controlar cuando el usuario quiera cerrar la pantalla
done = False
clock = pygame.time.Clock()
ballImage = pygame.image.load('pelota.png')
dudeImage = pygame.image.load('personaje.png')


Draw(done,ballImage,dudeImage,ballXInitPos,ballYInitPos,dudeXInitPos,dudeYInitPos)
MoveDude(done,ballImage,dudeImage,ballXInitPos,ballYInitPos,dudeXInitPos,dudeYInitPos,dudeAngleInit,"MuyLejos")

if(abs(Angulo-dudeAngleInit)>100):
    dudeAngleInit=FuzzyAngle(Angulo,dudeAngleInit,"MuyLejos")
elif(abs(Angulo-dudeAngleInit)>=50 and abs(Angulo-dudeAngleInit)<=100):
    dudeAngleInit=FuzzyAngle(Angulo,dudeAngleInit,"MedioLejos")
elif(abs(Angulo-dudeAngleInit)>=0 and abs(Angulo-dudeAngleInit)<=50):
    dudeAngleInit=FuzzyAngle(Angulo,dudeAngleInit,"Cerca")
   
    
pygame.quit()