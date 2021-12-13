import pygame
from config import GREY, BLUE, WINDOW, rects, FPS, default_lines
import copy


class Render:

    def __init__(self):
        self.screen = pygame.display.set_mode(WINDOW)
        self.clock = pygame.time.Clock()
        self.screen.fill(GREY)
        self.first_angle_pos = (0, 0)
        self.start_pos = (0, 0)
        self.rects = rects
        self.bg_color = GREY
        self.color = BLUE
        self.FPS = FPS
        self.angle = 0
        self.line_color = [610, 10, 690, 90, self.color]
        self.default_lines = [self.line_color] + default_lines
        self.lines = copy.deepcopy(self.default_lines)

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
        self.line_color[-1] = self.color
        self.lines[0][-1] = self.color

    def update_first_angle(self, pos):
        self.first_angle_pos = pos
        self.start_pos = pos

    def create_triangle(self, end_pos):
        self.lines.append([self.start_pos[0], self.start_pos[1], end_pos[0], end_pos[1], self.color])
        self.lines.append([self.first_angle_pos[0], self.first_angle_pos[1], end_pos[0], end_pos[1], self.color])

    def update(self):
        self.draw_rects()
        self.render_lines()
        self.clock.tick(self.FPS)
        pygame.display.update()

    def click(self):
        mouse_click = pygame.mouse.get_pressed()
        position = pygame.mouse.get_pos()
        if position[1] > 100 and position[0] < 400:
            if mouse_click[0] is True:
                if self.angle == 0:
                    self.angle += 1
                    self.update_first_angle(position)
                elif self.angle == 1:
                    self.angle += 1
                    self.reload_screen()
                    self.append_lines(position)
                    self.update_start(position)
                elif self.angle == 2:
                    self.angle = 0
                    self.reload_screen()
                    self.create_triangle(position)
        elif position[1] < 100 and position[0] < 600:
            self.get_color(position)
        if mouse_click[2] is True and self.angle == 0:
            self.update_lines()
            self.reload_screen()
