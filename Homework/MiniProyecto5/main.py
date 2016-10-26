import pygame
import random
import math

def Draw(done,ballImage,dudeImage,ballX,ballY,dudeX,dudeY,Angle):
        screen.fill(Green)
        screen.blit(ballImage,(ballX,ballY))
        pygame.draw.circle(screen,Red,(dudeX,dudeY),5,0)
        pygame.draw.line(screen,White,(dudeXInitPos,dudeYInitPos),(dudeX+math.cos(math.radians(Angle)),dudeY+360*math.sin(math.radians(-Angle))))
        pygame.draw.line(screen,Red,(390,100),(390,250),10)
        pygame.display.flip()
#def mover():
    
        
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

#This is the colors that we are gonna use
Black = (  0,  0,  0)
White = (255,255,255)
Blue  = (  0,  0,255)
Green = ( 34,139, 34)
Red   = (255,  0,  0)
#size keeps the size of the screen we need
size = [400,300]
#We throw some random number between 400 and 300 to have the figure inside the screen
ballXInitPos = random.randint(0,300)
dudeXInitPos = random.randint(0,300)
ballYInitPos = random.randint(0,200)
dudeYInitPos = random.randint(0,200)
#we throw another random between 0 and 360 for the angle of the dude
dudeAngleInit = random.randint(0,360)
Distance = round(math.sqrt((ballXInitPos-dudeXInitPos)**2+(ballYInitPos-dudeYInitPos)**2),2)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Juan Luis Garcia 14189")
#Vamos a utilizar done y clock para controlar cuando el usuario quiera cerrar la pantalla
done = False
clock = pygame.time.Clock()
ballImage = pygame.image.load('pelota.png')
dudeImage = pygame.image.load('personaje.png')

if(ballYInitPos>dudeYInitPos):
    AngleBallAndDude = round(360 - abs(math.degrees(math.atan2((ballYInitPos-dudeYInitPos),(ballXInitPos-dudeXInitPos)))),0)
else:
    AngleBallAndDude = round(abs(math.degrees(math.atan2((ballYInitPos-dudeYInitPos),(ballXInitPos-dudeXInitPos)))),0)

contador = 0
print "Dude ",dudeAngleInit
print "Ball & Dude ",AngleBallAndDude
while not done:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        while contador != 1:
            while AngleBallAndDude!=dudeAngleInit:
                if(abs(AngleBallAndDude-dudeAngleInit)>100):
                    dudeAngleInit=FuzzyAngle(AngleBallAndDude,dudeAngleInit,"MuyLejos")
                    Draw(done,ballImage,dudeImage,ballXInitPos,ballYInitPos,dudeXInitPos,dudeYInitPos,dudeAngleInit)
                elif(abs(AngleBallAndDude-dudeAngleInit)>=50 and abs(AngleBallAndDude-dudeAngleInit)<=100):
                    dudeAngleInit=FuzzyAngle(AngleBallAndDude,dudeAngleInit,"MedioLejos")
                    Draw(done,ballImage,dudeImage,ballXInitPos,ballYInitPos,dudeXInitPos,dudeYInitPos,dudeAngleInit)
                elif(abs(AngleBallAndDude-dudeAngleInit)>=0 and abs(AngleBallAndDude-dudeAngleInit)<=50):
                    dudeAngleInit=FuzzyAngle(AngleBallAndDude,dudeAngleInit,"Cerca")
                    Draw(done,ballImage,dudeImage,ballXInitPos,ballYInitPos,dudeXInitPos,dudeYInitPos,dudeAngleInit)
            for i in range(int(Distance)):
                Draw(done,ballImage,dudeImage,ballXInitPos,ballYInitPos,dudeXInitPos+int(i*math.cos(math.radians(AngleBallAndDude))),dudeYInitPos+int(i*math.sin(math.radians(-AngleBallAndDude))),dudeAngleInit)
            if(ballYInitPos>450):
                AngleBallAndGoal = round(360-abs(math.degrees(math.atan2((ballYInitPos-450),(ballXInitPos-890)))),0) 
            else:
                AngleBallAndGoal = round(abs(math.degrees(math.atan2((ballYInitPos-450),(ballXInitPos-890)))),0) 
            print "Angulo entre pelota y porteria" , AngleBallAndGoal
            
            contador = contador +1
            
pygame.quit()
