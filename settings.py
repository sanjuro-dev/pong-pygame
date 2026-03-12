from pygame import font, display
from os import path

# Screen settings
HEIGHT = 600
WIDTH = 800

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GRAY = (200, 200, 200)

# Fonts
def init_fonts():
    font.init()

init_fonts()
font = font.Font(path.dirname(__file__) + "/assets/rainyhearts.ttf", 50)



screen = display.set_mode((WIDTH, HEIGHT))

