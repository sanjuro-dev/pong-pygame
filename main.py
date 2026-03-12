from os import path
import pygame
from settings import init_fonts, WIDTH, HEIGHT, WHITE, GRAY, BLACK, screen, font
from player import player1, player2
from ball import ball
from sounds import init_sound

pygame.init()
init_sound()

clock = pygame.time.Clock()
running = True

pygame.display.set_icon(pygame.image.load(path.dirname(__file__) + "/assets/bola.png"))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Restart with R key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                player1.score = 0
                player2.score = 0
                ball.xpos = WIDTH/2
                ball.ypos = HEIGHT/2
                ball.xvel = 4
                ball.yvel = 4
    
    screen.fill(WHITE)
    
    # Central line
    for y in range(0, HEIGHT, 30):
        pygame.draw.rect(screen, GRAY, (WIDTH/2 - 5, y, 10, 15))
    

    player1.moving(pygame.key.get_pressed())
    player2.moving(pygame.key.get_pressed())
    player1.drawing(screen)
    player2.drawing(screen)
    

    ball.moving()
    ball.drawing(screen)
    

    score1_text = font.render(str(player1.score), True, BLACK)
    score2_text = font.render(str(player2.score), True, BLACK)
    screen.blit(score1_text, (WIDTH/4, 20))
    screen.blit(score2_text, (WIDTH*3/4, 20))
    
    # Instructions
    instructions = pygame.font.Font(path.dirname(__file__) + "/assets/rainyhearts.ttf", 26).render("Player 1: Arrows | Player 2: W/S | Restart: R", True, GRAY)
    screen.blit(instructions, (WIDTH/2 - instructions.get_width()/2, HEIGHT - 30))
    
    clock.tick(60)
    pygame.display.set_caption(f"Pong - {player1.score} x {player2.score}")
    pygame.display.flip()
    
