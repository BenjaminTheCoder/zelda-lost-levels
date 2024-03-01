import pyxel
from dataclasses import dataclass

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
TILE_SIZE = 20
GAME_SPEED = 15



    

@dataclass
class Point:
    x: float
    y: float
    
@dataclass
class Line:
    a: Point
    b: Point
    
@dataclass
class Item:
    char: str
    name: str

@dataclass
class Player:
    x: int
    y: int
#     inventory: list[Item]




def update(player):
    if pyxel.btnp(pyxel.KEY_LEFT, repeat=1):
        player.x -= TILE_SIZE
    elif pyxel.btnp(pyxel.KEY_RIGHT, repeat=1):
        player.x += TILE_SIZE
    elif pyxel.btnp(pyxel.KEY_UP, repeat=1):
        player.y -= TILE_SIZE
    elif pyxel.btnp(pyxel.KEY_DOWN, repeat=1):
        player.y += TILE_SIZE
    elif pyxel.btnp(pyxel.KEY_R):
        player.x = SCREEN_WIDTH // 2
        player.y = SCREEN_HEIGHT // 2
        
    # Update everything else, like enemies and stuff.


def draw(player):
    pyxel.cls(13)
    pyxel.rect(player.x, player.y, TILE_SIZE, TILE_SIZE, 0)


def main():
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    
    
    pyxel.init(SCREEN_WIDTH,
               SCREEN_HEIGHT,
               title="GGOAT",
               fps=GAME_SPEED)
    pyxel.run(lambda: update(player),
              lambda: draw(player))
   
   
main()