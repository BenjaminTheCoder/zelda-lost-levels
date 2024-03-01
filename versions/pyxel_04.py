import pyxel
from dataclasses import dataclass

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TILESIZE = 20
pyxel.init(SCREEN_WIDTH, SCREEN_HEIGHT, fps=15)

@dataclass
class Rect:
    x: int
    y: int
    w: int
    h: int
    
@dataclass
class Player:
    x: int
    y: int

updatedplayer = Player(x = SCREEN_WIDTH // 5, y = SCREEN_HEIGHT // 5)

walls = [
        Rect(x = 0*TILESIZE, y = 0*TILESIZE, w = 2*TILESIZE, h = 60*TILESIZE),
        Rect(x = 0*TILESIZE, y = 0*TILESIZE, w = 80*TILESIZE, h = 2*TILESIZE),
        Rect(x = 0, y = 560, w = 80*TILESIZE, h = 2*TILESIZE),
        Rect(x = 760, y = 0*TILESIZE, w = 2*TILESIZE, h = 60*TILESIZE),
        Rect(x = 260, y = 0*TILESIZE, w = 20, h = 140),
        Rect(x = 0, y = 260, w = 120, h = 20),
        Rect(x = 160, y = 260, w = 120, h = 20),

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
    pyxel.cls(7)
    for wall in walls:
        pyxel.rect(wall.x, wall.y, wall.w, wall.h, 3)
    pyxel.rect(updatedplayer.x, updatedplayer.y, TILESIZE, TILESIZE, 5)
pyxel.run(update, draw)