
import pygame
from sys import exit
width=800
height= 600
pygame.init()
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake game")
clock = pygame.time.Clock()
test_surface= pygame.Surface((100,200))
test_surface.fill('red')

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(test_surface,(200,100))

    pygame.display.update()
    clock.tick(60) # sets max frame to 60fps
    