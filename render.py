import pygame
from config import running, WHITE, \
    BLUE, WINDOW, first, second


class Render:

    def __init__(self):
        self.screen = pygame.display.set_mode(WINDOW)
        self.screen.fill(WHITE)
        self.lines = []
        self.start_pos = (0, 0)

    def update_start(self, pos):
        self.start_pos = pos

    def render_lines(self):
        for line in self.lines:
            pygame.draw.line(self.screen, BLUE, (line[0], line[1]), (line[2], line[3]))

    def create_line(self, end_pos):
        pygame.draw.line(self.screen, BLUE, self.start_pos, end_pos)

    def reload_screen(self):
        self.screen.fill(WHITE)

    def append_lines(self, end_pos):
        self.lines.append([self.start_pos[0], self.start_pos[1], end_pos[0], end_pos[1]])


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
