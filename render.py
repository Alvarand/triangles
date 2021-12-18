import pygame
from math import sqrt, acos, degrees
from config import BLUE, WINDOW, rects, FPS, default_lines


class Coordinates:

    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y


class Line:

    def __init__(self, x=None, y=None):
        self.start_pos = Coordinates(x, y)
        self.end_pos = Coordinates()


class Triangle:

    def __init__(self):
        self.lines = []
        self.color = BLUE
        self.sides_length = []
        self.angles = []

    def add_line(self, pos):
        self.lines.append(Line(pos[0], pos[1]))
        if len(self.lines) != 1:
            self.lines[len(self.lines) - 2].end_pos.x = pos[0]
            self.lines[len(self.lines) - 2].end_pos.y = pos[1]
        if len(self.lines) == 3:
            self.lines[-1].end_pos.x = self.lines[0].start_pos.x
            self.lines[-1].end_pos.y = self.lines[0].start_pos.y

    def calculate_distance(self):
        line1, line2, line3 = [line.start_pos for line in self.lines]
        for a, b in ([line1, line2], [line2, line3], [line1, line3]):
            x = abs(a.x - b.x)
            y = abs(a.y - b.y)
            length = sqrt(x * x + y * y) * 2.5 / 96
            self.sides_length.append(length)
        self.calculate_angle()

    def calculate_angle(self):
        len1, len2, len3 = self.sides_length
        for a, b, c in ([len1, len3, len2], [len2, len1, len3], [len3, len2, len1]):
            try:
                angle = degrees(acos((a * a + b * b - c * c) / (2 * a * b)))
                self.angles.append(angle)
            except ZeroDivisionError:
                self.angles.append(0.0)


class NewRender:

    def __init__(self):
        self.triangles = []
        self.current_triangle = Triangle()
        self.screen = pygame.display.set_mode(WINDOW)
        self.clock = pygame.time.Clock()
        self.FPS = FPS
        self.bg_color = (202, 228, 241)  # GREY
        self.rects = rects
        self.line_color = [610, 10, 690, 90, self.current_triangle.color]
        self.default_lines = [self.line_color] + default_lines
        self.last_pos = (0, 0)

    def render_triangle(self):
        if len(self.current_triangle.lines) == 3:
            self.current_triangle.calculate_distance()
            self.triangles.append(self.current_triangle)
            self.current_triangle = Triangle()
            self.current_triangle.color = self.line_color[-1]

        for triangle in self.triangles:
            for line in triangle.lines:
                pygame.draw.line(self.screen, triangle.color, (line.start_pos.x, line.start_pos.y),
                                 (line.end_pos.x, line.end_pos.y))

    def render_current_triangle(self, pos):
        if len(self.current_triangle.lines) > 0:
            for line in self.current_triangle.lines[:-1]:
                pygame.draw.line(self.screen, self.current_triangle.color, (line.start_pos.x, line.start_pos.y),
                                 (line.end_pos.x, line.end_pos.y))
            if pos[1] > 100 and pos[0] < 400:
                self.last_pos = pos
                pygame.draw.line(self.screen, self.current_triangle.color,
                                 (self.current_triangle.lines[-1].start_pos.x,
                                  self.current_triangle.lines[-1].start_pos.y),
                                 (pos[0], pos[1]))
            else:
                pygame.draw.line(self.screen, self.current_triangle.color,
                                 (self.current_triangle.lines[-1].start_pos.x,
                                  self.current_triangle.lines[-1].start_pos.y),
                                 (self.last_pos[0], self.last_pos[1]))

    def clear_triangle(self):
        self.triangles = []

    def reload_screen(self):
        self.screen.fill(self.bg_color)

    def get_color(self, pos):
        self.current_triangle.color = self.screen.get_at(pos)
        self.line_color[-1] = self.current_triangle.color

    def render_rect(self):
        for rect in self.rects:
            pygame.draw.rect(self.screen, rect[-1], (rect[0], rect[1], rect[2], rect[3]))

    def render_default_line(self):
        for line in self.default_lines:
            pygame.draw.line(self.screen, line[-1], (line[0], line[1]), (line[2], line[3]))

    def click(self):
        mouse_click = pygame.mouse.get_pressed()
        position = pygame.mouse.get_pos()
        if position[1] > 100 and position[0] < 400:
            if mouse_click[0] is True:
                self.current_triangle.add_line(position)
        elif position[1] < 100 and position[0] < 600:
            self.get_color(position)
        if mouse_click[2] is True and len(self.current_triangle.lines) == 0:
            self.clear_triangle()
            self.reload_screen()

    def update(self):
        self.reload_screen()
        self.render_triangle()
        self.render_current_triangle(pygame.mouse.get_pos())
        self.render_rect()
        self.render_default_line()
        self.clock.tick(self.FPS)
        pygame.display.update()
