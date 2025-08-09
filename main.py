import pygame
from random import randint
import os

class Player():
    def __init__(self, xpos, ypos, color, WASD=False):

        self.xpos = xpos
        self.ypos = ypos
        self.velocity = 5
        self.color = color
        self.size = (25, 100)
        self.score = 0
        self.WASD = WASD


    def mover(self, teclas):
        if self.WASD:
            if teclas[pygame.K_w] and self.ypos > 0:
                self.ypos -= self.velocity
            if teclas[pygame.K_s] and self.ypos < HEIGHT - self.size[1]:
                self.ypos += self.velocity
        else:
            if teclas[pygame.K_UP] and self.ypos > 0:
                self.ypos -= self.velocity
            if teclas[pygame.K_DOWN] and self.ypos < HEIGHT - self.size[1]:
                self.ypos += self.velocity


        
    def desenhar(self, tela):
        pygame.draw.rect(tela, self.color, (self.xpos, self.ypos, self.size[0],self.size[1]))

    

class Ball():
    def __init__(self, xpos, ypos, color):
        self.xpos = xpos
        self.ypos = ypos
        self.velocity = 5
        self.color = color
        self.xvel = 4
        self.yvel = 4
        self.radius = 25

    def mover(self):
        self.xpos += self.xvel
        self.ypos += self.yvel

        if self.xpos > WIDTH:
            self.xpos = WIDTH/2
            self.ypos = HEIGHT/2
            player2.ypos = HEIGHT/2
            player1.ypos = HEIGHT/2


            self.xvel = -4  
            self.yvel = 4
            player1.score += 1
            play_score_sound()  # Toca som de pontuação
            print(f"Player 1: {player1.score}")
            return  # Evita verificações adicionais após reiniciar a bola

        if self.xpos < 0:
            self.xpos = WIDTH/2
            self.ypos = HEIGHT/2
            player2.ypos = HEIGHT/2
            player1.ypos = HEIGHT/2
            self.xvel = 4  # Direção oposta ao último jogador que pontuou
            self.yvel = 4
            player2.score += 1
            play_score_sound()  # Toca som de pontuação
            print(f"Player 2: {player2.score}")
            return  # Evita verificações adicionais após reiniciar a bola

        # Colisão com as bordas superior e inferior
        if self.ypos > HEIGHT - self.radius:
            self.yvel = -self.yvel
            self.ypos = HEIGHT - self.radius  # Corrige a posição para evitar que a bola saia da tela
            play_hit_sound()  # Som de colisão com a borda
        if self.ypos < self.radius:
            self.yvel = -self.yvel
            self.ypos = self.radius  # Corrige a posição para evitar que a bola saia da tela
            play_hit_sound()  # Som de colisão com a borda
        


        # Colisão com os jogadores - melhorada para considerar a posição da bola e o raio
        # Colisão com o jogador 1 (esquerda)
        if (self.xpos - self.radius <= player1.xpos + player1.size[0] and 
            self.xpos + self.radius >= player1.xpos and 
            self.ypos + self.radius >= player1.ypos and 
            self.ypos - self.radius <= player1.ypos + player1.size[1]):
            
            # Se a bola está se movendo para a esquerda
            if self.xvel < 0:
                # Calcula o impacto baseado na posição relativa da bola na raquete
                impacto = ((self.ypos - (player1.ypos + player1.size[1]/2)) / (player1.size[1]/2)) * 2
                
                # Inverte a direção horizontal e adiciona variação baseada na posição de impacto
                self.xvel = abs(self.xvel) + 0.2  # Aumenta levemente a velocidade a cada rebatida
                self.yvel = self.yvel + impacto  # Ajusta a direção vertical baseado no ponto de impacto
                
                # Limita a velocidade máxima
                if self.xvel > 10:
                    self.xvel = 10
                if abs(self.yvel) > 8:
                    self.yvel = 8 * (1 if self.yvel > 0 else -1)
                    
                # Garante que a bola não fique presa na raquete
                self.xpos = player1.xpos + player1.size[0] + self.radius
                
                # Toca som de colisão
                play_hit_sound()

        # Colisão com o jogador 2 (direita)
        if (self.xpos - self.radius <= player2.xpos + player2.size[0] and 
            self.xpos + self.radius >= player2.xpos and 
            self.ypos + self.radius >= player2.ypos and 
            self.ypos - self.radius <= player2.ypos + player2.size[1]):
            
            # Se a bola está se movendo para a direita
            if self.xvel > 0:
                # Calcula o impacto baseado na posição relativa da bola na raquete
                impacto = ((self.ypos - (player2.ypos + player2.size[1]/2)) / (player2.size[1]/2)) * 2
                
                # Inverte a direção horizontal e adiciona variação baseada na posição de impacto
                self.xvel = -abs(self.xvel) - 0.2  # Aumenta levemente a velocidade a cada rebatida
                self.yvel = self.yvel + impacto  # Ajusta a direção vertical baseado no ponto de impacto
                
                # Limita a velocidade máxima
                if abs(self.xvel) > 10:
                    self.xvel = -10
                if abs(self.yvel) > 8:
                    self.yvel = 8 * (1 if self.yvel > 0 else -1)
                    
                # Garante que a bola não fique presa na raquete
                self.xpos = player2.xpos - self.radius
                
                # Toca som de colisão
                play_hit_sound()
    def desenhar(self, tela):

        textura = pygame.image.load(os.path.dirname(__file__) + "/bola.png")
        textura = pygame.transform.scale(textura, (self.radius*2, self.radius*2))


        circulo = pygame.Surface((self.radius*2, self.radius*2), pygame.SRCALPHA)
        pygame.draw.circle(circulo, (255, 255, 255), (self.radius, self.radius), self.radius)

        circulo.blit(textura, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        tela.blit(circulo, (self.xpos - self.radius, self.ypos - self.radius))


    





    




    

pygame.init()

HEIGHT = 600
WIDTH = 800

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

GRAY = (200, 200, 200)

# Inicialização da fonte para o placar
pygame.font.init()
font = pygame.font.Font(os.path.dirname(__file__) + "/rainyhearts.ttf", 50)



# Inicialização de sons
pygame.mixer.init()

# Criação de sons simples
def play_hit_sound():
    hit = pygame.mixer.Sound(os.path.dirname(__file__) + "/hit.wav")
    hit.play()

def play_score_sound():
    score = pygame.mixer.Sound(os.path.dirname(__file__) + "/score.wav")
    score.play()

player1 = Player(100, HEIGHT/2 - 50, BLUE, False)
player2 = Player(WIDTH - 125, HEIGHT/2 - 50, RED, True)
ball = Ball(WIDTH/2, HEIGHT/2, BLACK)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

pygame.display.set_icon(pygame.image.load(os.path.dirname(__file__) + "/bola.png"))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Adiciona opção de reiniciar o jogo com a tecla R
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                player1.score = 0
                player2.score = 0
                ball.xpos = WIDTH/2
                ball.ypos = HEIGHT/2
                ball.xvel = 4
                ball.yvel = 4
    
    screen.fill(WHITE)
    
    # Desenha a linha central
    for y in range(0, HEIGHT, 30):
        pygame.draw.rect(screen, GRAY, (WIDTH/2 - 5, y, 10, 15))
    
    # Atualiza e desenha os jogadores
    player1.mover(pygame.key.get_pressed())
    player2.mover(pygame.key.get_pressed())
    player1.desenhar(screen)
    player2.desenhar(screen)
    
    # Atualiza e desenha a bola
    ball.mover()
    ball.desenhar(screen)
    
    # Desenha o placar
    score1_text = font.render(str(player1.score), True, BLACK)
    score2_text = font.render(str(player2.score), True, BLACK)
    screen.blit(score1_text, (WIDTH/4, 20))
    screen.blit(score2_text, (WIDTH*3/4, 20))
    
    # Instruções
    instructions = pygame.font.Font(os.path.dirname(__file__) + "/rainyhearts.ttf", 26).render("Player 1: Setas | Player 2: W/S | Reiniciar: R", True, GRAY)
    screen.blit(instructions, (WIDTH/2 - instructions.get_width()/2, HEIGHT - 30))
    
    clock.tick(60)
    pygame.display.set_caption(f"Pong - {player1.score} x {player2.score}")
    pygame.display.flip()
    
