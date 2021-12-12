import pygame
from config import running, WHITE, \
    BLUE, WINDOW, first, second


class Render:

    def __init__(self):
        self.screen = pygame.display.set_mode(WINDOW)
        self.screen.fill(WHITE)
        self.lines = []
        self.x_y_start = (0, 0)

    def update_start(self, x, y):
        self.x_y_start = x, y

    def render_lines(self):
        for line in self.lines:
            pygame.draw(self.screen, BLUE, (line[0], line[1]), (line[2], line[3]))

    def create_line(self, x, y):
        pygame.draw.line(self.screen, BLUE, self.x_y_start, (x, y))

    def reload_screen(self):
        self.screen.fill(WHITE)


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
                    window.update_start(position[0], position[1])
                elif second is True:
                    first, second = second, first
                    window.reload_screen()
                    window.create_line(position[0], position[1])

            if click[2] is True:
                window.reload_screen()
    if second is True:
        window.reload_screen()
        position = pygame.mouse.get_pos()
        window.create_line(position[0], position[1])
    window.render_lines()
    pygame.display.update()

pygame.quit()
