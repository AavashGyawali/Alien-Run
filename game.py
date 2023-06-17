
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
score_surface=test_font.render(" My game",False,(64,64,64))
score_rec=score_surface.get_rect(center=(400,50))

#snail surface
snail_surface=pygame.image.load("graphics\snail\snail1.png").convert_alpha()
snail_rec=snail_surface.get_rect(bottomright=(600,300))

#player
player_surface=pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_rec=player_surface.get_rect(bottomleft=(80,300))
player_gravity=0

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()


        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                player_gravity=-20
                # player_gravity+=1
                
        
        if event.type == pygame.KEYUP:
            print("key up")

        
        # if player_rec.collidepoint((mouse_pos)) and pygame.mouse.get_pressed():
        #     player_gravity=-20



        mouse_pos=pygame.mouse.get_pos()
        if event.type == pygame.MOUSEMOTION:
            if player_rec.collidepoint((mouse_pos)) and pygame.mouse.get_pressed():
                player_gravity=-20
                player_gravity+=1
                
        

    #showing surface to the screen using coordinate        
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    pygame.draw.rect(screen,"#c0e8ec",score_rec,border_radius=4)
    pygame.draw.rect(screen,"black",score_rec,2,border_radius=4)
    screen.blit(score_surface,score_rec)
    # pygame.draw.ellipse(screen,"black",pygame.Rect(50,200,50,100))

    #for snail   
    screen.blit(snail_surface,snail_rec)

    
    snail_rec.left-=4
    if snail_rec.right<0:snail_rec.left=800

    #Player
    player_gravity+=1
    player_rec.y+=player_gravity
    screen.blit(player_surface,player_rec)
    
    if player_rec.left>800:player_rec.right=0




    # keys=pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print('Jump')
    
    # #collison
    # collision=player_rec.colliderect(snail_rec)
    # if collision:
    #     print("Collision")


    # mouse_pos=pygame.mouse.get_pos()
    # if player_rec.collidepoint((mouse_pos)):
    #     print(pygame.mouse.get_pressed())#shows what mouse button is pressed
    
    pygame.display.update()
    clock.tick(60) # sets max frame to 60fps
    