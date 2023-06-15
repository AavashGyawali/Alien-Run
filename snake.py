
import pygame
from sys import exit
width=500
height= 400
pygame.init()
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake game")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)# sets max frame to 60fps
    