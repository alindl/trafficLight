import pygame
import time
import math

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
                pygame.draw.circle(screen,color,(math.ceil(a[0])+(x_jump*i),math.ceil(a[1])+(y_jump*i)),radius)
            else:
                y_plus = False
                pygame.draw.circle(screen,color,(math.ceil(a[0])+(x_jump*i),math.ceil(a[1])-(y_jump*i)),radius)
        else:
            x_plus = False
            if a[1] < b[1]:
                y_plus = False
                pygame.draw.circle(screen,color,(math.ceil(a[0])-(x_jump*i),math.ceil(a[1])+(y_jump*i)),radius)
            else:
                y_plus = True
                pygame.draw.circle(screen,color,(math.ceil(a[0])-(x_jump*i),math.ceil(a[1])-(y_jump*i)),radius)


def countDown(text):
        return image

def draw_stick_figure(screen,color, x, y,scale, pos, dim):
    if pos == 0: # Stand
        bodyUp =    [(5*scale) + x, (7*scale) + y]
        bodyDown =  [(5*scale) + x, (17*scale) + y]
        footLeft  = [(10*scale) + x-45, (27*scale) + y]
        footRight = [x +45, (27*scale) + y]
        handLeft =  [(9*scale) + x -10, (17*scale) + y]
        handRight = [(1*scale) + x +10, (17*scale) + y]
        headBox =   [1 + x+(2.5*scale), y-(4*scale)+(5*scale), (10*scale)-(5*scale), (10*scale)-(5*scale)]

    elif pos == 1 or pos == 3: # Mid Pos
        downMove = (scale*1.5)
        bodyUp =    [(5*scale) + x, (7*scale) + y + downMove ]
        bodyDown =  [(5*scale) + x, (17*scale) + y + downMove ]
        footLeft  = [(10*scale) + x-15, (27*scale) + y]
        footRight = [x+15, (27*scale) + y]
        handLeft =  [(9*scale) + x+50,bodyUp[1]]
        handRight = [(1*scale) + x-50,bodyUp[1]]
        headBox =   [1 + x+(2.5*scale), y-(4*scale)+(4*scale)+ downMove, (10*scale)-(5*scale), (10*scale)-(5*scale)]

    elif pos == 2:   # Full Pos
        downMove = (scale*3)
        bodyUp =    [(5*scale) + x, (7*scale) + y + downMove ]
        bodyDown =  [(5*scale) + x, (17*scale) + y + downMove ]
        footLeft  = [(10*scale) + x+10, (27*scale) + y]
        footRight = [x -10, (27*scale) + y]
        handLeft =  [(9*scale) + x+50, (1*scale) + y + downMove ]
        handRight = [(1*scale) + x-50, (1*scale) + y + downMove ]
        headBox =   [1 + x+(2.5*scale) , y-(4*scale)+(4*scale) + downMove , (10*scale)-(5*scale), (10*scale)-(5*scale)]
    
    elif pos == 4: # Run first
        bodyUp =    [(5*scale) + x, (7*scale) + y]
        bodyDown =  [(5*scale) + x, (17*scale) + y]
        footLeft  = [(10*scale) + x-15, (27*scale) + y]  
        footRight = [x+15, (27*scale) + y]
        handLeft =  [(10*scale) + x , (15*scale) + y]
        handRight = [x , (15*scale) + y]
        headBox =   [1 + x+(2.5*scale), y-(4*scale)+(5*scale), (10*scale)-(5*scale), (10*scale)-(5*scale)]

    elif pos == 5 or pos == 7: # Run second
        bodyUp =    [(5*scale) + x, (7*scale) + y]
        bodyDown =  [(5*scale) + x, (17*scale) + y]
        footLeft  = [(10*scale) + x-45, (27*scale) + y]
        footRight = [x +45, (27*scale) + y]
        handLeft =  [(9*scale) + x -10, (17*scale) + y]
        handRight = [(1*scale) + x +10, (17*scale) + y]                                    
        headBox =   [1 + x+(2.5*scale), y-(4*scale)+(5*scale), (10*scale)-(5*scale), (10*scale)-(5*scale)]

    elif pos == 6: # Run third
        bodyUp =    [(5*scale) + x, (7*scale) + y]
        bodyDown =  [(5*scale) + x, (17*scale) + y]
        foot  =     [bodyDown[0],bodyDown[1]+(scale*10)]
        headBox =   [1 + x+(2.5*scale), y-(4*scale)+(5*scale), (10*scale)-(5*scale), (10*scale)-(5*scale)]
    
    if pos == 6:
        # Legs
        if dim:
            linesToPoints(screen, color, bodyDown, foot, 8,math.ceil(scale*0.4))
            # pygame.draw.aaline(screen, color, bodyDown, foot, (2*scale))
        else:
            pygame.draw.line(screen, color, bodyDown, foot, (2*scale))
    else:
        if dim:
            # Legs
            linesToPoints(screen, color, bodyDown, footLeft,  6,math.ceil(scale*0.4))
            linesToPoints(screen, color, bodyDown, footRight, 6,math.ceil(scale*0.4))
            # pygame.draw.aaline(screen, color, bodyDown, footLeft, (2*scale))
            # pygame.draw.aaline(screen, color, bodyDown, footRight, (2*scale))
            # Arms
            linesToPoints(screen, color, bodyUp, handLeft,  6,math.ceil(scale*0.4))
            linesToPoints(screen, color, bodyUp, handRight, 6,math.ceil(scale*0.4))
            # pygame.draw.aaline(screen, color, bodyUp, handLeft, (2*scale))
            # pygame.draw.aaline(screen, color, bodyUp, handRight, (2*scale))

        else:
            # Legs
            pygame.draw.line(screen, color, bodyDown, footLeft, (2*scale))
            pygame.draw.line(screen, color, bodyDown, footRight, (2*scale))
            # Arms
            pygame.draw.line(screen, color, bodyUp , handLeft, (2*scale))
            pygame.draw.line(screen, color, bodyUp , handRight, (2*scale))

    # Body
    if dim:
        linesToPoints(screen, color, bodyDown, bodyUp, 6,math.ceil(scale*0.4))
    else:
        pygame.draw.line(screen, color, bodyDown, bodyUp, (2*scale))

    # Head
    if dim:
        linesToPoints(screen, color, bodyDown, bodyUp, 6,math.ceil(scale*0.4))
        pygame.draw.circle(screen,color,(math.ceil(headBox[0]+(headBox[2]/2)),math.ceil(headBox[1]+(headBox[3]/2+20))),math.ceil(scale*0.4*2),0)
    else:
        pygame.draw.ellipse(screen, color, headBox, 0)


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
pygame.font.init()
screenWidth = 1920
screenLength = 1080
screen = pygame.display.set_mode((screenWidth, screenLength))
font = pygame.font.Font(None, 512)
rect = screen.get_rect()
done = False
clock = pygame.time.Clock()

while not done:
        
    pygame.draw.rect(screen, DARKRED, [0,0,screenLength/2,screenLength/2])
    pygame.draw.rect(screen, DARKGREEN, [0,screenLength/2,screenLength/2,screenLength/2])
    # pygame.display.update()
    # font_surface = font.render("15", 1, RED)
    # font_rect = font_surface.get_rect()
    # font_rect.topleft = (10,10)
    # screen.blit(font_surface,(65,110))
    # pygame.display.update()
    redSeconds = 25
    greenSeconds = 5
    dimmed = True

    for i in range(5*redSeconds):
        if (redSeconds-(math.ceil(i/5))) < 1:
            break
        font_surface = font.render(str(redSeconds-(math.ceil(i/5))), 1, RED)
        font_rect = font_surface.get_rect()
        font_rect.topleft = (10,10)
        screen.blit(font_surface,(65,660))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    dimmed = False if dimmed else True
                    pygame.draw.rect(screen, DARKGREEN, [0,screenLength/2,screenLength/2,screenLength/2])
                if event.key == pygame.K_ESCAPE:
                    done = True
                    sys.exit()
        draw_stick_figure(screen,RED,190,50,15,i%4,dimmed)
        pygame.display.update()
        pygame.time.wait(200)

        pygame.draw.rect(screen, DARKRED, [0,0,screenLength/2,screenLength/2])
        pygame.display.update()
        
        if i%5 == 0:
            pygame.draw.rect(screen, DARKGREEN, [0,screenLength/2,screenLength/2,screenLength/2])
            if not dimmed:
                redSeconds -= 1

        if i > (5*redSeconds):
            break

    pygame.draw.rect(screen, DARKGREEN, [0,screenLength/2,screenLength/2,screenLength/2])


    for i in range(5*greenSeconds):
        draw_stick_figure(screen,GREEN,190,600,15,(i%4)+4,False)
        pygame.display.update()
        pygame.time.wait(200)

        font_surface = font.render(str(greenSeconds-(math.ceil(i/5))), 1, GREEN)
        font_rect = font_surface.get_rect()
        font_rect.topleft = (10,10)
        screen.blit(font_surface,(65,110))

        pygame.draw.rect(screen, DARKGREEN, [0,screenLength/2,screenLength/2,screenLength/2])
        pygame.display.update()

        if i%5 == 0:
            pygame.draw.rect(screen, DARKRED, [0,0,screenLength/2,screenLength/2])
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                    sys.exit()

    pygame.draw.rect(screen, DARKRED, [0,0,screenLength/2,screenLength/2])


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
