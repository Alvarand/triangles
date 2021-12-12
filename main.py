import pygame
from config import running, first, second, FPS
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
            if position[1] >= 100:
                if click[0] is True:
                    if first is True:
                        first, second = second, first
                        window.update_start(position)
                    elif second is True:
                        first, second = second, first
                        window.reload_screen()
                        window.append_lines(position)
            else:
                window.get_color(position)
            if click[2] is True:
                window.update_lines()
                window.reload_screen()
    if second is True:
        window.reload_screen()
        window.create_line(pygame.mouse.get_pos())
    window.render_lines()
    window.clock.tick(FPS)
    window.draw_rects()
    pygame.display.update()

pygame.quit()
