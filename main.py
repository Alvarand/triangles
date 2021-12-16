import pygame
from config import running
from render import NewRender

window = NewRender()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            window.click()
    window.update()

pygame.quit()
