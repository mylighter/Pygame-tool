from .styles import *
from .stage import *
import pygame
import os


# Init variables
version = '1.0.0'
"""
Attention: all the positions and sizes given should be formatted like this: (x, y) or (width, height)
注意：所有传入的坐标和size参数都应为(x, y) 或 (宽度, 高度) 形式
"""
print("Pygame Tool By Mylights\nVersion: ", version)
base_dir = tool_base_dir = os.path.dirname(os.path.abspath(__file__))
pygame.font.init()


class Text:
    def __init__(self, style, text=None, position=(0, 0)):
        """
        Used to display a line of text. Move Text.space.rect to place the text block.\n
        用于显示一行文字。操作Text.space.rel_pos来放置文本。
        :param style: A style instance that describes the look of the text. 文字样式
        :param text: The text to show. 文本
        :param position: Where the widget will be located. 组件位置
        """
        self.color = style.color
        self.font = style.font
        self.text = self.font.render(text, True, self.color) if text else None
        self.rect = self.text.get_rect() if self.text else None
        self.space = Sprite(position, self.rect.size)

    def show(self, text):
        """Change the text that will be displayed.\n
        更改显示的文字
        :param text: The new text to show on the screen. 将被显示的新文本
        """
        self.text = self.font.render(text, True, self.color)
        self.rect = self.text.get_rect()
        self.space.rect.size = self.rect.size
        self.space.rel_pos.size = self.rect.size

    def blit(self, screen):
        """Show the text.\n显示该文本"""
        if not self.text:
            return False
        self.rect.topleft = self.space.rect.topleft
        screen.blit(self.text, self.rect)


class Button:
    def __init__(self, style: ButtonStyle, prep="Button", position=(0, 0), mode=0):
        """
        A Button that can be clicked. Try to use a function as a mode!\n
        一个普通的按钮，你可以试试将一个函数作为mode参数传入
        :param style: A style instance that describes the look of the button. 按钮样式
        :param prep: The text to show on the button. 按钮文本
        :param position: Where the widget will be located. 组件位置
        :param mode: How you want to handle a click. 按钮按下的响应方式
        """
        self.background = style.background
        self.color = style.color
        self.prep = Text(style, text=prep)
        self.rect = pygame.Rect(0, 0, style.width, style.height)
        self.status = False
        self.space = Sprite(position, (style.width, style.height))
        self.mode = mode

    def update(self, event: pygame.event.Event, mouse_pos=False, args=()):
        """Being Used to check if the button is clicked.
        用于检测按钮是否按下
        :param event: An event in pygame.event.get()    pygame.event.get()返回序列中的一项
        :param mouse_pos: The position of your mouse.   鼠标坐标
        :param args: To be the parameters of interrupt function if you have.    如果有中断函数，则该参数为中断函数的参数"""
        x, y = mouse_pos if mouse_pos else pygame.mouse.get_pos()
        if self.rect.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONDOWN:
            if self.mode == 0:
                self.status = not self.status
            elif self.mode == 1:
                self.status = True
            elif callable(self.mode):
                self.mode(*args)
                self.status = not self.status
        if self.mode == 1 and event.type == pygame.MOUSEBUTTONUP:
            self.status = False

    def compose(self):
        """Compose the button. To be used before Button.blit()\n
        组装按钮，Button.blit()前使用。"""
        self.rect.topleft = self.space.rect.topleft
        self.prep.space.rect.center = self.rect.center

    def blit(self, screen):
        """Blit the button on the screen.\n
        在屏幕上显示"""
        screen.fill(self.background, self.rect)
        self.prep.blit(screen)


class List:
    def __init__(self, data, style: ListStyle, position=(0, 0)):
        """
            A composition of lines of text and a title.\n
            多行文字以及标题
            :param data: Texts you want to display. 要显示的文本
            :param style: A style object that describes the look of the list. 列表样式
            :param position: Where the widget will be located. 起始（左上）坐标
        """
        self.data = list(data)
        self.space = Sprite(position)
        self.displayed = []
        self.font = style.font
        self.color = style.color
        self.spare = style.line_height

    def load(self):
        """
        To render the texts. 渲染文本
        :return: None
        """
        self.displayed.clear()
        for i, datum in enumerate(self.data):
            text = self.font.render(datum, True, self.color)
            rect = text.get_rect()
            self.displayed.append((i, text, rect))

    def blit(self, screen, with_compose=True):
        """
        Blit the list on the screen. 将本列表显示在屏幕上
        :param screen: The screen to display the list on. 显示列表的屏幕
        :param with_compose: If the list will be formatted before being displayed. 是否在显示列表前将期组合好
        :return: None
        """
        for i, text, rect in self.displayed:
            if with_compose:
                rect.top = self.space.rect.top - i * self.spare
                rect.left = self.space.rect.left
            screen.blit(text, rect)
