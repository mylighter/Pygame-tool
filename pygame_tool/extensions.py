import pygame.font
from . import *
from .styles import *
from .stage import *


class ScaleBar:
    def __init__(self, style: ScaleBarStyle, scale, position=(0, 0)):
        """
        A group of rectangles that can show a scale. 一堆用于显示一个比例的矩形（进度条或比例条）
        :param style: A style instance that describes the look of the scale bar. 比例条样式
        :param scale: The scale to show. 将要展示的比例
        :param position: The left-top position of the scale bar. 起始点（左上）
        Set it to False if you want to disable relative position. 如果要关闭相对坐标模式，将该参数设为False
        """
        self.bg_rect = pygame.Rect(*position if position else (0, 0), style.width, style.height)
        self.data_rect = pygame.Rect(*position if position else (0, 0), int(style.width*scale), style.height)
        self.bg_color = style.background
        self.color = style.front_color
        self.prep = style.font.render('%.3f' % scale, True, style.color)
        self.p_rect = self.prep.get_rect()
        self.space = Sprite(position, (style.height, style.width+self.p_rect.width+10)) if position else False

    def compose(self):
        """
        Compose the scale bar. 组装比例条
        :return: None
        """
        if self.space:
            self.bg_rect.topleft = self.space.rect.topleft
        self.data_rect.topleft = self.bg_rect.topleft
        self.p_rect.centery = self.bg_rect.centery
        self.p_rect.left = self.bg_rect.right + 10

    def blit(self, screen):
        """
        Blit the scale bar on a certain screen. 将该比例条显示在屏幕上。
        :param screen: The screen to display the widget on. 用于显示的screen
        :return: None
        """
        screen.fill(self.bg_color, self.bg_rect)
        screen.fill(self.color, self.data_rect)
        screen.blit(self.prep, self.p_rect)


class Barchart:
    def __init__(self, data, style: ListStyle, bar_style: ScaleBarStyle, position=(0, 0)):
        """
        A bar chart that can show a dictionary. 一个能显示字典的条形统计图（横向）
        :param data: The data to show. 显示的数据
        :param style: A style object that describes the look of the bar chart. 条形统计图样式
        :param bar_style: A style object that describes the look of each scale bar. 单个比例条样式
        :param position: The left-top position of the bar chart. 起始位置（左上）
        """
        self.bars = []
        self.bar_style = bar_style
        self.style = style
        self.font = style.font
        for prep, datum in data:
            bar = ScaleBar(self.bar_style, datum, position=False)
            prep = self.font.render(prep, True, style.color)
            self.bars.append(((prep, prep.get_rect()), bar))

        self.space = Sprite(position, size=(self.bar_style.width, self.style.line_height*len(data)))

    def compose(self):
        """
        Compose the scale bar. 组装该统计图。
        :return: None
        """
        for i, (prep, bar) in enumerate(self.bars):
            bar.bg_rect.left = self.space.rect.left
            bar.bg_rect.top = self.space.rect.top + i*self.style.line_height
            bar.compose()
            prep[1].top = bar.bg_rect.top
            prep[1].right = bar.bg_rect.left - 10

    def blit(self, screen):
        """
        Blit the bar chart on a certain screen. 将该条形统计图显示在屏幕上
        :param screen: The screen to display the widget on. 用于显示的screen
        :return: None
        """
        for (prep, p_rect), bar in self.bars:
            screen.blit(prep, p_rect)
            bar.blit(screen)


class Switch:
    def __init__(self, style: ButtonStyle, text, preps=('off', 'on'), bg_color=(32, 32, 32), position=(0, 0)):
        """
        Just a switch with two statuses. 开关（或者叫拉杆）
        :param text: The text to describe the switch. 描述语
        :param style: A style instance that describes the look of the button of the switch. 开关中按钮的样式
        :param position: The left-top position of the widget. 组件起始位置（左上）
        :param preps: The text to show on the switch to show the status. 用于展示当前状态的文本（显示在开关上）
        :param bg_color: The background color of the switch. 背景颜色
        """
        self.font = style.font
        self.text = Text(style, text)
        self.preps = preps
        self.width = int(style.width * 1.5)
        self.height = style.height
        self.background = pygame.Rect(0, 0, self.width, self.height)
        self.color = bg_color
        self.switch = Button(style, preps[0], mode=None)
        self.switch.mode = self.switch.prep.show
        self.space = Sprite(position, (self.width, self.height))

    def update(self, event, mouse_pos):
        """
        Check if the switch is clicked. 检测开关是否被按下
        :param event: An event in the returned list of pygame.event.get()
        :param mouse_pos: The position of your mouse. 鼠标坐标
        :return: If the status was changed. 状态是否改变
        """
        pre_s = self.switch.status
        self.switch.update(event, mouse_pos, (self.preps[not self.switch.status],))
        if self.switch.status:
            self.switch.space.rect.right = self.background.right
        else:
            self.switch.space.rect.left = self.background.left
        if not self.switch.status == pre_s:
            self.switch.compose()

    def compose(self):
        """
        Compose the switch. 组装开关
        :return: None
        """
        self.background.topleft = self.space.rect.topleft
        self.switch.space.rect.top = self.background.top
        if self.switch.status:
            self.switch.space.rect.right = self.background.right
        else:
            self.switch.space.rect.left = self.background.left
        self.switch.compose()
        self.text.space.rect.right = self.background.left - 8
        self.text.space.rect.centery = self.background.centery
        self.text.space.settle()

    def blit(self, screen):
        """
        Blit the switch on a certain screen 显示开关
        :param screen: The screen to display the widget on. 用于显示该组件的screen
        :return: None
        """
        screen.fill(self.color, self.background)
        self.switch.blit(screen)
        self.text.blit(screen)


class Slipper(object):
    def __init__(self, width=100, height=10, bg_color=(100, 100, 100), color=(200, 200, 200), position=(0, 0)):
        """
        A slipper to change a value easily. 一个滑动条
        :param width: The width of the slipper. 宽
        :param height: The height of the slipper. 高
        :param bg_color: The color of the background. 背景颜色
        :param color: The color of the slipper. 滑动块颜色
        :param position: The left-top position of the slipper. 起始点（左上）
        """
        self.width = width
        self.height = height
        self.color = bg_color
        self.slipper_color = color
        self.rect = pygame.rect.Rect(0, 0, width, height)
        self.slipper = pygame.rect.Rect(0, 0, 5, 20)
        self.value = 0
        self.flag = False
        self.space = Sprite(position, (width, height))

    def update(self, event, mouse_pos=False):
        """
        Update the value according to the dragging. 根据鼠标的拖拽更新值
        :param event: An event in pygame.event.get()
        :param mouse_pos: The position of your mouse. 鼠标坐标
        :return: None
        """
        x, y = mouse_pos if mouse_pos else pygame.mouse.get_pos()
        if self.slipper.collidepoint(x, y) and event.type == pygame.MOUSEBUTTONDOWN:
            self.flag = True
        if event.type == pygame.MOUSEBUTTONUP:
            self.flag = False
            self.value = (self.slipper.centerx - self.rect.left) / self.width
        if self.flag:
            if self.rect.left <= x <= self.rect.right:
                self.slipper.centerx = x
            elif x > self.rect.right:
                self.slipper.centerx = self.rect.right
            else:
                self.slipper.centerx = self.rect.left

    def compose(self):
        """
        Compose the slipper. 组装滑动条
        :return: None
        """
        self.rect.topleft = self.space.rect.topleft
        self.slipper.centerx = self.rect.left + self.value * self.width
        self.slipper.centery = self.rect.centery

    def blit(self, screen):
        """
        Blit the slipper on a certain screen. 显示滑动条
        :param screen: The screen to display the widget on. 用于显示该组件的screen
        :return: None
        """
        screen.fill(self.color, self.rect)
        screen.fill(self.slipper_color, self.slipper)
