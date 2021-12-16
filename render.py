import pygame
from config import GREY, BLUE, WINDOW, rects, FPS, default_lines
import copy


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

    def add_line(self, pos):
        self.lines.append(Line(pos[0], pos[1]))
        if len(self.lines) != 1:
            self.lines[len(self.lines) - 2].end_pos.x = pos[0]
            self.lines[len(self.lines) - 2].end_pos.y = pos[1]
        if len(self.lines) == 3:
            self.lines[-1].end_pos.x = self.lines[0].start_pos.x
            self.lines[-1].end_pos.y = self.lines[0].start_pos.y


class NewRender:

    def __init__(self):
        self.triangles = []
        self.current_triangle = Triangle()
        self.screen = pygame.display.set_mode(WINDOW)
        self.clock = pygame.time.Clock()
        self.screen.fill(GREY)
        self.FPS = FPS
        self.bg_color = GREY
        self.rects = rects
        self.line_color = [610, 10, 690, 90, self.current_triangle.color]
        self.default_lines = [self.line_color] + default_lines

    def render_triangles(self):
        if len(self.current_triangle.lines) == 3:
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
            pygame.draw.line(self.screen, self.current_triangle.color,
                             (self.current_triangle.lines[-1].start_pos.x,
                              self.current_triangle.lines[-1].start_pos.y),
                             (pos[0], pos[1]))

    def clear_triangles(self):
        self.triangles = []

    def reload_screen(self):
        self.screen.fill(self.bg_color)

    def get_color(self, pos):
        self.current_triangle.color = self.screen.get_at(pos)
        self.line_color[-1] = self.current_triangle.color

    def render_rects(self):
        for rect in self.rects:
            pygame.draw.rect(self.screen, rect[-1], (rect[0], rect[1], rect[2], rect[3]))

    def render_default_lines(self):
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
            self.clear_triangles()
            self.reload_screen()

    def update(self):
        self.reload_screen()
        self.render_triangles()
        self.render_current_triangle(pygame.mouse.get_pos())
        self.render_rects()
        self.render_default_lines()
        self.clock.tick(self.FPS)
        pygame.display.update()


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
