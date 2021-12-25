import pygame
from math import sqrt, acos, degrees
from config import (BLUE, WINDOW, rects, default_lines,
                    delete_button, add_button, switch_button,
                    texts, random_position, draw,
                    get_circle_range, get_cos, radius,
                    font, texts_for_polygon)


class Coordinates:

    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y


class Line:

    def __init__(self, x=None, y=None):
        self.start_pos = Coordinates(x, y)
        self.end_pos = Coordinates()


class Polygon:

    def __init__(self, n=6):
        self.count_angles = n
        self.lines = []
        self.color = BLUE
        self.sides_length = []
        self.angles = []
        self.corner_name = dict()
        for i in range(self.count_angles):
            if i == self.count_angles - 1:
                self.corner_name[i] = [
                    f'{chr(65 + i)}',
                    (422, 200 + i * 20),
                    (422, 300 + i * 20),
                    [f'A{chr(65 + i)}', (422, 400 + i * 20)]
                ]
            else:
                self.corner_name[i] = [
                    f'{chr(65 + i)}',
                    (422, 200 + i * 20),
                    (422, 300 + i * 20),
                    [f'{chr(65 + i)}{chr(65 + i + 1)}', (422, 400 + i * 20)]
                ]

    def add_line(self, pos):
        self.lines.append(Line(pos[0], pos[1]))

        if len(self.lines) != 1:
            self.lines[len(self.lines) - 2].end_pos.x = pos[0]
            self.lines[len(self.lines) - 2].end_pos.y = pos[1]
        if len(self.lines) == self.count_angles:
            self.lines[-1].end_pos.x = self.lines[0].start_pos.x
            self.lines[-1].end_pos.y = self.lines[0].start_pos.y

    def calculate_distance(self):
        lines = [line.start_pos for line in self.lines]
        self.sides_length = []
        for current_angle in range(self.count_angles):
            x = abs(lines[current_angle].x - lines[(current_angle + 1) % self.count_angles].x)
            y = abs(lines[current_angle].y - lines[(current_angle + 1) % self.count_angles].y)
            length = sqrt(x * x + y * y) * 2.5 / 96
            self.sides_length.append(length)
        self.calculate_angle()

    def calculate_angle(self):
        self.angles = []
        for current_angle in range(self.count_angles):
            try:
                a = self.sides_length[current_angle]
                b = self.sides_length[(current_angle - 1 + self.count_angles) % self.count_angles]
                x = abs(
                    self.lines[(current_angle - 1 + self.count_angles) % self.count_angles].start_pos.x - self.lines[
                        (current_angle + 1) % self.count_angles].start_pos.x)
                y = abs(
                    self.lines[(current_angle - 1 + self.count_angles) % self.count_angles].start_pos.y - self.lines[
                        (current_angle + 1) % self.count_angles].start_pos.y)
                c = sqrt(x * x + y * y) * 2.5 / 96
                a_cos = get_cos((a * a + b * b - c * c) / (2 * a * b))
                angle = degrees(acos(a_cos))
                self.angles.append(angle)
            except ZeroDivisionError:
                self.angles.append(0.0)


class Button:
    def __init__(self, x, y, image, func):
        self.width = image.get_width()
        self.height = image.get_height()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.func = func

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def do_it(self):
        self.func()


class NewRender:

    def __init__(self):
        self.polygons = []
        self.current_polygon = Polygon()
        self.screen = pygame.display.set_mode(WINDOW)
        pygame.display.set_caption('Polygons')
        self.clock = pygame.time.Clock()
        self.draw = draw
        self.bg_color = (202, 228, 241)  # GREY
        self.rects = rects
        self.line_color = [610, 10, 690, 90, self.current_polygon.color]
        self.default_lines = [self.line_color] + default_lines
        self.last_pos = (0, 0)
        self.count_current_angles = self.current_polygon.count_angles
        self.buttons = [
            Button(425, 103, delete_button, self.restart),
            Button(500, 103, add_button, self.add_random_polygon),
            Button(575, 103, add_button, self.add_random_line),
            Button(650, 103, switch_button, self.switch),
        ]
        self.texts = texts

    def reload_screen(self):
        # reloading screen and filling with grey color
        self.screen.fill(self.bg_color)

    def clear_polygon(self):
        # clear polygons:[list]
        self.polygons = []

    def restart(self):
        self.clear_polygon()
        self.reload_screen()

    def add_random_polygon(self):
        random_polygon = Polygon()
        positions = [random_position() for _ in range(random_polygon.count_angles)]
        for i in range(random_polygon.count_angles):
            line = Line(positions[i][0], positions[i][1])
            line.end_pos.x = positions[(i + 1) % random_polygon.count_angles][0]
            line.end_pos.y = positions[(i + 1) % random_polygon.count_angles][1]
            random_polygon.lines.append(line)
        random_polygon.color = self.line_color[-1]
        random_polygon.calculate_distance()
        self.polygons.append(random_polygon)

    def add_random_line(self):
        self.current_polygon.add_line(random_position())

    def switch(self):
        self.draw = not self.draw
        self.restart()
        if not self.draw:
            self.add_random_polygon()

    def get_color(self, pos):
        # get color in current pixel
        self.current_polygon.color = self.screen.get_at(pos)
        self.line_color[-1] = self.current_polygon.color

    def render_rect(self):
        # rendering all default rectangles
        for rect in self.rects:
            pygame.draw.rect(self.screen, rect[-1], (rect[0], rect[1], rect[2], rect[3]))

    def render_button(self):
        # rendering all buttons
        for button in self.buttons:
            button.draw(self.screen)

    def render_text(self):
        # rendering default text
        for text in self.texts:
            self.screen.blit(text[0], text[1])
        if not self.draw:
            for text in texts_for_polygon:
                self.screen.blit(text[0], text[1])
            for polygon in self.polygons:
                for corner, line in enumerate(polygon.lines):
                    angles_text = [
                        [
                            font.render(
                                polygon.corner_name[corner][0], True, (255, 0, 0)
                            ),
                            (line.start_pos.x - radius - 5, line.start_pos.y - radius - 5),
                        ],
                        [
                            font.render(
                                f'{polygon.corner_name[corner][0]}: ({line.start_pos.x}, {line.start_pos.y})', True,
                                (0, 0, 0)
                            ),
                            (polygon.corner_name[corner][1]),
                        ],
                    ]
                    for angle in angles_text:
                        self.screen.blit(angle[0], angle[1])
            for polygon in self.polygons:
                for angle in range(self.count_current_angles):
                    angles_text = [
                        [
                            font.render(
                                f'<{polygon.corner_name[angle][0]}: {polygon.angles[angle]:.2f}°', True, (0, 0, 0)
                            ),
                            (polygon.corner_name[angle][2]),
                        ],
                        [
                            font.render(
                                f'{polygon.corner_name[angle][3][0]}: {polygon.sides_length[angle]:.2f}', True,
                                (0, 0, 0)
                            ),
                            (polygon.corner_name[angle][3][1])
                        ]
                    ]
                    for corner in angles_text:
                        self.screen.blit(corner[0], corner[1])

    def render_default_line(self):
        # rendering default lines
        for line in self.default_lines:
            pygame.draw.line(self.screen, line[-1], (line[0], line[1]), (line[2], line[3]))

    def render_current_circle(self, pos):
        if not self.draw:
            for polygon in self.polygons:
                for line in polygon.lines:
                    x_range, y_range = get_circle_range(line.start_pos.x, line.start_pos.y)
                    if pos[0] in x_range and pos[1] in y_range:
                        width = 0
                    else:
                        width = 1
                    pygame.draw.circle(
                        self.screen, polygon.color,
                        (line.start_pos.x, line.start_pos.y),
                        radius, width=width
                    )

    def render_polygon(self):

        if len(self.current_polygon.lines) == self.current_polygon.count_angles:
            # if drew three lines, then calculating all metrics
            self.current_polygon.calculate_distance()
            # then adding current polygon in polygons:[list]
            self.polygons.append(self.current_polygon)

            # restarting current polygon
            self.current_polygon = Polygon()
            self.current_polygon.color = self.line_color[-1]

        # rendering all polygons in polygons:[list]
        for polygon in self.polygons:
            for line in polygon.lines:
                pygame.draw.line(
                    self.screen, polygon.color,
                    (line.start_pos.x, line.start_pos.y),
                    (line.end_pos.x, line.end_pos.y)
                )

    def render_current_polygon(self, pos):
        # rendering current polygon
        if len(self.current_polygon.lines):
            for line in self.current_polygon.lines[:-1]:
                pygame.draw.line(
                    self.screen, self.current_polygon.color,
                    (line.start_pos.x, line.start_pos.y),
                    (line.end_pos.x, line.end_pos.y)
                )
            if pos[1] > 100 and pos[0] < 400:
                self.last_pos = pos  # remember current position
                pygame.draw.line(
                    self.screen, self.current_polygon.color,
                    (self.current_polygon.lines[-1].start_pos.x,
                     self.current_polygon.lines[-1].start_pos.y),
                    (pos[0], pos[1])
                )
            else:
                # draw line with last position if we leave screen
                pygame.draw.line(
                    self.screen, self.current_polygon.color,
                    (self.current_polygon.lines[-1].start_pos.x,
                     self.current_polygon.lines[-1].start_pos.y),
                    (self.last_pos[0], self.last_pos[1])
                )

    def change_current_pos(self, pos):
        mouse_click = pygame.mouse.get_pressed()

        if not self.draw and mouse_click[0]:
            for polygon in self.polygons:
                for line in polygon.lines:
                    if pos[0] < 400 and pos[1] > 100:
                        x_range_start, y_range_start = get_circle_range(line.start_pos.x, line.start_pos.y)
                        if pos[0] in x_range_start and pos[1] in y_range_start:
                            line.start_pos.x = pos[0]
                            line.start_pos.y = pos[1]
                        x_range_end, y_range_end = get_circle_range(line.end_pos.x, line.end_pos.y)
                        if pos[0] in x_range_end and pos[1] in y_range_end:
                            line.end_pos.x = pos[0]
                            line.end_pos.y = pos[1]
                polygon.calculate_distance()

    def click(self):
        mouse_click = pygame.mouse.get_pressed()
        position = pygame.mouse.get_pos()
        if mouse_click[0]:
            if self.draw:
                if position[1] > 100 and position[0] < 400:
                    self.current_polygon.add_line(position)
            if position[1] > 100 and position[0] > 400:
                if self.draw:
                    for button in self.buttons[:-1]:
                        if button.rect.collidepoint(position):
                            button.do_it()
                if self.buttons[-1].rect.collidepoint(position) and not len(self.current_polygon.lines):
                    self.buttons[-1].do_it()
            elif position[1] < 100 and position[0] < 600:
                self.get_color(position)

    def update(self):
        self.reload_screen()
        self.render_polygon()
        self.render_current_circle(pygame.mouse.get_pos())
        self.render_current_polygon(pygame.mouse.get_pos())
        self.render_rect()
        self.render_default_line()
        self.render_button()
        self.change_current_pos(pygame.mouse.get_pos())
        self.render_text()
        pygame.display.update()
