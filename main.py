from numpy import true_divide
import pygame
import sys
import traceback
from pygame.locals import *
import random
import myplane
import enemy

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

def add_small_enemies(group1, group2, number):
    for i in range(number):
        e1 = enemy.SmallEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)

def add_mid_enemies(group1, group2, number):
    for i in range(number):
        e1 = enemy.MidEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)

def add_big_enemies(group1, group2, number):
    for i in range(number):
        e1 = enemy.BigEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)

def main():
    pygame.mixer.music.play()\
    
    #generate user plane
    me = myplane.MyPlane(bg_size)

    # generate enemies
    enemies = pygame.sprite.Group()

    # generate small enemies
    small_enemies = pygame.sprite.Group()
    add_small_enemies(small_enemies, enemies, 15)
    # generate mid enemies
    mid_enemies = pygame.sprite.Group()
    add_mid_enemies(small_enemies, enemies, 4)
    # generate small enemies
    big_enemies = pygame.sprite.Group()
    add_big_enemies(small_enemies, enemies, 2)



    clock = pygame.time.Clock()

    #picture switching
    switch = True

    running = True

    delay = 100

    # hit pircture
    e1_destroy_index = 0
    e2_destroy_index = 0
    e3_destroy_index = 0
    me_destroy_index = 0


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
        for each in big_enemies:
            if each.active:
                each.move()
                if switch:
                    screen.blit(each.image1, each.rect)
                else:
                    screen.blit(each.image2, each.rect)

                # play music
                if each.rect.bottom > - 50:
                    enemy3_fly_sound.play()
            else:
                #  destroy
                enemy3_down_sound.play()
                if not (delay % 3):
                    screen.blit(each.destroy_images[e3_destroy_index], each.rect)
                    e3_destroy_index =  (e3_destroy_index + 1) % 6
                    if e3_destroy_index == 0:
                        each.reset()
        
        for each in mid_enemies:
            if each.active:
                each.move()
                screen.blit(each.image1, each.rect)
            else:
                #  destroy
                enemy2_down_sound.play()
                if not (delay % 3):
                    screen.blit(each.destroy_images[e2_destroy_index], each.rect)
                    e2_destroy_index =  (e2_destroy_index + 1) % 6
                    if e2_destroy_index == 0:
                        each.reset()


        
        for each in small_enemies:
            if each.active:
                each.move()
                screen.blit(each.image1, each.rect)
            else:
                #  destroy
                enemy1_down_sound.play()
                if not (delay % 3):
                    screen.blit(each.destroy_images[e1_destroy_index], each.rect)
                    e1_destroy_index =  (e1_destroy_index + 1) % 4
                    if e1_destroy_index == 0:
                        each.reset()
        # test if get collided
        enemies_down = pygame.sprite.spritecollide(me, enemies, False, pygame.sprite.collide_mask)
        if enemies_down and not me.invincible:
            me.active = False
            for e in enemies_down:
                e.active = False

        #draw plane
        if me.active:
            if switch:
                screen.blit(me.image1, me.rect)
            else:
                screen.blit(me.image2, me.rect)
                me_down_sound.play()
                if not (delay % 3):
                    screen.blit(each.destroy_images[me_destroy_index], each.rect)
                    me_destroy_index =  (me_destroy_index + 1) % 4
                    if me_destroy_index == 0:
                        each.reset()

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