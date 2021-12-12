import pygame
from config import WHITE, BLUE, WINDOW


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
