
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


game_active=True

#creating surface
sky_surface=pygame.image.load("graphics/Sky.png").convert()
ground_surface=pygame.image.load("graphics/ground.png").convert()

#Score
score_surface=test_font.render(" My game",False,(64,64,64))
score_rec=score_surface.get_rect(center=(400,50))

#snail surface
snail_surface=pygame.image.load("graphics\snail\snail1.png").convert_alpha()
snail_rec=snail_surface.get_rect(bottomright=(600,300))

#player
player_surface=pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_rec=player_surface.get_rect(bottomleft=(80,300))
player_gravity=0

#Game Over
game_over_surface=test_font.render("Game Over",False,(64,64,64))
game_over_rec=game_over_surface.get_rect(center=(400,150))

to_restart_surface=test_font.render("To Restart press Space ",False,(64,64,64))
to_restart_rec=to_restart_surface.get_rect(center=(400,200))


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()


        if game_active:
#if space key is pressed player will jump
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE and player_rec.bottom >=300:
                        player_gravity=-20
                        # player_gravity+=1
                
        

        #if mouse key is pressed on the player rectangle than player will jump
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed():
                    if player_rec.collidepoint(event.pos):#instead of event.pos you can write pygame.mouse.get_pos()
                        player_gravity=-20

        else:
            if event.type == pygame.KEYDOWN and event.key==pygame.K_SPACE:
                game_active=True
                snail_rec.left=800



        
 # Before Collison(Gameplay)
    if game_active:
        #showing surface to the screen using coordinate        
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        pygame.draw.rect(screen,"#c0e8ec",score_rec,border_radius=2)
        pygame.draw.rect(screen,"black",score_rec,2,border_radius=2)
        screen.blit(score_surface,score_rec)
        # pygame.draw.ellipse(screen,"black",pygame.Rect(50,200,50,100))

        #for snail   
        screen.blit(snail_surface,snail_rec)

        
        snail_rec.left-=4
        if snail_rec.right<0:snail_rec.left=800

        #Player
        player_gravity+=1
        player_rec.y+=player_gravity
        if player_rec.bottom>=300:player_rec.bottom=300
        screen.blit(player_surface,player_rec)
        
        if player_rec.left>800:player_rec.right=0

    
        if player_rec.colliderect(snail_rec):
            game_active=False


#After Collision
    else:
        # screen.fill('yellow')
        # pygame.draw.rect(screen,"#c0e8ec",game_over_rec,border_radius=2)
        # pygame.draw.rect(screen,"black",score_rec,2,border_radius=2)
        screen.blit(game_over_surface,game_over_rec)
        screen.blit(to_restart_surface,to_restart_rec)
        


            
         

    pygame.display.update()
    clock.tick(60) # sets max frame to 60fps
    