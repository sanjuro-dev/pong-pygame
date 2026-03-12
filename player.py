from settings import HEIGHT, WIDTH, BLUE, RED
from pygame import K_w, K_s, K_UP, K_DOWN, draw

class Player():
    def __init__(self, xpos, ypos, color, WASD=False):

        self.xpos = xpos
        self.ypos = ypos
        self.velocity = 5
        self.color = color
        self.size = (25, 100)
        self.score = 0
        self.WASD = WASD

    def moving(self, teclas):
        if self.WASD:
            if teclas[K_w] and self.ypos > 0:
                self.ypos -= self.velocity
            if teclas[K_s] and self.ypos < HEIGHT - self.size[1]:
                self.ypos += self.velocity
        else:
            if teclas[K_UP] and self.ypos > 0:
                self.ypos -= self.velocity
            if teclas[K_DOWN] and self.ypos < HEIGHT - self.size[1]:
                self.ypos += self.velocity

    def drawing(self, tela):
        draw.rect(tela, self.color, (self.xpos, self.ypos, self.size[0], self.size[1]))

player1 = Player(100, HEIGHT/2 - 50, BLUE, False)
player2 = Player(WIDTH - 125, HEIGHT/2 - 50, RED, True)