# pyxel edit test.pyxres

import pyxel
from dataclasses import dataclass

TILESIZE = 16
SCREEN_WIDTH = 50*TILESIZE
SCREEN_HEIGHT = 40*TILESIZE
WALLCOLOR = 3

pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, fps=15, display_scale=1)
pyxel.load('test.pyxres')
pyxel.mouse(False)

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

    
updatedplayer = Player(x = SCREEN_WIDTH // 5, y = SCREEN_HEIGHT // 5, inventory = [], direction = 'down', slashing = False, shooting = False)
dummy = Moblin(x =  TILESIZE * 7, y = TILESIZE * 7, health = 3)
sword = Item(x = 9*TILESIZE, y = 12*TILESIZE, name = 'Sword', tile_x = 16, tile_y = 0)
slash_sword = ItemWithDirection(x = -10*TILESIZE, y = -10*TILESIZE, tile_x_down = 16, tile_y_down = 32, tile_x_up = 64, tile_y_up = 0, tile_x_left = 48, tile_y_left = 32, tile_x_right = 32, tile_y_right = 32, alpha = 7)
shoot_bow =   ItemWithDirection(x = -20*TILESIZE, y = -20*TILESIZE, tile_x_down = 16, tile_y_down = 64, tile_x_up = 0,  tile_y_up = 64,tile_x_left = 32, tile_y_left = 64, tile_x_right = 48, tile_y_right = 64, alpha = 14)
arrow = ItemWithDirection(x = -30*TILESIZE, y = -30*TILESIZE, tile_x_down = 16, tile_y_down = 48, tile_x_up = 0,  tile_y_up = 48,tile_x_left = 32, tile_y_left = 48, tile_x_right = 48, tile_y_right = 48, alpha = 7)
bow = Item(x = 26*TILESIZE, y = 19*TILESIZE, name = 'Bow', tile_x = 32, tile_y = 0)
quiver = Item(x = 25*TILESIZE, y = 19*TILESIZE, name = 'Quiver', tile_x = 48 , tile_y = 0)
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
        Rect(x = 24*TILESIZE, y = 27*TILESIZE, w = 10*TILESIZE, h = 1*TILESIZE, color=WALLCOLOR),
        Rect(x = 32*TILESIZE, y = 17*TILESIZE, w = 1*TILESIZE, h = 11*TILESIZE, color=WALLCOLOR),
        Rect(x = 32*TILESIZE, y = 16*TILESIZE, w = 15*TILESIZE, h = 1*TILESIZE, color=WALLCOLOR),
        Rect(x = 16*TILESIZE, y = 14*TILESIZE, w = 1*TILESIZE, h = 2*TILESIZE, color=WALLCOLOR),
        Rect(x = 32*TILESIZE, y = 14*TILESIZE, w = 1*TILESIZE, h = 2*TILESIZE, color=WALLCOLOR),

    ]

def canYouGoThere(nextX, nextY):
    canGo = True
    for wall in walls:
        if nextX >= wall.x and nextX < wall.x + wall.w and nextY >= wall.y and nextY < wall.h + wall.y:
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

def updateArrowPosition(weapon):
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



def update():
    updateWeaponPosition(slash_sword)
    updateWeaponPosition(shoot_bow)
    updateArrowPosition(arrow)
    updatedplayer.slashing = False
    updatedplayer.shooting = False
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
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
    if slash_sword.x == dummy.x and slash_sword.y == dummy.y and updatedplayer.slashing == True:
        dummy.health -= 1
        
def draw():
    pyxel.cls(5)
    for wall in walls:
        pyxel.rect(wall.x, wall.y, wall.w, wall.h, wall.color)
    #debug_rect = getDebugRect()
    pyxel.blt(sword.x, sword.y, 0, sword.tile_x, sword.tile_y, TILESIZE, TILESIZE, 14)
    pyxel.blt(bow.x, bow.y, 0, bow.tile_x, bow.tile_y, TILESIZE, TILESIZE, 14)
    pyxel.blt(quiver.x, quiver.y, 0, quiver.tile_x, quiver.tile_y, TILESIZE, TILESIZE, 14)
    pyxel.blt(dummy.x, dummy.y, 0, 16, 16, TILESIZE, TILESIZE, 14)
    if dummy.health <= 0:
       dummy.x = -70
       dummy.y = -70 
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
            
    if updatedplayer.shooting == True:       
        if updatedplayer.direction == 'down':
            pyxel.blt(shoot_bow.x, shoot_bow.y, 0, shoot_bow.tile_x_down, shoot_bow.tile_y_down, TILESIZE, TILESIZE, shoot_bow.alpha)
            pyxel.blt(arrow.x, arrow.y, 0, arrow.tile_x_down, arrow.tile_y_down, TILESIZE, TILESIZE, arrow.alpha)
        elif updatedplayer.direction == 'up':
            pyxel.blt(shoot_bow.x, shoot_bow.y, 0, shoot_bow.tile_x_up, shoot_bow.tile_y_up, TILESIZE, TILESIZE, shoot_bow.alpha)
            pyxel.blt(arrow.x, arrow.y, 0, arrow.tile_x_up, arrow.tile_y_up, TILESIZE, TILESIZE, arrow.alpha)            
        elif updatedplayer.direction == 'right':
            pyxel.blt(shoot_bow.x, shoot_bow.y, 0, shoot_bow.tile_x_right, shoot_bow.tile_y_right, TILESIZE, TILESIZE, shoot_bow.alpha)
            pyxel.blt(arrow.x, arrow.y, 0, arrow.tile_x_right, arrow.tile_y_right, TILESIZE, TILESIZE, arrow.alpha)
        elif updatedplayer.direction == 'left':
            pyxel.blt(shoot_bow.x, shoot_bow.y, 0, shoot_bow.tile_x_left, shoot_bow.tile_y_left, TILESIZE, TILESIZE, shoot_bow.alpha)
            pyxel.blt(arrow.x, arrow.y, 0, arrow.tile_x_left, arrow.tile_y_left, TILESIZE, TILESIZE, arrow.alpha)

    pyxel.rect(secretdoor1.x, secretdoor1.y, secretdoor1.w, secretdoor1.h, WALLCOLOR)
    pyxel.rect(secretdoor2.x, secretdoor2.y, secretdoor2.w, secretdoor2.h, WALLCOLOR)

    #if pyxel.btnp(pyxel.KEY_R):
        #print(absolute_to_tilesize(debug_rect))

pyxel.run(update, draw)