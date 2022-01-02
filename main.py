from numpy import true_divide
import pygame
import sys
import traceback
from pygame.locals import *
import random
import myplane

pygame.init()
pygame.mixer.init()
bg_size = width, height = 480, 700
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption('SPACE WAR')


background = pygame.image.load('image\\background.png').convert()


pygame.mixer.music.load('sound\\game_music.wav')
pygame.mixer.music.set_volume(0.2)
bullet_sound = pygame.mixer.Sound("sound/bullet.wav")
bullet_sound.set_volume(0.2)
bomb_sound = pygame.mixer.Sound("sound/use_bomb.wav")
bomb_sound.set_volume(0.2)
supply_sound = pygame.mixer.Sound("sound/supply.wav")
supply_sound.set_volume(0.2)
get_bomb_sound = pygame.mixer.Sound("sound/get_bomb.wav")
get_bomb_sound.set_volume(0.2)
get_bullet_sound = pygame.mixer.Sound("sound/get_bullet.wav")
get_bullet_sound.set_volume(0.2)
upgrade_sound = pygame.mixer.Sound("sound/upgrade.wav")
upgrade_sound.set_volume(0.2)
enemy3_fly_sound = pygame.mixer.Sound("sound/enemy3_flying.wav")
enemy3_fly_sound.set_volume(0.2)
enemy1_down_sound = pygame.mixer.Sound("sound/enemy1_down.wav")
enemy1_down_sound.set_volume(0.2)
enemy2_down_sound = pygame.mixer.Sound("sound/enemy2_down.wav")
enemy2_down_sound.set_volume(0.2)
enemy3_down_sound = pygame.mixer.Sound("sound/enemy3_down.wav")
enemy3_down_sound.set_volume(0.5)
me_down_sound = pygame.mixer.Sound("sound/me_down.wav")
me_down_sound.set_volume(0.2)

def main():
    pygame.mixer.music.play()\
    
    #generate user plane
    me = myplane.MyPlane(bg_size)

    clock = pygame.time.Clock()

    #picture switching
    switch = True

    running = True

    delay = 100

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running == False
                pygame.quit()
                sys.exit()

        # check user keyboard
        key_pressed  = pygame.key.get_pressed()

        if key_pressed[K_w] or key_pressed[[K_UP]]:
            me.moveUp()
        
        if key_pressed[K_s] or key_pressed[[K_DOWN]]:
            me.moveDown()
        
        if key_pressed[K_a] or key_pressed[[K_LEFT]]:
            me.moveLeft()
        
        if key_pressed[K_d] or key_pressed[[K_RIGHT]]:
            me.moveRight()

        screen.blit(background, (0, 0))

        #draw the plane
        
        if switch:
            screen.blit(me.image1, me.rect)
        else:
            screen.blit(me.image2, me.rect)

        if (not delay % 5):
            switch = not switch
            
        delay -= 1
        if not delay:
            delay = 100

        pygame.display.flip()

        clock.tick(60)

if __name__ == "main":
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()