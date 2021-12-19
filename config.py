import random
import pygame

pygame.font.init()


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def random_position():
    return random.randint(0, 399), random.randint(100, 512)


def get_circle_range(x, y):
    x_range = range(x - radius, x + radius)
    y_range = range(y - radius, y + radius)
    return x_range, y_range


def get_cos(cos_angle):
    return min(1, max(cos_angle, -1))


running = True
draw = True
radius = 15
WINDOW = WIDTH, HEIGHT = 700, 512
GREY = (220, 220, 220)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 100, 0)
BLUE = (0, 0, 255)

default_lines = [
    [0, 100, WIDTH, 100, BLACK],
    [WIDTH - 100, 100, WIDTH - 100, 100, BLACK],
    [WIDTH - 100, 0, WIDTH, 0, BLACK],
    [WIDTH - 100, 0, WIDTH - 100, 100, BLACK],
    [WIDTH - 1, 0, WIDTH - 1, 100, BLACK],
    [400, 170, WIDTH, 170, BLACK],
    [400, 100, 400, HEIGHT, BLACK],
]

rects = [
    [0, 0, 100, 100, RED],
    [100, 0, 100, 100, BLUE],
    [200, 0, 100, 100, GREEN],
    [300, 0, 100, 100, random_color()],
    [400, 0, 100, 100, random_color()],
    [500, 0, 100, 100, random_color()],
    [400, 100, WIDTH - 400, HEIGHT - 100, WHITE],
    [601, 1, 99, 99, GREY],
]

delete_button = pygame.image.load('image/delete.png')
add_button = pygame.image.load('image/add.png')
switch_button = pygame.image.load('image/switch.png')

font = pygame.font.Font(None, 24)
texts = [
    [font.render('clear', True, (180, 0, 0)), (422, 145)],
    [font.render('add', True, (180, 0, 0)), (500, 137)],
    [font.render('triangle', True, (180, 0, 0)), (485, 152)],
    [font.render('add', True, (180, 0, 0)), (575, 137)],
    [font.render('line', True, (180, 0, 0)), (577, 152)],
    [font.render('switch', True, (180, 0, 0)), (638, 145)],
]
