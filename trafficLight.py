import pygame
import time
import math

def squatFigure(screen,color,heel,kneeHight,kneeLength,hip):

    pygame.draw.lines(screen,color, False,((570,heel),(600,heel),(kneeLength,kneeHight),(600,hip),(600,hip-35),(540,hip-35),(600,hip-35)),6) # BODY
    pygame.draw.circle(screen, color, (600,hip-60), 12) # HEAD
    pygame.display.update()

    # Clear 
    pygame.draw.lines(screen,BLACK, False,((570,heel),(600,heel),(kneeLength,kneeHight),(600,hip),(600,hip-35),(540,hip-35),(600,hip-35)),6) # BODY
    pygame.draw.circle(screen, BLACK, (600,hip-60), 12) # HEAD

def jumpingJackFigure(screen,color,body, feet, hip, shoulder, hands, hipDist, feetDist, shoulderDist, handDist, elbow, elbowDist):

    pygame.draw.lines(screen,color, False,((body-feetDist,feet),(body-hipDist,hip),(body+hipDist,hip),(body+feetDist,feet)),5) # LEGS
    pygame.draw.lines(screen,color, False,((body,hip),(body,shoulder)),25) # BODY
    pygame.draw.lines(screen,color, False,((body-handDist,hands),(body-elbowDist,elbow),(body-shoulderDist,shoulder),(body+shoulderDist,shoulder),(body+elbowDist,elbow),(body+handDist,hands)),5) # ARMS
    pygame.draw.circle(screen, color, (body+handDist,hands), 2) # RIGHTHAND
    pygame.draw.circle(screen, color, (body-handDist,hands), 2) # LEFTHAND
    pygame.draw.circle(screen, color, (body,hip-70), 10) # HEAD
    pygame.display.update()

    pygame.draw.lines(screen,BLACK, False,((body-feetDist,feet),(body-hipDist,hip),(body+hipDist,hip),(body+feetDist,feet)),5) # LEGS
    pygame.draw.lines(screen,BLACK, False,((body,hip),(body,shoulder)),25) # BODY
    pygame.draw.lines(screen,BLACK, False,((body-handDist,hands),(body-elbowDist,elbow),(body-shoulderDist,shoulder),(body+shoulderDist,shoulder),(body+elbowDist,elbow),(body+handDist,hands)),5) # ARMS
    pygame.draw.circle(screen, BLACK, (body+handDist,hands), 2) # RIGHTHAND
    pygame.draw.circle(screen, BLACK, (body-handDist,hands), 2) # LEFTHAND
    pygame.draw.circle(screen, BLACK, (body,hip-70), 10) # HEAD

def squatGIF(delayTime):
    stHeel, stKneeHight, stKneeLength, stHip = 300,250,600,200
    hsHeel, hsKneeHight, hsKneeLength, hsHip = 300,270,585,240
    sqHeel, sqKneeHight, sqKneeLength, sqHip = 300,285,560,280


    # STAND
    squatFigure(screen, WHITE, stHeel, stKneeHight, stKneeLength, stHip)
    pygame.time.wait(delayTime)
    # HALF SQUAT
    squatFigure(screen, WHITE, hsHeel, hsKneeHight, hsKneeLength, hsHip)
    pygame.time.wait(delayTime)
    # SQUAT
    squatFigure(screen, WHITE, sqHeel, sqKneeHight, sqKneeLength, sqHip)
    pygame.time.wait(delayTime)
    # HALF SQUAT
    squatFigure(screen, WHITE, hsHeel, hsKneeHight, hsKneeLength, hsHip)
    pygame.time.wait(delayTime)
    # STAND
    squatFigure(screen, WHITE, stHeel, stKneeHight, stKneeLength, stHip)




def jumpingJackGIF(moveX,moveY,delayTime):
    # STAND
    body, feet, hip, hands = 600, 300, 220, 220
    shoulder = hip - 50
    elbow = math.ceil((shoulder + hands) / 2)
    hipDist, feetDist, shoulderDist, handDist = 10,10,12,25
    elbowDist = math.ceil((shoulderDist + handDist) / 2)

    jumpingJackFigure(screen,WHITE,body, feet, hip, shoulder, hands, hipDist, feetDist, shoulderDist, handDist, elbow, elbowDist)

    pygame.time.wait(delayTime)

    # HALF JJ
    body, feet, hip = 600, 300, 230
    shoulder = hip - 50
    hands = shoulder
    elbow = shoulder
    hipDist, feetDist, shoulderDist, handDist = 10,25,12,55
    elbowDist = math.ceil((shoulderDist + handDist) / 2)

    jumpingJackFigure(screen,WHITE,body, feet, hip, shoulder, hands, hipDist, feetDist, shoulderDist, handDist, elbow, elbowDist)

    pygame.time.wait(delayTime)

    # JJ
    body, feet, hip, hands= 600, 300, 245, 145 
    shoulder = hip - 50
    elbow = math.ceil((shoulder + hands) / 2)
    hipDist, feetDist, shoulderDist, handDist, elbowDist = 10,40,12,12,30

    jumpingJackFigure(screen,WHITE,body, feet, hip, shoulder, hands, hipDist, feetDist, shoulderDist, handDist, elbow, elbowDist)

    pygame.time.wait(delayTime)
    
    # HALF JJ
    body, feet, hip = 600, 300, 230
    shoulder = hip - 50
    hands = shoulder
    elbow = shoulder
    hipDist, feetDist, shoulderDist, handDist = 10,25,12,55
    elbowDist = math.ceil((shoulderDist + handDist) / 2)

    jumpingJackFigure(screen,WHITE,body, feet, hip, shoulder, hands, hipDist, feetDist, shoulderDist, handDist, elbow, elbowDist)

    pygame.time.wait(delayTime)

    # STAND
    body, feet, hip, hands = 600, 300, 220, 220
    shoulder = hip - 50
    elbow = math.ceil((shoulder + hands) / 2)
    hipDist, feetDist, shoulderDist, handDist = 10,10,12,25
    elbowDist = math.ceil((shoulderDist + handDist) / 2)

    jumpingJackFigure(screen,WHITE,body, feet, hip, shoulder, hands, hipDist, feetDist, shoulderDist, handDist, elbow, elbowDist)


def arrowBlock(scolor,left,top,width,height,delayTime):
    pygame.draw.rect(screen, ORANGE, [left,top,width,height])


def arrowGIF(left,top,width,height,color,delayTime):
    numBlocks = 10
    block = math.floor(height/numBlocks)
    arrowWidth = math.ceil(width/2)
    for i in range(numBlocks):
        pygame.draw.rect(screen, color, [left,(top+(block*i)),width,block])
        pygame.draw.rect(screen, color, [left,(top+(block*(i+1))),width,block])
        if i is not 0:
            pygame.draw.rect(screen, BLACK, [left,(top+(block*(i-1))),width,block])
        else:
            pygame.draw.rect(screen, BLACK, [left,(top+(block*(numBlocks))),width,block])
            pygame.draw.rect(screen, BLACK, [left,(top+(block*(numBlocks-1))),width,block])
        pygame.display.update()
        pygame.time.wait(delayTime)
    pygame.draw.polygon(screen, color,[[left,top+height-(block+arrowWidth)],[left,top+height+(block+arrowWidth)],[left-width,top+height]])
    pygame.display.update()
    pygame.time.wait(delayTime)
    pygame.draw.rect(screen, BLACK, [left,(top+(block*(numBlocks))),width,block])
    pygame.draw.rect(screen, BLACK, [left,(top+(block*(numBlocks-1))),width,block])
    pygame.draw.polygon(screen, BLACK,[[left,top+height-(block+arrowWidth)],[left,top+height+(block+arrowWidth)],[left-width,top+height]])




BLACK      = ( 0, 0, 0)
WHITE      = ( 255, 255, 255)
GREEN      = (  0, 255,   0)
RED        = (255,   0,   0)
ORANGE     = (255, 165,   0)

pygame.init()
screen = pygame.display.set_mode((1920, 1080))

done = False
clock = pygame.time.Clock()

while not done:


        redTime = 3
        pygame.draw.circle(screen, BLACK, (200,800), 150)
        pygame.draw.circle(screen, RED, (200,200), 150)
        pygame.display.update()

        delayTime = 300
        delayTimeArrow = 150
        for i in range(5):
            pygame.draw.circle(screen, BLACK, (200,800), 150,2)
            pygame.display.update()
            # jumpingJackGIF(50,100,delayTime)
            squatGIF(delayTime)
            pygame.time.wait(delayTime+200)
            arrowGIF(500,300,100,500,ORANGE,delayTimeArrow)
            pygame.draw.circle(screen, GREEN, (200,800), 150,2)
            pygame.display.update()
            pygame.time.wait(delayTime+200)



        # while redTime is not 0:
        #     delayTime = 300

        #     # squatGIF(delayTime)

        #     jumpingJackGIF(delayTime)
        #     redTime -= 1


        pygame.draw.circle(screen, BLACK, (200,200), 150)
        pygame.draw.circle(screen, GREEN, (200,800), 150)
        pygame.display.update()
        pygame.time.wait(1000)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        pygame.display.flip()
