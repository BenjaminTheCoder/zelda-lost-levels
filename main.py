# pyxel edit test.pyxres

import pyxel
from dataclasses import dataclass
import random
import math

TILESIZE = 16
SCREEN_WIDTH = 50*TILESIZE
SCREEN_HEIGHT = 40*TILESIZE
WALLCOLOR = 3
MAX_ARROW_FRAMES = 10

pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, fps=15, display_scale=1)
pyxel.load('assets.pyxres')
pyxel.mouse(True)

@dataclass
class Rect:
    x: int
    y: int
    w: int
    h: int
    color: int

@dataclass
class Agent:
    x: int
    y: int
    

@dataclass
class Enemy(Agent):
    health: int
    

@dataclass
class Moblin(Enemy):
   pass 


@dataclass
class Item:
    x: int
    y: int
    name: str
    tile_x: int
    tile_y: int  
 
@dataclass
class ItemWithDirection:
    x: int
    y: int
    tile_x_down: int
    tile_y_down: int      
    tile_x_up: int
    tile_y_up: int
    tile_x_left: int
    tile_y_left: int
    tile_x_right: int
    tile_y_right: int
    alpha: int
 
@dataclass
class Player(Agent):
    inventory: list[Item]
    direction: str
    slashing: bool
    shooting: bool
    arrow_frame: int
    arrow_dir: str
    health: int
    
game_over = False
heart = Item(x = 27 * TILESIZE, y = TILESIZE * 35, name = 'Heart', tile_x = 0, tile_y = 32)
updatedplayer = Player(x = SCREEN_WIDTH // 5, y = SCREEN_HEIGHT // 5, inventory = [], direction = 'down', slashing = False, shooting = False, arrow_frame = 0, arrow_dir = 'up', health = 10)
sword = Item(x = 9*TILESIZE, y = 12*TILESIZE, name = 'Sword', tile_x = 16, tile_y = 0)
slash_sword = ItemWithDirection(x = -10*TILESIZE, y = -10*TILESIZE, tile_x_down = 16, tile_y_down = 32, tile_x_up = 64, tile_y_up = 0, tile_x_left = 48, tile_y_left = 32, tile_x_right = 32, tile_y_right = 32, alpha = 7)
shoot_bow =   ItemWithDirection(x = -20*TILESIZE, y = -20*TILESIZE, tile_x_down = 16, tile_y_down = 64, tile_x_up = 0,  tile_y_up = 64,tile_x_left = 32, tile_y_left = 64, tile_x_right = 48, tile_y_right = 64, alpha = 14)
arrow = ItemWithDirection(x = -30*TILESIZE, y = -30*TILESIZE, tile_x_down = 16, tile_y_down = 48, tile_x_up = 0,  tile_y_up = 48,tile_x_left = 32, tile_y_left = 48, tile_x_right = 48, tile_y_right = 48, alpha = 7)
Din = Item(x=640, y=80, name = 'Zelda', tile_x = 0, tile_y = 112)
bow = Item(x = 26*TILESIZE, y = 19*TILESIZE, name = 'Bow', tile_x = 32, tile_y = 0)
quiver = Item(x = 25*TILESIZE, y = 19*TILESIZE, name = 'Quiver', tile_x = 48 , tile_y = 0)
open_chest = Item(x = -53*TILESIZE, y = -53*TILESIZE, name = 'Open_chest', tile_x = 48, tile_y = 80)
closed_chest = Item(x = 24*TILESIZE, y = 19*TILESIZE, name = 'Closed_chest', tile_x = 32, tile_y = 96)
key = Item(x = -52*TILESIZE, y = -52*TILESIZE, name = 'Key', tile_x = 48, tile_y = 96)
Gannondorf = Moblin(x = 24*TILESIZE, y = 10*TILESIZE, health = 20)
secretdoor1 = Rect(x = 23*TILESIZE, y = 27*TILESIZE, w = 1*TILESIZE, h = 1*TILESIZE, color=WALLCOLOR)
secretdoor2 = Rect(x = 47*TILESIZE, y = 16*TILESIZE, w = 1*TILESIZE, h = 1*TILESIZE, color=WALLCOLOR)
walls = [
        Rect(x = 0*TILESIZE, y = 0*TILESIZE, w = 2*TILESIZE, h = 60*TILESIZE, color=WALLCOLOR),
        Rect(x = 0*TILESIZE, y = 0*TILESIZE, w = 80*TILESIZE, h = 2*TILESIZE, color=WALLCOLOR),
        Rect(x = 0, y = 30*TILESIZE, w = 80*TILESIZE, h = 10*TILESIZE, color=WALLCOLOR), #bottom
        Rect(x = 48*TILESIZE, y = 0*TILESIZE, w = 2*TILESIZE, h = 60*TILESIZE, color=WALLCOLOR), # right
        Rect(x = 16*TILESIZE, y = 0*TILESIZE, w = TILESIZE, h = 7*TILESIZE, color=WALLCOLOR), # done
        Rect(x = 0, y = 16*TILESIZE, w = 8*TILESIZE, h = TILESIZE, color=WALLCOLOR),
        Rect(x = 10*TILESIZE, y = 16*TILESIZE, w = 6*TILESIZE, h = TILESIZE, color=WALLCOLOR),
        Rect(x = 16*TILESIZE, y = 17*TILESIZE, w = 7*TILESIZE, h = 6*TILESIZE, color=WALLCOLOR),
        Rect(x = 16*TILESIZE, y = 27*TILESIZE, w = 7*TILESIZE, h = 4*TILESIZE, color=WALLCOLOR),
        Rect(x = 16*TILESIZE, y = 16*TILESIZE, w = 17*TILESIZE, h = 1*TILESIZE, color=WALLCOLOR),
        Rect(x = 17*TILESIZE, y = 2*TILESIZE, w = 16*TILESIZE, h = 1*TILESIZE, color=WALLCOLOR),
        Rect(x = 32*TILESIZE, y = 2*TILESIZE, w = 1*TILESIZE, h = 7*TILESIZE, color=WALLCOLOR),
        Rect(x = 2*TILESIZE, y = 30*TILESIZE, w = 14*TILESIZE, h = 1*TILESIZE, color=WALLCOLOR),
        Rect(x = 24*TILESIZE, y = 27*TILESIZE, w = 9*TILESIZE, h = 1*TILESIZE, color=WALLCOLOR),
        Rect(x = 32*TILESIZE, y = 17*TILESIZE, w = 1*TILESIZE, h = 11*TILESIZE, color=WALLCOLOR),
        Rect(x = 32*TILESIZE, y = 16*TILESIZE, w = 15*TILESIZE, h = 1*TILESIZE, color=WALLCOLOR),
        Rect(x = 16*TILESIZE, y = 14*TILESIZE, w = 1*TILESIZE, h = 2*TILESIZE, color=WALLCOLOR),
        Rect(x = 32*TILESIZE, y = 14*TILESIZE, w = 1*TILESIZE, h = 2*TILESIZE, color=WALLCOLOR),

    ]

doors = [
        Rect(x=256, y=112, w=16, h=112, color=0),
        Rect(x=128, y=256, w=32, h=16, color=4),
        Rect(x=256, y=368, w=16, h=64, color=13),
        Rect(x=512, y=144, w=16, h=80, color=7)

    
    
    ]

Room1Moblins = [
        Moblin(x = 5*TILESIZE, y = 26*TILESIZE, health = 5),
        Moblin(x = 5*TILESIZE, y = 20*TILESIZE, health = 5),
        Moblin(x = 8*TILESIZE, y = 27*TILESIZE, health = 5),
        Moblin(x = 13*TILESIZE, y = 25*TILESIZE, health = 5),
        Moblin(x = 13*TILESIZE, y = 21*TILESIZE, health = 5),
    ]

SecretRoomMoblins = [        
        Moblin(x = 42*TILESIZE, y = 26*TILESIZE, health = 5),
        Moblin(x = 38*TILESIZE, y = 22*TILESIZE, health = 5),
        Moblin(x = 35*TILESIZE, y = 19*TILESIZE, health = 5),
    ]


dr1 = Rect(x = 256-TILESIZE, y = 112, w = 16, h = 112, color=7)
dr2 = Rect(x=128, y=256 - TILESIZE, w=32, h=16, color=4)
dr3 = Rect(x=256 - TILESIZE, y=368, w=16, h=64, color=13)
dr4 = Rect(x=496, y=144, w=16, h=80, color=7)


def reset_game():
    global game_over, heart, updatedplayer, sword, slash_sword, shoot_bow, arrow, Din, bow, quiver
    global open_chest, closed_chest, key, Gannondorf, secretdoor1, secretdoor2, walls, doors
    global Room1Moblins, SecretRoomMoblins, dr1, dr2, dr3, dr4
    game_over = False
    heart = Item(x = 27 * TILESIZE, y = TILESIZE * 35, name = 'Heart', tile_x = 0, tile_y = 32)
    updatedplayer = Player(x = SCREEN_WIDTH // 5, y = SCREEN_HEIGHT // 5, inventory = [], direction = 'down', slashing = False, shooting = False, arrow_frame = 0, arrow_dir = 'up', health = 10)
    sword = Item(x = 9*TILESIZE, y = 12*TILESIZE, name = 'Sword', tile_x = 16, tile_y = 0)
    slash_sword = ItemWithDirection(x = -10*TILESIZE, y = -10*TILESIZE, tile_x_down = 16, tile_y_down = 32, tile_x_up = 64, tile_y_up = 0, tile_x_left = 48, tile_y_left = 32, tile_x_right = 32, tile_y_right = 32, alpha = 7)
    shoot_bow =   ItemWithDirection(x = -20*TILESIZE, y = -20*TILESIZE, tile_x_down = 16, tile_y_down = 64, tile_x_up = 0,  tile_y_up = 64,tile_x_left = 32, tile_y_left = 64, tile_x_right = 48, tile_y_right = 64, alpha = 14)
    arrow = ItemWithDirection(x = -30*TILESIZE, y = -30*TILESIZE, tile_x_down = 16, tile_y_down = 48, tile_x_up = 0,  tile_y_up = 48,tile_x_left = 32, tile_y_left = 48, tile_x_right = 48, tile_y_right = 48, alpha = 7)
    Din = Item(x=640, y=80, name = 'Zelda', tile_x = 0, tile_y = 112)
    bow = Item(x = 26*TILESIZE, y = 19*TILESIZE, name = 'Bow', tile_x = 32, tile_y = 0)
    quiver = Item(x = 25*TILESIZE, y = 19*TILESIZE, name = 'Quiver', tile_x = 48 , tile_y = 0)
    open_chest = Item(x = -53*TILESIZE, y = -53*TILESIZE, name = 'Open_chest', tile_x = 48, tile_y = 80)
    closed_chest = Item(x = 24*TILESIZE, y = 19*TILESIZE, name = 'Closed_chest', tile_x = 32, tile_y = 96)
    key = Item(x = -52*TILESIZE, y = -52*TILESIZE, name = 'Key', tile_x = 48, tile_y = 96)
    Gannondorf = Moblin(x = 24*TILESIZE, y = 10*TILESIZE, health = 20)
    secretdoor1 = Rect(x = 23*TILESIZE, y = 27*TILESIZE, w = 1*TILESIZE, h = 1*TILESIZE, color=WALLCOLOR)
    secretdoor2 = Rect(x = 47*TILESIZE, y = 16*TILESIZE, w = 1*TILESIZE, h = 1*TILESIZE, color=WALLCOLOR)
    walls = [
            Rect(x = 0*TILESIZE, y = 0*TILESIZE, w = 2*TILESIZE, h = 60*TILESIZE, color=WALLCOLOR),
            Rect(x = 0*TILESIZE, y = 0*TILESIZE, w = 80*TILESIZE, h = 2*TILESIZE, color=WALLCOLOR),
            Rect(x = 0, y = 30*TILESIZE, w = 80*TILESIZE, h = 10*TILESIZE, color=WALLCOLOR), #bottom
            Rect(x = 48*TILESIZE, y = 0*TILESIZE, w = 2*TILESIZE, h = 60*TILESIZE, color=WALLCOLOR), # right
            Rect(x = 16*TILESIZE, y = 0*TILESIZE, w = TILESIZE, h = 7*TILESIZE, color=WALLCOLOR), # done
            Rect(x = 0, y = 16*TILESIZE, w = 8*TILESIZE, h = TILESIZE, color=WALLCOLOR),
            Rect(x = 10*TILESIZE, y = 16*TILESIZE, w = 6*TILESIZE, h = TILESIZE, color=WALLCOLOR),
            Rect(x = 16*TILESIZE, y = 17*TILESIZE, w = 7*TILESIZE, h = 6*TILESIZE, color=WALLCOLOR),
            Rect(x = 16*TILESIZE, y = 27*TILESIZE, w = 7*TILESIZE, h = 4*TILESIZE, color=WALLCOLOR),
            Rect(x = 16*TILESIZE, y = 16*TILESIZE, w = 17*TILESIZE, h = 1*TILESIZE, color=WALLCOLOR),
            Rect(x = 17*TILESIZE, y = 2*TILESIZE, w = 16*TILESIZE, h = 1*TILESIZE, color=WALLCOLOR),
            Rect(x = 32*TILESIZE, y = 2*TILESIZE, w = 1*TILESIZE, h = 7*TILESIZE, color=WALLCOLOR),
            Rect(x = 2*TILESIZE, y = 30*TILESIZE, w = 14*TILESIZE, h = 1*TILESIZE, color=WALLCOLOR),
            Rect(x = 24*TILESIZE, y = 27*TILESIZE, w = 9*TILESIZE, h = 1*TILESIZE, color=WALLCOLOR),
            Rect(x = 32*TILESIZE, y = 17*TILESIZE, w = 1*TILESIZE, h = 11*TILESIZE, color=WALLCOLOR),
            Rect(x = 32*TILESIZE, y = 16*TILESIZE, w = 15*TILESIZE, h = 1*TILESIZE, color=WALLCOLOR),
            Rect(x = 16*TILESIZE, y = 14*TILESIZE, w = 1*TILESIZE, h = 2*TILESIZE, color=WALLCOLOR),
            Rect(x = 32*TILESIZE, y = 14*TILESIZE, w = 1*TILESIZE, h = 2*TILESIZE, color=WALLCOLOR),

        ]

    doors = [
            Rect(x=256, y=112, w=16, h=112, color=0),
            Rect(x=128, y=256, w=32, h=16, color=4),
            Rect(x=256, y=368, w=16, h=64, color=13),
            Rect(x=512, y=144, w=16, h=80, color=7)

        
        
        ]

    Room1Moblins = [
            Moblin(x = 5*TILESIZE, y = 26*TILESIZE, health = 5),
            Moblin(x = 5*TILESIZE, y = 20*TILESIZE, health = 5),
            Moblin(x = 8*TILESIZE, y = 27*TILESIZE, health = 5),
            Moblin(x = 13*TILESIZE, y = 25*TILESIZE, health = 5),
            Moblin(x = 13*TILESIZE, y = 21*TILESIZE, health = 5),
        ]

    SecretRoomMoblins = [        
            Moblin(x = 42*TILESIZE, y = 26*TILESIZE, health = 5),
            Moblin(x = 38*TILESIZE, y = 22*TILESIZE, health = 5),
            Moblin(x = 35*TILESIZE, y = 19*TILESIZE, health = 5),
        ]


    dr1 = Rect(x = 256-TILESIZE, y = 112, w = 16, h = 112, color=7)
    dr2 = Rect(x=128, y=256 - TILESIZE, w=32, h=16, color=4)
    dr3 = Rect(x=256 - TILESIZE, y=368, w=16, h=64, color=13)
    dr4 = Rect(x=496, y=144, w=16, h=80, color=7)


def Are_room_1_Moblins_dead(Room1Moblins):
    deadcount = 0
    for moblin in Room1Moblins:
        if moblin.health == 0:
            deadcount += 1
    if deadcount == len(Room1Moblins):
        return True
    else:
        return False


def canYouGoThere(nextX, nextY):
    canGo = True
    for wall in walls:
        if nextX >= wall.x and nextX < wall.x + wall.w and nextY >= wall.y and nextY < wall.h + wall.y:
            canGo = False
    for door in doors:
        if nextX >= door.x and nextX < door.x + door.w and nextY >= door.y and nextY < door.h + door.y:
            canGo = False
    return canGo

def getDebugRect():
    x = (pyxel.mouse_x // TILESIZE) * TILESIZE
    y = (pyxel.mouse_y // TILESIZE) * TILESIZE
    w = (updatedplayer.x - x)
    h = (updatedplayer.y - y)
    color = 11
    return Rect(x, y, w, h, color)

def absolute_to_tilesize(rect):
    x = rect.x // TILESIZE
    y = rect.y // TILESIZE
    w = rect.w // TILESIZE
    h = rect.h // TILESIZE
    color = rect.color
    return f'Rect(x = {x}*TILESIZE, y = {y}*TILESIZE, w = {w}*TILESIZE, h = {h}*TILESIZE, color=WALLCOLOR)'


def updateWeaponPosition(weapon):
    if updatedplayer.direction == 'down':
        weapon.x = updatedplayer.x
        weapon.y = updatedplayer.y + TILESIZE
    elif updatedplayer.direction == 'up':
        weapon.x = updatedplayer.x
        weapon.y = updatedplayer.y - TILESIZE
    elif updatedplayer.direction == 'right':
        weapon.x = updatedplayer.x + TILESIZE
        weapon.y = updatedplayer.y
    elif updatedplayer.direction == 'left':
        weapon.x = updatedplayer.x - TILESIZE
        weapon.y = updatedplayer.y

def updateArrowPosition(arrow):
    if updatedplayer.arrow_frame == MAX_ARROW_FRAMES:
        updatedplayer.arrow_frame = 0
    if updatedplayer.shooting and updatedplayer.arrow_frame == 0:
        updatedplayer.arrow_frame += 1
        updatedplayer.arrow_dir = updatedplayer.direction
        arrow.x = updatedplayer.x
        arrow.y = updatedplayer.y
    if updatedplayer.arrow_frame > 0:
        updatedplayer.arrow_frame += 1
#     print('updatedplayer.arrow_frame', updatedplayer.arrow_frame)    
    if updatedplayer.arrow_dir == 'down':
        arrow.y += TILESIZE
    elif updatedplayer.arrow_dir == 'up':
        arrow.y -= TILESIZE
    elif updatedplayer.arrow_dir == 'right':
        arrow.x += TILESIZE
    elif updatedplayer.arrow_dir == 'left':
        arrow.x -= TILESIZE


def vector2D(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    mag = math.sqrt(dx**2 + dy**2)
    if mag == 0:
        return (0, 0)
    dxn = dx/mag
    if dxn >= 0:
        dxn = math.ceil(dxn)
    else:
        dxn = math.floor(dxn)
    dyn = dy/mag
    if dyn >= 0:
        dyn = math.ceil(dyn)
    else:
        dyn = math.floor(dyn)
    return (dxn, dyn)

def debugVector2D():
    x1 = (pyxel.mouse_x // TILESIZE) * TILESIZE
    y1 = (pyxel.mouse_y // TILESIZE) * TILESIZE
    x2 = updatedplayer.x
    y2 = updatedplayer.y
    print(vector2D(x1, y1, x2, y2))

def update():
    global game_over
    updateWeaponPosition(slash_sword)
    updateWeaponPosition(shoot_bow)
    updateArrowPosition(arrow)
    updatedplayer.slashing = False
    updatedplayer.shooting = False
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    #elif pyxel.btnp(pyxel.KEY_P):
        #print(getDebugRect())
    elif pyxel.btnp(pyxel.KEY_SPACE):
        updatedplayer.slashing = True
    elif pyxel.btnp(pyxel.KEY_B):
        updatedplayer.shooting = True
    elif pyxel.btnp(pyxel.KEY_LEFT, repeat=1):
        updatedplayer.direction = 'left'
        nextX = updatedplayer.x - TILESIZE
        nextY = updatedplayer.y
        canGo = canYouGoThere(nextX, nextY)
        if canGo:
            updatedplayer.x -= TILESIZE
    elif pyxel.btnp(pyxel.KEY_RIGHT, repeat=1):
        updatedplayer.direction = 'right'
        nextX = updatedplayer.x + TILESIZE
        nextY = updatedplayer.y
        canGo = canYouGoThere(nextX, nextY)
        if canGo:
            updatedplayer.x += TILESIZE
    elif pyxel.btnp(pyxel.KEY_DOWN, repeat=1):
        updatedplayer.direction = 'down'
        nextX = updatedplayer.x
        nextY = updatedplayer.y + TILESIZE
        canGo = canYouGoThere(nextX, nextY)
        if canGo:
            updatedplayer.y += TILESIZE
    elif pyxel.btnp(pyxel.KEY_UP, repeat=1):
        updatedplayer.direction = 'up'
        nextX = updatedplayer.x
        nextY = updatedplayer.y - TILESIZE
        canGo = canYouGoThere(nextX, nextY)
        if canGo:
            updatedplayer.y -= TILESIZE
            
    if updatedplayer.x == sword.x and updatedplayer.y == sword.y:
        updatedplayer.inventory.append(sword)
        sword.x = TILESIZE * 5
        sword.y = TILESIZE * 35
        #print(updatedplayer.inventory)
    elif updatedplayer.x == bow.x and updatedplayer.y == bow.y:
        updatedplayer.inventory.append(bow)
        bow.x = TILESIZE * 7
        bow.y = TILESIZE * 35
        # print(updatedplayer.inventory)
    elif updatedplayer.x == quiver.x and updatedplayer.y == quiver.y:
        updatedplayer.inventory.append(sword)
        quiver.x = TILESIZE * 9
        quiver.y = TILESIZE * 35
    #print(updatedplayer.direction)    
    if sword not in updatedplayer.inventory:
        updatedplayer.slashing = False
    if bow not in updatedplayer.inventory and quiver not in updatedplayer.inventory:
        updatedplayer.shooting = False
    for moblin in Room1Moblins:
        if random.random() < 0.05:
            stepX, stepY = vector2D(moblin.x, moblin.y, updatedplayer.x, updatedplayer.y)            
            canGo = canYouGoThere(moblin.x + stepX * TILESIZE, moblin.y + stepY * TILESIZE)
            if canGo:
                moblin.x += stepX*TILESIZE
                moblin.y += stepY*TILESIZE
        if slash_sword.x == moblin.x and slash_sword.y == moblin.y and updatedplayer.slashing == True:
            moblin.health -= 1
        if arrow.x == moblin.x and arrow.y == moblin.y:
            moblin.health -= 1
            updatedplayer.arrow_frame = 0
        if updatedplayer.x == moblin.x and updatedplayer.y == moblin.y and random.random() < 0.3:
            updatedplayer.health -= 1
        if moblin.health <= 0:
           moblin.x = -70
           moblin.y = -70
           
    for moblin in SecretRoomMoblins:
        if random.random() < 0.05:
            stepX, stepY = vector2D(moblin.x, moblin.y, updatedplayer.x, updatedplayer.y)            
            canGo = canYouGoThere(moblin.x + stepX * TILESIZE, moblin.y + stepY * TILESIZE)
            if canGo:
                moblin.x += stepX*TILESIZE
                moblin.y += stepY*TILESIZE
        if slash_sword.x == moblin.x and slash_sword.y == moblin.y and updatedplayer.slashing == True:
            moblin.health -= 1
        if arrow.x == moblin.x and arrow.y == moblin.y:
            moblin.health -= 1
            updatedplayer.arrow_frame = 0
        if updatedplayer.x == moblin.x and updatedplayer.y == moblin.y and random.random() < 0.3:
            updatedplayer.health -= 1
        if moblin.health <= 0:
           moblin.x = -70
           moblin.y = -70
           
           
    if random.random() < 0.05:
        stepX, stepY = vector2D(Gannondorf.x, Gannondorf.y, updatedplayer.x, updatedplayer.y)
        canGo1 = canYouGoThere(Gannondorf.x + stepX * TILESIZE, Gannondorf.y + stepY * TILESIZE)
        canGo2 = canYouGoThere((Gannondorf.x + stepX * TILESIZE) + TILESIZE, (Gannondorf.y + stepY * TILESIZE) + TILESIZE)
        if canGo1 and canGo2:
            Gannondorf.x += stepX*TILESIZE
            Gannondorf.y += stepY*TILESIZE
        
    if slash_sword.x >= Gannondorf.x and slash_sword.x < Gannondorf.x + TILESIZE*2 and slash_sword.y >= Gannondorf.y and slash_sword.y < Gannondorf.y + TILESIZE*2 and updatedplayer.slashing == True:
        Gannondorf.health -= 1
    if arrow.x >= Gannondorf.x and arrow.x < Gannondorf.x + TILESIZE*2 and arrow.y >= Gannondorf.y and arrow.y < Gannondorf.y + TILESIZE*2:
        Gannondorf.health -= 1
        updatedplayer.arrow_frame = 0
    if updatedplayer.x >= Gannondorf.x and updatedplayer.x < Gannondorf.x + TILESIZE*2 and updatedplayer.y >= Gannondorf.y and updatedplayer.y < Gannondorf.y + TILESIZE*2 and random.random() < 0.3:
        updatedplayer.health -= 2
    if Gannondorf.health <= 0:
       Gannondorf.x = -70
       Gannondorf.y = -70
        
    if closed_chest.x == updatedplayer.x and closed_chest.y == updatedplayer.y:
        updatedplayer.inventory.append(key)
        closed_chest.x = -53
        closed_chest.y = -53
        open_chest.x = 24*TILESIZE
        open_chest.y = 19*TILESIZE
        key.x = TILESIZE * 11
        key.y = TILESIZE * 35
    for door in doors:
        for moblin in Room1Moblins:
            if door.color == 0 and key in updatedplayer.inventory and updatedplayer.x >= dr1.x and updatedplayer.x < dr1.x+dr1.w and updatedplayer.y >= dr1.y and updatedplayer.y < dr1.y+dr1.h:
                door.x = -1000000
                door.x = -1000000
            if door.color == 4 and updatedplayer.x >= dr2.x and updatedplayer.x < dr2.x+dr2.w and updatedplayer.y >= dr2.y and updatedplayer.y < dr2.y+dr2.h:
                door.x = -1000000
                door.x = -1000000
            if door.color == 13 and updatedplayer.x >= dr3.x and updatedplayer.x < dr3.x+dr3.w and updatedplayer.y >= dr3.y and updatedplayer.y < dr3.y+dr3.h and Are_room_1_Moblins_dead(Room1Moblins) == True:
                door.x = -1000000
                door.x = -1000000
            if door.color == 7 and updatedplayer.x >= dr4.x and updatedplayer.x < dr4.x+dr4.w and updatedplayer.y >= dr4.y and updatedplayer.y < dr4.y+dr4.h:
                door.x = -1000000
                door.x = -1000000

    if pyxel.btnp(pyxel.KEY_R, repeat=1) and game_over == True:
        reset_game()
            
    if updatedplayer.health <= 0:
        game_over = True
        

def draw():
    if game_over == True:
        pyxel.cls(0)
        pyxel.blt(255, 255, 2, 0, 0, 255, 31)
        pyxel.text(350, 300, "PRESS R TO RESTART", 8)
        
    else:
        pyxel.cls(5)
        for door in doors:
            pyxel.rect(door.x, door.y, door.w, door.h, door.color)    
        for wall in walls:
            pyxel.rect(wall.x, wall.y, wall.w, wall.h, wall.color)
        #debug_rect = getDebugRect()
        for i in range(updatedplayer.health):        
            pyxel.blt(heart.x + (i * TILESIZE * 2), heart.y, 0, heart.tile_x, heart.tile_y, TILESIZE, TILESIZE, 7)
        for moblin1 in Room1Moblins:
            for moblin2 in SecretRoomMoblins:
                pyxel.blt(sword.x, sword.y, 0, sword.tile_x, sword.tile_y, TILESIZE, TILESIZE, 14)
                pyxel.blt(bow.x, bow.y, 0, bow.tile_x, bow.tile_y, TILESIZE, TILESIZE, 14)
                pyxel.blt(quiver.x, quiver.y, 0, quiver.tile_x, quiver.tile_y, TILESIZE, TILESIZE, 14)
                pyxel.blt(closed_chest.x, closed_chest.y, 0, closed_chest.tile_x, closed_chest.tile_y, TILESIZE, TILESIZE)
                pyxel.blt(open_chest.x, open_chest.y, 0, open_chest.tile_x, open_chest.tile_y, TILESIZE, TILESIZE)
                pyxel.blt(key.x, key.y, 0, key.tile_x, key.tile_y, TILESIZE, TILESIZE, 7)
                pyxel.blt(Gannondorf.x, Gannondorf.y, 0, 0, 80, 2*TILESIZE, 2*TILESIZE, 14)
                pyxel.blt(Din.x, Din.y, 0, Din.tile_x, Din.tile_y, TILESIZE, TILESIZE, 14)
                pyxel.blt(moblin1.x, moblin1.y, 0, 32, 80, TILESIZE, TILESIZE, 14)
                pyxel.blt(moblin2.x, moblin2.y, 0, 32, 80, TILESIZE, TILESIZE, 14)

        #pyxel.rect(debug_rect.x, debug_rect.y, debug_rect.w, debug_rect.h, debug_rect.color)
        if updatedplayer.direction == 'down':
            pyxel.blt(updatedplayer.x, updatedplayer.y, 0, 0, 0, 16, 16, 7)
        elif updatedplayer.direction == 'up':
            pyxel.blt(updatedplayer.x, updatedplayer.y, 0, 32, 16, 16, 16, 7)
        elif updatedplayer.direction == 'left':
            pyxel.blt(updatedplayer.x, updatedplayer.y, 0, 48, 16, 16, 16, 7)    
        elif updatedplayer.direction == 'right':
            pyxel.blt(updatedplayer.x, updatedplayer.y, 0, 64, 16, 16, 16, 7)
            
        if updatedplayer.slashing == True:    
            if updatedplayer.direction == 'down':
                pyxel.blt(slash_sword.x, slash_sword.y, 0, slash_sword.tile_x_down, slash_sword.tile_y_down, TILESIZE, TILESIZE, slash_sword.alpha)
            elif updatedplayer.direction == 'up':
                pyxel.blt(slash_sword.x, slash_sword.y, 0, slash_sword.tile_x_up, slash_sword.tile_y_up, TILESIZE, TILESIZE, slash_sword.alpha)
            elif updatedplayer.direction == 'right':
                pyxel.blt(slash_sword.x, slash_sword.y, 0, slash_sword.tile_x_right, slash_sword.tile_y_right, TILESIZE, TILESIZE, slash_sword.alpha)
            elif updatedplayer.direction == 'left':
                pyxel.blt(slash_sword.x, slash_sword.y, 0, slash_sword.tile_x_left, slash_sword.tile_y_left, TILESIZE, TILESIZE, slash_sword.alpha)
                
        if updatedplayer.arrow_frame > 0:       
            if updatedplayer.arrow_dir == 'down':
                pyxel.blt(shoot_bow.x, shoot_bow.y, 0, shoot_bow.tile_x_down, shoot_bow.tile_y_down, TILESIZE, TILESIZE, shoot_bow.alpha)
                pyxel.blt(arrow.x, arrow.y, 0, arrow.tile_x_down, arrow.tile_y_down, TILESIZE, TILESIZE, arrow.alpha)
            elif updatedplayer.arrow_dir == 'up':
                pyxel.blt(shoot_bow.x, shoot_bow.y, 0, shoot_bow.tile_x_up, shoot_bow.tile_y_up, TILESIZE, TILESIZE, shoot_bow.alpha)
                pyxel.blt(arrow.x, arrow.y, 0, arrow.tile_x_up, arrow.tile_y_up, TILESIZE, TILESIZE, arrow.alpha)            
            elif updatedplayer.arrow_dir == 'right':
                pyxel.blt(shoot_bow.x, shoot_bow.y, 0, shoot_bow.tile_x_right, shoot_bow.tile_y_right, TILESIZE, TILESIZE, shoot_bow.alpha)
                pyxel.blt(arrow.x, arrow.y, 0, arrow.tile_x_right, arrow.tile_y_right, TILESIZE, TILESIZE, arrow.alpha)
            elif updatedplayer.arrow_dir == 'left':
                pyxel.blt(shoot_bow.x, shoot_bow.y, 0, shoot_bow.tile_x_left, shoot_bow.tile_y_left, TILESIZE, TILESIZE, shoot_bow.alpha)
                pyxel.blt(arrow.x, arrow.y, 0, arrow.tile_x_left, arrow.tile_y_left, TILESIZE, TILESIZE, arrow.alpha)    

        pyxel.rect(secretdoor1.x, secretdoor1.y, secretdoor1.w, secretdoor1.h, WALLCOLOR)
        pyxel.rect(secretdoor2.x, secretdoor2.y, secretdoor2.w, secretdoor2.h, WALLCOLOR)        

pyxel.run(update, draw)