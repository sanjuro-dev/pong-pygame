from settings import WIDTH, HEIGHT, BLACK
from os import path
from pygame import image, draw, transform, Surface, SRCALPHA,BLEND_RGBA_MULT
from player import player1, player2
from sounds import play_hit_sound, play_score_sound

class Ball():
    def __init__(self, xpos, ypos, color):
        self.xpos = xpos
        self.ypos = ypos
        self.velocity = 5
        self.color = color
        self.xvel = 4
        self.yvel = 4
        self.radius = 25

    def moving(self):
        self.xpos += self.xvel
        self.ypos += self.yvel

        if self.xpos > WIDTH:
            self.xpos = WIDTH / 2
            self.ypos = HEIGHT / 2
            player2.ypos = HEIGHT / 2
            player1.ypos = HEIGHT / 2

            self.xvel = -4
            self.yvel = 4
            player1.score += 1
            play_score_sound()
            print(f"Player 1: {player1.score}")
            return

        if self.xpos < 0:
            self.xpos = WIDTH / 2
            self.ypos = HEIGHT / 2
            player2.ypos = HEIGHT / 2
            player1.ypos = HEIGHT / 2
            self.xvel = 4
            self.yvel = 4
            player2.score += 1
            play_score_sound()
            print(f"Player 2: {player2.score}")
            return

            # Border colision
        if self.ypos > HEIGHT - self.radius:
            self.yvel = -self.yvel
            self.ypos = HEIGHT - self.radius
            play_hit_sound()
        if self.ypos < self.radius:
            self.yvel = -self.yvel
            self.ypos = self.radius
            play_hit_sound()

            # Player collision

        # Player 1 collision
        if (self.xpos - self.radius <= player1.xpos + player1.size[0] and
                self.xpos + self.radius >= player1.xpos and
                self.ypos + self.radius >= player1.ypos and
                self.ypos - self.radius <= player1.ypos + player1.size[1]):

            # Moving left
            if self.xvel < 0:

                impact = ((self.ypos - (player1.ypos + player1.size[1] / 2)) / (player1.size[1] / 2)) * 2

                # Inverts ball velocity
                self.xvel = abs(self.xvel) + 0.2
                self.yvel = self.yvel + impact

                # Velocity limit
                if self.xvel > 10:
                    self.xvel = 10
                if abs(self.yvel) > 8:
                    self.yvel = 8 * (1 if self.yvel > 0 else -1)

                # Fixing ball pos
                self.xpos = player1.xpos + player1.size[0] + self.radius

                play_hit_sound()

        # Player 2 colision
        if (self.xpos - self.radius <= player2.xpos + player2.size[0] and
                self.xpos + self.radius >= player2.xpos and
                self.ypos + self.radius >= player2.ypos and
                self.ypos - self.radius <= player2.ypos + player2.size[1]):

            # Moving right
            if self.xvel > 0:

                impact = ((self.ypos - (player2.ypos + player2.size[1] / 2)) / (player2.size[1] / 2)) * 2

                # Inverts ball velocity
                self.xvel = -abs(self.xvel) - 0.2
                self.yvel = self.yvel + impact

                # Velocity limit
                if abs(self.xvel) > 10:
                    self.xvel = -10
                if abs(self.yvel) > 8:
                    self.yvel = 8 * (1 if self.yvel > 0 else -1)

                # Fixing ball pos
                self.xpos = player2.xpos - self.radius

                play_hit_sound()

    def drawing(self, tela):

        textura = image.load(path.dirname(__file__) + "/assets/bola.png")
        textura = transform.scale(textura, (self.radius * 2, self.radius * 2))

        circulo = Surface((self.radius * 2, self.radius * 2), SRCALPHA)
        draw.circle(circulo, (255, 255, 255), (self.radius, self.radius), self.radius)

        circulo.blit(textura, (0, 0), special_flags=BLEND_RGBA_MULT)
        tela.blit(circulo, (self.xpos - self.radius, self.ypos - self.radius))

ball = Ball(WIDTH/2, HEIGHT/2, BLACK)