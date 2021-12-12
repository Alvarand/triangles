import pygame
from config import running, first, second
from render import Render

window = Render()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = pygame.mouse.get_pressed()
            position = pygame.mouse.get_pos()
            if click[0] is True:
                if first is True:
                    first, second = second, first
                    window.update_start(position)
                elif second is True:
                    first, second = second, first
                    window.reload_screen()
                    window.append_lines(position)
            if click[2] is True:
                window.lines = []
                window.reload_screen()
    if second is True:
        window.reload_screen()
        window.create_line(pygame.mouse.get_pos())
    window.render_lines()
    pygame.display.update()

pygame.quit()
