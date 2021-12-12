import pygame
from func import reload
from config import *


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)
pygame.display.set_caption('Типа игра')
clock = pygame.time.Clock()


while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = pygame.mouse.get_pressed()
            if click[0] is True:
                if first is True:
                    x_start, y_start = pygame.mouse.get_pos()
                    first, second = second, first
                elif second is True:
                    x_end, y_end = pygame.mouse.get_pos()
                    reload(screen)
                    pygame.draw.line(screen, BLUE, (x_start, y_start), (x_end, y_end))
                    lines.append([x_start, y_start, x_end, y_end])
                    first, second = second, first
            if click[2] is True:
                lines = []
                reload(screen)
    if second is True:
        reload(screen)
        pygame.draw.line(screen, BLUE, (x_start, y_start), pygame.mouse.get_pos())
    for line in lines:
        pygame.draw.line(screen, BLUE, (line[0], line[1]), (line[2], line[3]))
    pygame.display.update()

pygame.quit()
