import pyxel
from dataclasses import dataclass



pyxel.init(160, 120)

@dataclass
class Rect:
    x: int
    y: int
    
rect = Rect(x=0, y=0)
rect2 = Rect(x=160, y=0)
rect3 = Rect(x=160, y=120)
rect4 = Rect(x=0, y=160)


def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    rect.x += 1
    rect.y += 1
    rect2.x -= 1
    rect2.y += 1
    rect3.x -= 1
    rect3.y -= 1
    rect4.x += 1
    rect4.y -= 1

def draw():
    pyxel.cls(0)
    pyxel.rect(rect.x, rect.y, 20, 10, 11)
    pyxel.rect(rect2.x, rect2.y, 20, 10, 2)
    pyxel.rect(rect3.x, rect3.y, 5, 10, 1)
    pyxel.rect(rect4.x, rect4.y, 5, 10, 4)


pyxel.run(update, draw)