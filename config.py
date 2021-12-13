import random


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


running = True
angle = 0
WINDOW = WIDTH, HEIGHT = 600, 512
FPS = 60
GREY = (220, 220, 220)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
first, second = True, False
lines = []
rects = [[0, 0, 100, 100, RED],
         [100, 0, 100, 100, BLUE],
         [200, 0, 100, 100, GREEN],
         [300, 0, 100, 100, random_color()],
         [400, 0, 100, 100, random_color()],
         [500, 0, 100, 100, random_color()],
         ]
