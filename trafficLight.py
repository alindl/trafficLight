import pygame
import time

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
        pygame.draw.circle(screen, RED, (200,200), 150)
        pygame.display.update()
        pygame.time.wait(1000)

        # Squat Standing
        pygame.draw.lines(screen,WHITE,False,((570,300),(600,300),(600,150),(525,150),(600,150),(600,100)),5) # BODY
        pygame.draw.circle(screen, WHITE, (600,100), 15) # HEAD
        pygame.display.update()

        pygame.time.wait(1000)
        # Clear Squat Standing
        pygame.draw.lines(screen,BLACK,False,((570,300),(600,300),(600,150),(525,150),(600,150),(600,100)),5) # BODY
        pygame.draw.circle(screen, BLACK, (600,100), 15) # HEAD

        # Squat Squatting
        pygame.draw.lines(screen,WHITE,False,((570,300),(600,300),(550,275),(600,250),(600,225),(525,225),(600,225),(600,200),),5) # BODY
        pygame.draw.circle(screen, WHITE, (600,200), 15) # HEAD
        pygame.display.update()
        
        pygame.time.wait(1000)
        # Clear Squat Squatting
        pygame.draw.lines(screen,BLACK,False,((570,300),(600,300),(550,275),(600,250),(600,225),(525,225),(600,225),(600,200),),5) # BODY
        pygame.draw.circle(screen, BLACK, (600,200), 15) # HEAD

        # pygame.draw.line(screen,WHITE,(600,300),(600,100),5) # BODY
        # pygame.draw.line(screen,WHITE,(525,150),(600,150),5) # ARMS
        # pygame.draw.line(screen,WHITE,(570,300),(600,300),5) # FEET




        pygame.draw.circle(screen, BLACK, (200,200), 150)
        pygame.draw.circle(screen, GREEN, (200,700), 150)
        pygame.display.update()
        pygame.time.wait(1000)
        pygame.draw.circle(screen, BLACK, (200,700), 150)
        pygame.display.update()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        pygame.display.flip()
