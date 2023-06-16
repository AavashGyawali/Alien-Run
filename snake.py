
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
sky_surface=pygame.image.load("graphics/Sky.png").convert()
ground_surface=pygame.image.load("graphics/ground.png").convert()

#Text
text_surface=test_font.render("My game",False,"Black")
text_rec=text_surface.get_rect(center=(400,50))

#snail surface
snail_surface=pygame.image.load("graphics\snail\snail1.png").convert_alpha()
snail_rec=snail_surface.get_rect(bottomright=(600,300))


player_surface=pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_rec=player_surface.get_rect(bottomleft=(80,300))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rec.collidepoint(event.pos):
        #         print("collide")

        

    #showing surface to the screen using coordinate        
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    pygame.draw.rect(screen,"pink",text_rec)
    screen.blit(text_surface,text_rec)

    #for snail   
    screen.blit(snail_surface,snail_rec)

    
    snail_rec.left-=4
    if snail_rec.right<0:snail_rec.left=800

    #for player
    screen.blit(player_surface,player_rec)
    # player_rec.left+=4
    
    if player_rec.left>800:player_rec.right=0
    
    # #collison
    # collision=player_rec.colliderect(snail_rec)
    # if collision:
    #     print("Collision")


    # mouse_pos=pygame.mouse.get_pos()
    # if player_rec.collidepoint((mouse_pos)):
    #     print(pygame.mouse.get_pressed())#shows what mouse button is pressed
    
    pygame.display.update()
    clock.tick(60) # sets max frame to 60fps
    