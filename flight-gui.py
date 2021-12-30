import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('SPACE WAR')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
bgImg = pygame.image.load('bg.png')
is_over = False

# background music
pygame.mixer.music.load('bg.wav')
pygame.mixer.music.play(-1)

# hit music
hit_sound = pygame.mixer.Sound('laser.wav')

# score mod
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

def show_score():
    text = f"SCORE: {score}"
    score_render = font.render(text, True, (255, 255, 255))
    screen.blit(score_render, (10, 10))

# over mod
overfont = pygame.font.Font('freesansbold.ttf', 64)
def check_over():
    if is_over:
        over_text = "GAME OVER"
        over_render = overfont.render(over_text, True, (255, 200, 50))
        screen.blit(over_render, (200, 250))

#player
playerImg = pygame.image.load('Plane.png')
px = 400 #player x-axis
py = 500 #player y-axis
ps = 0 #player step
def move_player():
    # set boundaries
    global px
    px += ps
    if px > 736:
        px = 736
    if px < 0:
        px = 0



#enemy
num_of_enemy = 6

class enemy:
    def __init__(self):
        self.Img = pygame.image.load('enemy.png')
        self.x = random.randint(150, 600)
        self.y = random.randint(50, 250)
        self.step = random.randint(2, 6) # enemy step
    
    def reset(self):
        self.x = random.randint(150, 600)
        self.y = random.randint(50, 200)

enemies = []
for i in range(num_of_enemy):
    enemies.append(enemy())

def show_enemy():
    global is_over
    for e in enemies:
        screen.blit(e.Img, (e.x, e.y))
        e.x += e.step
        # set boundaries
        if (e.x > 736 or e.x < 0):
            e.step *= -1
            e.y += 40
            if e.y > 450:
                is_over = True
                enemies.clear()

# bullet
class bullet:
    def __init__(self):               
        self.Img = pygame.image.load('bullet.png')
        self.x = px + 16
        self.y = py + 10
        self.step = 10   #bullet moving speed
    def hit(self):
        global score
        for e in enemies:
            if(distance(self.x, self.y, e.x, e.y) < 30):
                # hit
                hit_sound.play()
                bullets.remove(self)
                e.reset()
                score += 1

bullets = [] # save bullets


# bullet show and move         
def show_bullet():
    for b in bullets:
        screen.blit(b.Img, (b.x, b.y))
        b.hit() # check if hit
        b.y -= b.step
        if b.y < 0:
            bullets.remove(b)

def distance(bx, by, ex, ey):
    a = bx - ex
    b = by - ey
    return math.sqrt(a * a + b * b)




running = True
while running:
    screen.blit(bgImg, (0,0))
    show_score()
    for event in pygame.event.get():
        #quit
        if event.type == pygame.QUIT:
            running == False
            pygame.quit()
            exit()
        # key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ps = 3
            elif event.key == pygame.K_LEFT:
                ps = -3
            elif event.key == pygame.K_SPACE: #shoot
                #create bullet
                b = bullets.append(bullet())
        #keyup then freeze
        if event.type == pygame.KEYUP:
            ps = 0

    screen.blit(playerImg, (px, py))
    
    move_player()
    show_enemy()
    check_over()
    show_bullet()
    
    pygame.display.update()