import argparse
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
        else:
            pygame.draw.line(screen, color, bodyDown, foot, (2*scale))
    else:
        if dim:
            # Legs
            linesToPoints(screen, color, bodyDown, footLeft,  6,math.ceil(scale*0.4))
            linesToPoints(screen, color, bodyDown, footRight, 6,math.ceil(scale*0.4))
            # Arms
            linesToPoints(screen, color, bodyUp, handLeft,  6,math.ceil(scale*0.4))
            linesToPoints(screen, color, bodyUp, handRight, 6,math.ceil(scale*0.4))

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

parser = argparse.ArgumentParser(description='Get metric and number.')
parser.add_argument('metric', choices=['counter', 'seconds'])
parser.add_argument('number', type=int)
args = parser.parse_args()

while not done:
        
    pygame.draw.rect(screen, DARKRED, [0,0,screenLength/2,screenLength/2])
    pygame.draw.rect(screen, DARKGREEN, [0,screenLength/2,screenLength/2,screenLength/2])
    redSeconds = args.number
    greenSeconds = 5
    dimmed = True

    # RED PHASE
    ## Seconds Mode
    if args.metric == 'seconds':
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
                if not dimmed and (args.metric == 'seconds'):
                    redSeconds -= 1

                if dimmed and (args.metric == 'counter'):
                    redSeconds += 1

            if i > (5*redSeconds):
                break

    ## Counter Mode
    elif args.metric == 'counter':
        i = 0
        second = 0
        while redSeconds > 0:
            if redSeconds < 1:
                break

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        redSeconds -= 1
                        pygame.draw.rect(screen, DARKGREEN, [0,screenLength/2,screenLength/2,screenLength/2])
                    if event.key == pygame.K_RETURN:
                        dimmed = False if dimmed else True
                    if event.key == pygame.K_ESCAPE:
                        done = True
                        sys.exit()
            draw_stick_figure(screen,RED,190,50,15,i,dimmed)

            font_surface = font.render(str(redSeconds), 1, RED)
            font_rect = font_surface.get_rect()
            font_rect.topleft = (10,10)
            screen.blit(font_surface,(65,660))

            pygame.display.update()
            pygame.time.wait(200)

            pygame.draw.rect(screen, DARKRED, [0,0,screenLength/2,screenLength/2])
            pygame.display.update()
            
            i += 1
            if i == 4:
                i = 0
    pygame.draw.rect(screen, DARKGREEN, [0,screenLength/2,screenLength/2,screenLength/2])

    # GREEN PHASE
    for i in range(5*greenSeconds):
        draw_stick_figure(screen,GREEN,190,600,15,(i%4)+4,False)

        font_surface = font.render(str(greenSeconds-(math.ceil(i/5))), 1, GREEN)
        font_rect = font_surface.get_rect()
        font_rect.topleft = (10,10)
        screen.blit(font_surface,(65,110))
        pygame.display.update()
        pygame.time.wait(200)

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
