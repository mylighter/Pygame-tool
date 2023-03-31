import pygame.font as pf


class TextStyle:
    def __init__(self, font='Arial', size=12, color=(0, 0, 0), bold=False, italic=False):
        self.font = pf.SysFont(font, size, bold, italic)
        self.color = color


class ListStyle(TextStyle):
    def __init__(self, title_style: TextStyle, font='Arial', font_size=12, font_color=(0, 0, 0),
                 size=(False, False), line_height=20, background=None, side='l'):
        super(ListStyle, self).__init__(font, font_size, font_color)
        self.width, self.height = size
        self.background = background
        self.line_height = line_height
        self.side = side
        self.title_style = title_style


class ButtonStyle(TextStyle):
    def __init__(self, font='Arial', font_size=12, color=(0, 0, 0), background=(200, 200, 200), size=(40, 20)):
        super(ButtonStyle, self).__init__(font, font_size, color)
        self.background = background
        self.width, self.height = size


class ScaleBarStyle(TextStyle):
    def __init__(self, font='Arial', font_size=12, font_color=(0, 0, 0),
                 size=(100, 20), color=(102, 204, 255), background=(240, 240, 240)):
        super(ScaleBarStyle, self).__init__(font, font_size, font_color)
        self.width, self.height = size
        self.front_color = color
        self.background = background
