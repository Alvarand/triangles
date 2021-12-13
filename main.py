import pygame
from config import running, angle, FPS
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
                    if angle == 0:
                        angle += 1
                        window.update_first_angle(position)
                    elif angle == 1:
                        angle += 1
                        window.reload_screen()
                        window.append_lines(position)
                        window.update_start(position)
                    elif angle == 2:
                        angle = 0
                        window.reload_screen()
                        window.create_triangle(position)
            else:
                window.get_color(position)
            if click[2] is True:
                window.update_lines()
                window.reload_screen()
    if angle != 0:
        window.reload_screen()
        window.create_line(pygame.mouse.get_pos())
    window.render_lines()
    window.clock.tick(FPS)
    window.draw_rects()
    pygame.display.update()

pygame.quit()
