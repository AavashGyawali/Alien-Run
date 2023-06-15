
import pygame
from sys import exit
width=800
height= 400
pygame.init()
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake game")
clock = pygame.time.Clock()
#creating font
test_font=pygame.font.Font(None,50)
#creating surface
sky_surface=pygame.image.load("graphics/Sky.png")
ground_surface=pygame.image.load("graphics/ground.png")
text_surface=test_font.render("My game",False,"Green")

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    #showing surface to the screen using coordinate        
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(325,50))

    pygame.display.update()
    clock.tick(60) # sets max frame to 60fps
    