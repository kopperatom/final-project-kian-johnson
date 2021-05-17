import math
import pygame as pg
import random
import os

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"imgs")
print(img_folder)


class Npc(pg.sprite.Sprite):
    def __init__(self):
        super(Npc, self).__init__()
        self.image = pg.Surface((15,15))
        self.image.fill(COBALT_BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT/2)
        self.speedx = 5
        self.speedy = 5
        self.center_x = self.rect.centerx
        self.center_y = self.rect.centery
        #current angle
        self.angle = 1
        # how far away from the center to orbit, in pixels
        self.radius = 100
        # how fast to orbit, in radians per frame
        self.speed = .5


    def update(self):

        # if self.angle <= 6.25:
        #      print(self.angle)
        #     self.rect.centerx = self.radius *math.sin(self.angle)+self.center_x
        #     self.rect.centery = self.radius *math.cos(self.angle)+self.center_y
        #     self.angle+=self.speed

        #self.rect.y+= self.speedx
        #self.rect.y+=5
        #if self.rect.left > WIDTH:
        #if self.rect.right = 0
        #if self.rect.right > WIDTH:
            #self.rect.left = 0
        #if self.rect.centery > HEIGHT:
            #self.rect.centery = 0
        #if self.rect.centerx > WIDTH:
            #self.rect.centery = 0
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.left <=0 or self.rect.right >= WIDTH:
            self.speedx *= -1
        if self.rect.top <=0 or self.rect.bottom >=HEIGHT:
            self.speedy *= -1

        # if self.rect.centerx > WIDTH/2:
        #     self.speedx = 5
        #     self.speedy = -5
        #
        # if self.rect.centery > HEIGHT/2:
        #     self.speedx = 5
        #     self.speedy = 0


        #screen warping
        # if self.rect.left > WIDTH:
        #     self.rect.top= HEIGHT
        #     self.rect.centerx=WIDTH/2
        #     self.speedx = 0
        #     self.speedy= -5

        # if self.rect.bottom < 0:
        #     print(self.rect.right)
        #     self.rect.right = 0
        #     self.rect.centery=HEIGHT/2
        #     self.speedx = 5
        #     self.speedy = 0

        # if self.rect.right == WIDTH:
        #     self.speedx = 0
        #     self.speedy = -5
        #
        # if self.rect.top == 0:
        #     self.speedx = -5
        #     self.speedy = 0
        #
        # if self.rect.left == 0:
        #     self.speedx = 0
        #     self.speedy = 5
        #
        # if self.rect.bottom == HEIGHT and self.rect.right != WIDTH:
        #     self.speedx = 5
        #     self.speedy = 0


class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pg.Surface((50,50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT/2)
        self.speedx = 0
        self.speedy = 0
        self.keypressed = False

    def toggle_pressed(self):
        self.keypressed = False

    def update(self):

        #mouse movent
        if mouse_buttn_held:
            self.rect.center = (mousex,mousey)


        #grid movement
        # keystate = pg.key.get_pressed()
        # if keystate[pg.K_LEFT] and self.keypressed == False:
        #     self.keypressed = True
        #     self.rect.centerx += -50
        # if keystate[pg.K_RIGHT] and self.keypressed == False:
        #     self.rect.centerx += 50
        #     self.keypressed = True
        # if keystate[pg.K_UP] and self.keypressed == False:
        #     self.rect.centery += -50
        #     self.keypressed = True
        # if keystate[pg.K_DOWN] and self.keypressed == False:
        #     self.rect.centery += 50
        #     self.keypressed = True

        # basic movement
        # self.speedx = 0
        # self.speedy = 0
        # keystate = pg.key.get_pressed()
        # if keystate[pg.K_LEFT]:
        #     self.speedx += -10
        # if keystate[pg.K_RIGHT]:
        #     self.speedx = 10
        # if keystate[pg.K_UP]:
        #     self.speedy = -10
        # if keystate[pg.K_DOWN]:
        #     self.speedy = 10

        self.rect.x += self.speedx
        self.rect.y += self.speedy


        # bind player to screen
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH



def spawn_player(x,y):
    newplayer = Player()
    newplayer.rect.center = (x,y)
    newplayer.speedx = random.randint(-10, 10)
    newplayer.speedy = random.randint(-10,10)
    all_Sprites.add(newplayer)
    players_group.add(newplayer)



WIDTH = 360
HEIGHT = 480
FPS = 70
title = "Template"

# colors (r,g,b)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (128,0,128)
ORANGE = (255,165,0)
YELLOW = (255,255,0)
PINK = (255,182,193)
COBALT_BLUE = (0,80,181)

mouse_buttn_held = False

pg.init()
pg.mixer.init()

screen=pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption(title)
clock = pg.time.Clock()

# create sprite groups
all_Sprites = pg.sprite.Group()
players_group = pg.sprite.Group()
npc_group = pg.sprite.Group()
# create game object
player = Player()
npc = Npc()


# add objects to sprite groups
all_Sprites.add(player)
players_group.add(player)
all_Sprites.add(npc)
players_group.add(npc)


# Game Loop
running = True
while running:
    clock.tick(FPS)
    #process input
    # getting a list of events
    mousex,mousey = pg.mouse.get_pos()
    print(mousex,mousey)
    for event in pg.event.get():
        # if event.type == pg.KEYDOWN:
        #     if event.key == pg.K_LEFT:
        #         print("test")
        #         player.speedx = -5
        #     if event.key == pg.K_RIGHT:
        #         player.speedx = 5
        #     if event.key == pg.K_UP:
        #         player.speedy = -5
        #     if event.key == pg.K_DOWN:
        #         player.speedy = 5



            # basic grid movement
            # if event.key == pg.K_LEFT:
            #     player.rect.x -= 50
            # if event.key == pg.K_RIGHT:
            #     player.rect.x += 50
            # if event.key == pg.K_UP:
            #     player.rect.y -= 50
            # if event.key == pg.K_DOWN:
            #     player.rect.y += 50
            # if event.key == pg.K_KP4:
            #     player.rect.x -= 50
            # if event.key == pg.K_KP6:
            #     player.rect.x += 50
            # if event.key == pg.K_KP8:
            #     player.rect.y -= 50
            # if event.key == pg.K_KP2:
            #     player.rect.y += 50
            # if event.key == pg.K_a:
            #     player.rect.x -= 50
            # if event.key == pg.K_d:
            #     player.rect.x += 50
            # if event.key == pg.K_w:
            #     player.rect.y -= 50
            # if event.key == pg.K_s:
            #     player.rect.y += 50
        if event.type == pg.KEYUP:
            if event.type == pg.K_LEFT or event.key == pg.K_RIGHT:
                player.toggle_pressed()
            if event.type == pg.K_UP or event.key == pg.K_DOWN:
                player.toggle_pressed()
        if event.type == pg.MOUSEBUTTONDOWN and player.rect.collidepoint(pg.mouse.get_pos()):
            x = pg.mouse.get_pressed()
            if x[0]:
                print("clicked left button")
                mouse_buttn_held = True
            if x[1]:
                print("clicked wheel")
            if x[2]:
                spawn_player(mousex,mousey)
                print("clicked right button")
            print("clicked on player")
        if event.type == pg.MOUSEBUTTONUP and mouse_buttn_held == True:
            print("released left button")
            mouse_buttn_held = False

        #     if event.key == pg.K_LEFT:
        #         player.speedx = 0
        #     if event.key == pg.K_RIGHT:
        #         player.speedx = 0
        #     if event.key == pg.K_UP:
        #         player.speedy = 0
        #     if event.key == pg.K_DOWN:
        #         player.speedy = 0

        # checking events to preform actions
        if event.type == pg.QUIT:
            running = False

    # make updates
    all_Sprites.update()


    # render (draw)
    screen.fill(PINK)
    all_Sprites.draw(screen)

    # last thing we do in the loop
    pg.display.flip()


pg.quit()