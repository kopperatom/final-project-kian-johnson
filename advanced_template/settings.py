# pygame template - skeleton for new pygame project
import pygame as pg
import random as r
import os

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
snd_folder = os.path.join(game_folder, 'snd')

WIDTH = 600
HEIGHT = 600
FPS = 60
TITLE = "jumpy!"
FONT_NAME = 'arial'
HS_FILE = "highscore.txt"
SPRITESHEET = "spritesheet_jumper.png"


# player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 22

# game props
BOOST_POWER = 62
POW_SPAWN_PCT = 7
MOB_FREQ = 5000
PLAYER_LAYER = 2
PLATFORM_LAYER = 1
POW_LAYER = 1
MOB_LAYER = 2
CLOUD_LAYER = 0


# starting platform
PLATFORM_LIST = [(0, HEIGHT - 60),
                 (WIDTH / 2 - 50, HEIGHT * 3/ 4 - 50),
                 (125, HEIGHT - 350),
                 (350, 200),
                 (175, 100)]
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
LIGHTBLUE = (0, 155, 155)
BGCOLOR = LIGHTBLUE