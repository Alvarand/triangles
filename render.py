import pygame
from config import GREY, BLUE, WINDOW, RED, rects
import copy


class Render:

    def __init__(self):
        self.screen = pygame.display.set_mode(WINDOW)
        self.clock = pygame.time.Clock()
        self.screen.fill(GREY)
        self.default_lines = []
        self.lines = copy.deepcopy(self.default_lines)
        self.start_pos = (0, 0)
        self.rects = rects
        self.bg_color = GREY
        self.color = BLUE

    def update_start(self, pos):
        self.start_pos = pos

    def render_lines(self):
        for line in self.lines:
            pygame.draw.line(self.screen, line[-1], (line[0], line[1]), (line[2], line[3]))

    def create_line(self, end_pos):
        pygame.draw.line(self.screen, self.color, self.start_pos, end_pos)

    def reload_screen(self):
        self.screen.fill(self.bg_color)

    def append_lines(self, end_pos):
        self.lines.append([self.start_pos[0], self.start_pos[1], end_pos[0], end_pos[1], self.color])

    def update_lines(self):
        self.lines = copy.deepcopy(self.default_lines)

    def draw_rects(self):
        for rect in self.rects:
            pygame.draw.rect(self.screen, rect[-1], (rect[0], rect[1], rect[2], rect[3]))

    def get_color(self, pos):
        self.color = self.screen.get_at(pos)
