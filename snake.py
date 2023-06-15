
import pygame
from sys import exit
width=800
height= 400
pygame.init()
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Snake game")
clock = pygame.time.Clock()

#creating font
test_font=pygame.font.Font("font\Pixeltype.ttf",50)
#creating surface
sky_surface=pygame.image.load("graphics/Sky.png")
ground_surface=pygame.image.load("graphics/ground.png")
text_surface=test_font.render("My game",False,"Black")
#snail
snail_surface=pygame.image.load("graphics\snail\snail1.png")
snail_x_pos=700
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()

    #showing surface to the screen using coordinate        
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(330,50))
    snail_x_pos-=1
    screen.blit(snail_surface,(snail_x_pos,268))

    pygame.display.update()
    clock.tick(60) # sets max frame to 60fps
    