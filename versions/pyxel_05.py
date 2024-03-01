import pyxel
from dataclasses import dataclass

TILESIZE = 16
SCREEN_WIDTH = 50*TILESIZE
SCREEN_HEIGHT = 40*TILESIZE
WALLCOLOR = 3

pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, fps=15, display_scale=1)
pyxel.load('test.pyxres')

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

updatedplayer = Player(x = SCREEN_WIDTH // 5, y = SCREEN_HEIGHT // 5)

walls = [
        Rect(x = 0*TILESIZE, y = 0*TILESIZE, w = 2*TILESIZE, h = 60*TILESIZE, color=WALLCOLOR),
        Rect(x = 0*TILESIZE, y = 0*TILESIZE, w = 80*TILESIZE, h = 2*TILESIZE, color=WALLCOLOR),
        Rect(x = 0, y = 38*TILESIZE, w = 80*TILESIZE, h = 2*TILESIZE, color=WALLCOLOR), #bottom
        Rect(x = 48*TILESIZE, y = 0*TILESIZE, w = 2*TILESIZE, h = 60*TILESIZE, color=WALLCOLOR), # right
        Rect(x = 16*TILESIZE, y = 0*TILESIZE, w = TILESIZE, h = 7*TILESIZE, color=WALLCOLOR), # done
        Rect(x = 0, y = 16*TILESIZE, w = 8*TILESIZE, h = TILESIZE, color=WALLCOLOR),
        Rect(x = 10*TILESIZE, y = 16*TILESIZE, w = 6*TILESIZE, h = TILESIZE, color=WALLCOLOR),

    ]

def canYouGoThere(nextX, nextY):
    canGo = True
    for wall in walls:
        if nextX >= wall.x and nextX < wall.x + wall.w and nextY >= wall.y and nextY < wall.h + wall.y:
            canGo = False
    return canGo

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
        print(nextX, nextY, canGo)
        if canGo:
            updatedplayer.y += TILESIZE
    elif pyxel.btnp(pyxel.KEY_UP, repeat=1):
        nextX = updatedplayer.x
        nextY = updatedplayer.y - TILESIZE
        canGo = canYouGoThere(nextX, nextY)
        print(nextX, nextY, canGo)
        if canGo:
            updatedplayer.y -= TILESIZE
    
        
def draw():
    pyxel.cls(5)
    for wall in walls:
        pyxel.rect(wall.x, wall.y, wall.w, wall.h, wall.color)
    pyxel.blt(updatedplayer.x, updatedplayer.y, 0, 0, 0, 16, 16, 7)
    
pyxel.run(update, draw)