import random
import pygame

pygame.font.init()


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def random_position():
    return random.randint(0, 399), random.randint(100, 512)


running = True
angle = 0
WINDOW = WIDTH, HEIGHT = 700, 512
FPS = 60
GREY = (220, 220, 220)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 100, 0)
BLUE = (0, 0, 255)
first, second = True, False
default_lines = [[0, 100, WIDTH, 100, BLACK],
                 [WIDTH - 100, 100, WIDTH - 100, 100, BLACK],
                 [WIDTH - 100, 0, WIDTH, 0, BLACK],
                 [WIDTH - 100, 0, WIDTH - 100, 100, BLACK],
                 [WIDTH - 1, 0, WIDTH - 1, 100, BLACK],
                 [400, 100, 400, HEIGHT, BLACK]
                 ]
rects = [[0, 0, 100, 100, RED],
         [100, 0, 100, 100, BLUE],
         [200, 0, 100, 100, GREEN],
         [300, 0, 100, 100, random_color()],
         [400, 0, 100, 100, random_color()],
         [500, 0, 100, 100, random_color()],
         [400, 100, WIDTH - 400, HEIGHT - 100, WHITE],
         [601, 1, 99, 99, GREY]
         ]
delete_button = pygame.image.load('image/delete.png')
add_button = pygame.image.load('image/add.png')
font = pygame.font.Font(None, 24)
