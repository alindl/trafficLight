import pygame
import time
import math

def draw_stick_figure(screen,color, x, y,scale, pos):
    if pos == 0: # Stand
        bodyUp =    [(5*scale) + x, (7*scale) + y]
        bodyDown =  [(5*scale) + x, (17*scale) + y]
    
        # Legs
        pygame.draw.line(screen, color, bodyDown, [(10*scale) + x-45, (27*scale) + y], (2*scale))
        pygame.draw.line(screen, color, bodyDown, [x +45, (27*scale) + y], (2*scale))

        # Arms
        pygame.draw.line(screen, color, bodyUp , [(9*scale) + x -10, (17*scale) + y], (2*scale))
        pygame.draw.line(screen, color, bodyUp , [(1*scale) + x +10, (17*scale) + y], (2*scale))

        # Body
        pygame.draw.line(screen, color, bodyDown, bodyUp, (2*scale))

        # Head
        pygame.draw.ellipse(screen, color, [1 + x+(2.5*scale), y-(4*scale)+(5*scale), (10*scale)-(5*scale), (10*scale)-(5*scale)], 0)

    elif pos == 1 or pos == 3: # Mid Pos
        downMove = (scale*1.5)
        bodyUp =    [(5*scale) + x, (7*scale) + y + downMove ]
        bodyDown =  [(5*scale) + x, (17*scale) + y + downMove ]

        # Legs
        pygame.draw.line(screen, color, bodyDown, [(10*scale) + x-15, (27*scale) + y], (2*scale))
        pygame.draw.line(screen, color, bodyDown, [x+15, (27*scale) + y], (2*scale))

        # Arms
        pygame.draw.line(screen, color, bodyUp, [(9*scale) + x+50,bodyUp[1]], (2*scale))
        pygame.draw.line(screen, color, bodyUp, [(1*scale) + x-50,bodyUp[1]], (2*scale))

        # Body
        pygame.draw.line(screen, color, bodyDown, bodyUp, (2*scale))

        # Head
        pygame.draw.ellipse(screen, color, [1 + x+(2.5*scale), y-(4*scale)+(4*scale)+ downMove, (10*scale)-(5*scale), (10*scale)-(5*scale)], 0)

    elif pos == 2:   # Full Pos
        downMove = (scale*3)
        bodyUp =    [(5*scale) + x, (7*scale) + y + downMove ]
        bodyDown =  [(5*scale) + x, (17*scale) + y + downMove ]

        # Legs
        pygame.draw.line(screen, color, bodyDown, [(10*scale) + x+10, (27*scale) + y], (2*scale))
        pygame.draw.line(screen, color, bodyDown, [x -10, (27*scale) + y], (2*scale))

        # Arms
        pygame.draw.line(screen, color, bodyUp, [(9*scale) + x+50, (1*scale) + y + downMove ], (2*scale))
        pygame.draw.line(screen, color, bodyUp, [(1*scale) + x-50, (1*scale) + y + downMove ], (2*scale))

        # Body
        pygame.draw.line(screen, color, bodyDown, bodyUp, (2*scale))
        
        # Head
        pygame.draw.ellipse(screen, color, [1 + x+(2.5*scale) , y-(4*scale)+(4*scale) + downMove , (10*scale)-(5*scale), (10*scale)-(5*scale)], 0)
    
    elif pos == 4: # Run first

        bodyUp =    [(5*scale) + x, (7*scale) + y]
        bodyDown =  [(5*scale) + x, (17*scale) + y]
    
        # Legs
        pygame.draw.line(screen, color, bodyDown, [(10*scale) + x-15, (27*scale) + y], (2*scale))
        pygame.draw.line(screen, color, bodyDown, [x+15, (27*scale) + y], (2*scale))

        # Arms
        pygame.draw.line(screen, color, bodyUp , [(10*scale) + x , (15*scale) + y], (2*scale))
        pygame.draw.line(screen, color, bodyUp , [x , (15*scale) + y], (2*scale))

        # Body
        pygame.draw.line(screen, color, bodyDown, bodyUp, (2*scale))

        # Head
        pygame.draw.ellipse(screen, color, [1 + x+(2.5*scale), y-(4*scale)+(5*scale), (10*scale)-(5*scale), (10*scale)-(5*scale)], 0)

    elif pos == 5 or pos == 7: # Run second
        bodyUp =    [(5*scale) + x, (7*scale) + y]
        bodyDown =  [(5*scale) + x, (17*scale) + y]
    
        # Legs
        pygame.draw.line(screen, color, bodyDown, [(10*scale) + x-45, (27*scale) + y], (2*scale))
        pygame.draw.line(screen, color, bodyDown, [x +45, (27*scale) + y], (2*scale))

        # Arms
        pygame.draw.line(screen, color, bodyUp , [(9*scale) + x -10, (17*scale) + y], (2*scale))
        pygame.draw.line(screen, color, bodyUp , [(1*scale) + x +10, (17*scale) + y], (2*scale))

        # Body
        pygame.draw.line(screen, color, bodyDown, bodyUp, (2*scale))

        # Head
        pygame.draw.ellipse(screen, color, [1 + x+(2.5*scale), y-(4*scale)+(5*scale), (10*scale)-(5*scale), (10*scale)-(5*scale)], 0)

    elif pos == 6: # Run third
        bodyUp =    [(5*scale) + x, (7*scale) + y]
        bodyDown =  [(5*scale) + x, (17*scale) + y]
    
        # Legs
        pygame.draw.line(screen, color, bodyDown, [bodyDown[0],bodyDown[1]+(scale*10)], (2*scale))

        # Body
        pygame.draw.line(screen, color, bodyDown, bodyUp, (2*scale))

        # Head
        pygame.draw.ellipse(screen, color, [1 + x+(2.5*scale), y-(4*scale)+(5*scale), (10*scale)-(5*scale), (10*scale)-(5*scale)], 0)



def linesToPoints(screen, color, a, b, divisionFactor,radius):
    x_dist = abs(a[0] - b[0])
    y_dist = abs(a[1] - b[1])
    x_jump = math.floor(x_dist/divisionFactor)
    y_jump = math.floor(y_dist/divisionFactor)
    for i in range(divisionFactor+1):
        if a[0] < b[0]:
            x_plus = True
            if a[1] < b[1]:
                y_plus = True
                pygame.draw.circle(screen,color,(a[0]+(x_jump*i),a[1]+(y_jump*i)),radius)
            else:
                y_plus = False
                pygame.draw.circle(screen,color,(a[0]+(x_jump*i),a[1]-(y_jump*i)),radius)
        else:
            x_plus = False
            if a[1] < b[1]:
                y_plus = False
                pygame.draw.circle(screen,color,(a[0]-(x_jump*i),a[1]+(y_jump*i)),radius)
            else:
                y_plus = True
                pygame.draw.circle(screen,color,(a[0]-(x_jump*i),a[1]-(y_jump*i)),radius)


def squatFigure(screen,color,body,heel,kneeHight,kneeLength,hip):

    pygame.draw.lines(screen,color, False,((body-30,heel),(body,heel),(body-kneeLength,kneeHight),(body,hip),(body,hip-35),(body-60,hip-35),(body,hip-35)),6) # BODY
    pygame.draw.circle(screen, color, (body,hip-60), 12) # HEAD
    pygame.display.update()

    # Clear 
    pygame.draw.lines(screen,BLACK, False,((body-30,heel),(body,heel),(body-kneeLength,kneeHight),(body,hip),(body,hip-35),(body-60,hip-35),(body,hip-35)),6) # BODY
    pygame.draw.circle(screen, BLACK, (body,hip-60), 12) # HEAD

def squatGIF(delayTime):
    stHeel, stKneeHight, stKneeLength, stHip = 300,250,0,200
    hsHeel, hsKneeHight, hsKneeLength, hsHip = 300,270,15,240
    sqHeel, sqKneeHight, sqKneeLength, sqHip = 300,285,40,280
    body = 600 - 40

    # STAND
    squatFigure(screen, WHITE, body, stHeel, stKneeHight, stKneeLength, stHip)
    pygame.time.wait(delayTime)
    # HALF SQUAT
    squatFigure(screen, WHITE, body, hsHeel, hsKneeHight, hsKneeLength, hsHip)
    pygame.time.wait(delayTime)
    # SQUAT
    squatFigure(screen, WHITE, body, sqHeel, sqKneeHight, sqKneeLength, sqHip)
    pygame.time.wait(delayTime)
    # HALF SQUAT
    squatFigure(screen, WHITE, body, hsHeel, hsKneeHight, hsKneeLength, hsHip)
    pygame.time.wait(delayTime)
    # STAND
    squatFigure(screen, WHITE, body, stHeel, stKneeHight, stKneeLength, stHip)

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
# BACKLIGHT
DARKGREEN      = (  0, 30,   0)
GREEN      = (  0, 255,   0)
# BACKLIGHT
DARKRED        = (30,   0,   0)
RED        = (255,   0,   0)
ORANGE     = (255, 165,   0)

pygame.init()
screenWidth = 1920
screenLength = 1080
screen = pygame.display.set_mode((screenWidth, screenLength))

done = False
clock = pygame.time.Clock()

while not done:
        
    pygame.draw.rect(screen, DARKRED, [0,0,screenLength/2,screenLength/2])
    pygame.draw.rect(screen, DARKGREEN, [0,screenLength/2,screenLength/2,screenLength/2])
    pygame.display.update()
    # jumpingJackGIF(-300,50,300)
    # linesToPoints(screen,WHITE,(200,200),(400,400),10,5)
    for i in range(15):
        draw_stick_figure(screen,RED,190,50,15,i%4)
        pygame.display.update()
        pygame.time.wait(250)
        draw_stick_figure(screen,DARKRED,190,50,15,i%4)
        pygame.display.update()

    for i in range(15):
        draw_stick_figure(screen,GREEN,190,600,15,(i%4)+4)
        pygame.display.update()
        pygame.time.wait(250)
        draw_stick_figure(screen,DARKGREEN,190,600,15,(i%4)+4)
        pygame.display.update()






    # pygame.draw.circle(screen, DARKGREEN, (200,800), 150)
    # pygame.draw.circle(screen, RED, (200,200), 150)
    # pygame.display.update()

    # delayTime = 300
    # delayTimeArrow = 150
    # factor = 1
    # for i in range(5):
    #     delayTimeArrow = math.ceil(150 / factor)
    #     pygame.draw.circle(screen, BLACK, (200,800), 150,2)
    #     pygame.display.update()
    #     # jumpingJackGIF(50,100,delayTime)
    #     squatGIF(delayTime)
    #     for event in pygame.event.get():
    #         if event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_LEFT:
    #                 factor /= 2
    #             if event.key == pygame.K_RIGHT:
    #                 factor *= 2
    #             if event.key == pygame.K_ESCAPE:
    #                 done = True
    #                 sys.exit()
    #     pygame.time.wait(delayTime+200)
    #     for j in range(math.ceil(factor/2)):
    #         pygame.draw.circle(screen, BLACK, (200,800), 150,2)
    #         arrowGIF(500,300,100,500,ORANGE,delayTimeArrow)
    #         pygame.draw.circle(screen, GREEN, (200,800), 150,2)
    #         pygame.display.update()
    #         pygame.time.wait(150)
    #     # pygame.time.wait(100)



    # while redTime is not 0:
    #     delayTime = 300

    #     # squatGIF(delayTime)

    #     jumpingJackGIF(delayTime)
    #     redTime -= 1


    # pygame.draw.circle(screen, BLACK, (200,200), 150)
    # pygame.draw.circle(screen, GREEN, (200,800), 150)
    # pygame.display.update()
    # pygame.time.wait(1000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pygame.display.flip()
