import pyxel
from dataclasses import dataclass

SCREEN_WIDTH = 160
SCREEN_HEIGHT = 120
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

updatedplayer = Player(x = SCREEN_WIDTH // 2, y = SCREEN_HEIGHT // 2)
wall = Rect(x = 10, y = 20, w = 30, h = 40)

def canYouGoThere(nextX, nextY, wallX, wallY, wallW, wallH):
    if nextX > wallX and nextX < wallX + wallW and nextY > wallY and nextY < wallH + wallY:
        return False
    else:
        return True

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    elif pyxel.btnp(pyxel.KEY_LEFT, repeat=1):
        nextX = updatedplayer.x - 10
        nextY = updatedplayer.y
        canGo = canYouGoThere(nextX, nextY, wall.x, wall.y, wall.w, wall.h)
        if canGo:
            updatedplayer.x -= 10
    elif pyxel.btnp(pyxel.KEY_RIGHT, repeat=1):
        nextX = updatedplayer.x + 10
        nextY = updatedplayer.y
        canGo = canYouGoThere(nextX, nextY, wall.x, wall.y, wall.w, wall.h)
        if canGo:
            updatedplayer.x += 10
    elif pyxel.btnp(pyxel.KEY_DOWN, repeat=1):
        nextX = updatedplayer.x
        nextY = updatedplayer.y + 10
        canGo = canYouGoThere(nextX, nextY, wall.x, wall.y, wall.w, wall.h)
        print(nextX, nextY, canGo)
        if canGo:
            updatedplayer.y += 10
    elif pyxel.btnp(pyxel.KEY_UP, repeat=1):
        nextX = updatedplayer.x
        nextY = updatedplayer.y - 10
        canGo = canYouGoThere(nextX, nextY, wall.x, wall.y, wall.w, wall.h)
        print(nextX, nextY, canGo)
        if canGo:
            updatedplayer.y -= 10
    
        
def draw():
    pyxel.cls(0)    
    pyxel.rect(wall.x, wall.y, wall.w, wall.h, 13)
    pyxel.rect(updatedplayer.x, updatedplayer.y, 1, 1, 11)
pyxel.run(update, draw)