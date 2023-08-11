import pygame
import sys
from classes import Button,image,Player,Stats,food
width = 1200
height = 800

pygame.init()
pygame.mixer.init()

pygame.display.set_caption("Below")
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
def end_scene():
    played_jumpScare = False
    background_sound.stop()
    while True:
            end_screen = pygame.Surface((width,height))
            end_screen.fill((0,0,0))
            screen.blit(end_screen,(0,0))
            bunny_bun_horror_load.draw(screen)
            if not played_jumpScare:
                jump_scare_sound.play()
                played_jumpScare = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if retry_btn.draw(screen):
                food_bar_load.current_stat = food_bar_load.starting_stats
                sprint_bar_load.current_stat = sprint_bar_load.starting_stats
                
                break
            pygame.display.flip()
            clock.tick(60)
    

def fade_tran():
    
    for alpha in range(0,300,1):
        fade.set_alpha(alpha)
        screen.blit(fade,(0,0))
        pygame.display.update()
        pygame.time.delay(10)

def pause_func():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pause_menu = True
                while pause_menu:
                    pause_menu_screen = pygame.Surface((width,height))
                    pause_menu_screen.fill((0,0,0))
                    pause_menu_screen.set_alpha(20)
                    screen.blit(pause_menu_screen,(0,0))
                    if back_btn.draw(screen):
                        pause_menu = False
                    
                    
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                pause_menu = False
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                    pygame.display.flip()
                    clock.tick(60)


def game_logic():
    # if LSHIFT then sprint stats will go down this also runs all the player input
    if bunny_bun_load.Player_input(sprint_bar_load.current_stat):
        sprint_bar_load.current_stat -= 1
    # checks player collision 
    if pygame.Rect.colliderect(bunny_bun_load.rect_p,food_load.rect) and food_bar_load.Max != food_bar_load.current_stat:
        food_bar_load.current_stat += 10
        sprint_bar_load.current_stat += 30
        food_load.eaten = True
    if food_bar_load.current_stat > food_bar_load.Max:
        food_bar_load.current_stat = food_bar_load.Max
    
    if sprint_bar_load.current_stat > sprint_bar_load.Max:
        sprint_bar_load.current_stat = sprint_bar_load.Max

    if food_bar_load.current_stat < (food_bar_load.Max / 4):
        ramp_up_sound.set_volume(0.2)
        ramp_up_sound.play()
        ramp_up_sound.fadeout(40)
    elif food_bar_load.current_stat < (food_bar_load.Max / 2):
        ramp_up_sound.set_volume(0.1)
        ramp_up_sound.play()
        ramp_up_sound.fadeout(40)
    

    if food_bar_load.current_stat == 0 or food_bar_load.current_stat < 0:
        # lose game
        bunny_bun_load.hunger = True
        end_scene()

    else:
        food_bar_load.current_stat -= 0.1
        

def redraw_window():
    screen.fill(screen_color)
    background_img_load.draw(screen)
    # load everything before the pause
    flower_load.draw(screen)
    grass_load.draw_multiple(screen,12)
    food_load.draw()
    
    
    bunny_bun_load.Player_draw()
    food_bar_load.stats_draw()
    sprint_bar_load.stats_draw()
    
    pause_func()
    game_logic()




    pygame.display.update()



background_img = pygame.image.load("images\\background0.png").convert_alpha()
background_img_load = image(0,0,background_img,1)

play_game_img = pygame.image.load("images\Start Game!.png").convert_alpha()
play_game_btn = Button(((width/2) - 174.5),((height/2) + 50),play_game_img,1)

back_btn_img = pygame.image.load("images\BACK.png").convert_alpha()
back_btn = Button(((width/2) - 174.5),((height/2) + 50),back_btn_img,1)

retry_img = pygame.image.load("images\\retry.png").convert_alpha()
retry_btn = Button(((width/2) - 174.5),((height/2) + 50),retry_img,1)

flower_img = pygame.image.load("images\\flower.png").convert_alpha()
flower_load = image(300,400,flower_img,6)

grass_img = pygame.image.load("images\\grass.png").convert_alpha()
grass_load = image(20,20,grass_img,3)

bunny_bun_image = pygame.image.load("bunny-emotes\PNGs\\bunny (17).png").convert_alpha()
bunny_bun_image_horror = pygame.image.load("bunny-emotes\PNGs\\bun.png").convert_alpha()
bunny_bun_load = Player(bunny_bun_image,500,500,0.5,screen,bunny_bun_image_horror)
bunny_bun_horror_load = image(350,150,bunny_bun_image_horror,2.5)

food_bar_image = pygame.image.load("images\\food_bar.png").convert_alpha()
food_bar_load = Stats(0,90,food_bar_image,screen,0.4,240,280,(222, 179, 80))

food_image = pygame.image.load("images\\food.png").convert_alpha()
food_load = food(200,200,screen,food_image,0.09)

sprint_bar_image = pygame.image.load("images\\food_bar.png").convert_alpha()
sprint_bar_load = Stats(0,120,sprint_bar_image,screen,0.4,240,280,(67, 140, 204))


jump_scare_sound = pygame.mixer.Sound("sound\jump_scare.mp3")
background_sound = pygame.mixer.Sound("sound\\Below_background_noise.mp3")
ramp_up_sound = pygame.mixer.Sound("sound\\ramp_up.mp3")
background_sound.set_volume(0.5)
start_Menu = True
pause_menu = False

screen_color = (255,255,255)
background_sound.play(-1)

while True:


    while start_Menu:
        
        fade = pygame.Surface((width,height))
        fade.fill((21, 1, 38))

        if play_game_btn.draw(screen):
            fade_tran()
            start_Menu = False
            redraw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()
        clock.tick(60)
    


    redraw_window()

    



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    pygame.display.flip()
    clock.tick(60)
