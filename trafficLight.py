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

# pygame.draw.lines(screen,WHITE,True,)
        pygame.draw.line(screen,WHITE,(400,300),(500,300),5)




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
