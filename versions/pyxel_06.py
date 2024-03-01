import pyxel
from dataclasses import dataclass

TILESIZE = 16
SCREEN_WIDTH = 50*TILESIZE
SCREEN_HEIGHT = 40*TILESIZE
WALLCOLOR = 3

pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, fps=15, display_scale=1)
pyxel.load('test.pyxres')
pyxel.mouse(True)

@dataclass
class Rect:
    x: int
    y: int
    w: int
    h: int
    color: int
    
    
@dataclass
class Player:
    x: int
    y: int

@dataclass
class Item:
    x: int
    y: int
    name: str
    tile_x: int
    tile_y: int

    
updatedplayer = Player(x = SCREEN_WIDTH // 5, y = SCREEN_HEIGHT // 5)
sword = Item(x = 9*TILESIZE, y = 12*TILESIZE, name = 'Sword', tile_x = 16, tile_y = 0)
walls = [
        Rect(x = 0*TILESIZE, y = 0*TILESIZE, w = 2*TILESIZE, h = 60*TILESIZE, color=WALLCOLOR),
        Rect(x = 0*TILESIZE, y = 0*TILESIZE, w = 80*TILESIZE, h = 2*TILESIZE, color=WALLCOLOR),
        Rect(x = 0, y = 38*TILESIZE, w = 80*TILESIZE, h = 2*TILESIZE, color=WALLCOLOR), #bottom
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
        Rect(x = 23*TILESIZE, y = 27*TILESIZE, w = 10*TILESIZE, h = 1*TILESIZE, color=WALLCOLOR),
        Rect(x = 32*TILESIZE, y = 17*TILESIZE, w = 1*TILESIZE, h = 11*TILESIZE, color=WALLCOLOR),
        Rect(x = 33*TILESIZE, y = 16*TILESIZE, w = 15*TILESIZE, h = 1*TILESIZE, color=WALLCOLOR),
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

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    elif pyxel.btnp(pyxel.KEY_LEFT, repeat=1):
        nextX = updatedplayer.x - TILESIZE
        nextY = updatedplayer.y
        canGo = canYouGoThere(nextX, nextY)
        if canGo:
            updatedplayer.x -= TILESIZE
    elif pyxel.btnp(pyxel.KEY_RIGHT, repeat=1):
        nextX = updatedplayer.x + TILESIZE
        nextY = updatedplayer.y
        canGo = canYouGoThere(nextX, nextY)
        if canGo:
            updatedplayer.x += TILESIZE
    elif pyxel.btnp(pyxel.KEY_DOWN, repeat=1):
        nextX = updatedplayer.x
        nextY = updatedplayer.y + TILESIZE
        canGo = canYouGoThere(nextX, nextY)
        if canGo:
            updatedplayer.y += TILESIZE
    elif pyxel.btnp(pyxel.KEY_UP, repeat=1):
        nextX = updatedplayer.x
        nextY = updatedplayer.y - TILESIZE
        canGo = canYouGoThere(nextX, nextY)
        if canGo:
            updatedplayer.y -= TILESIZE



        
def draw():
    pyxel.cls(5)
    for wall in walls:
        pyxel.rect(wall.x, wall.y, wall.w, wall.h, wall.color)
    debug_rect = getDebugRect()
    pyxel.blt(sword.x, sword.y, 0, sword.tile_x, sword.tile_y, TILESIZE, TILESIZE, 14)
    pyxel.rect(debug_rect.x, debug_rect.y, debug_rect.w, debug_rect.h, debug_rect.color)
    pyxel.blt(updatedplayer.x, updatedplayer.y, 0, 0, 0, 16, 16, 7)
#     if pyxel.btnp(pyxel.KEY_R):
#         print(absolute_to_tilesize(debug_rect))

pyxel.run(update, draw)