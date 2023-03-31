import pygame


class Sprite:
    def __init__(self, origin=(0, 0), size=(0, 0)):
        """
        A container for a single widget. \n
        单个组件的容器
        :param origin: The left-top point of the sprite. 起始点（左上）坐标
        :param size: The size of the sprite. 大小
        """
        self.rect = pygame.Rect(*origin, *size)
        self.rel_pos = pygame.Rect(*origin, *size)


class Stage:
    def __init__(self, origin_pos=(0, 0), visible=True, sprites=()):
        """
        A container for a group of widgets. The positions of the widgets is related to the position of the stage.\n
        一组组件的容器。组件的坐标是相对于stage的起始坐标而言的。
        :param origin_pos: The left-top position of the stage. 舞台起始点（左上）
        :param visible: If the stage is visible. 舞台是否可见
        :param sprites: The sprites to be added to the stage. 舞台上的Sprites
        """
        self.ox, self.oy = origin_pos
        self.visible = visible
        self.sprites = list(sprites)
        self.need_composing = True

    def compose_all(self):
        """
        Compose all the sprites if necessary. 组合所有需要组合的sprite
        :return: None
        """
        for sprite in self.sprites:
            x, y = sprite.space.rel_pos.topleft
            sprite.space.rect.topleft = (x + self.ox, y + self.oy)
            try:
                sprite.compose()
            except AttributeError:
                pass

    def blit_all(self, screen):
        """
        Blit all the sprites on the screen if the stage is visible. 强制将所有sprite显示到屏幕上
        :param screen: The screen to blit the sprites on. 用于显示的screen
        :return: None
        """
        for ele in self.sprites:
            ele.blit(screen)

    def append(self, o):
        """
        Append a sprite to the stage. 向该stage添加一个sprite
        :param o: The sprite 要添加的sprite
        :return: If the sprite has already been contained by the stage. 要添加的sprite是否已存在于该stage上。
        """
        if o not in self.sprites:
            self.sprites.append(o)
            return False
        return True

    def show(self, screen):
        """
        Show the whole stage (including compose_all and blit_all). 在stage可见的情况下显示stage上的全部组件
        :param screen: The screen to place the stage on. 用于显示的screen
        :return: None
        """
        if self.visible:
            if self.need_composing:
                self.compose_all()
                self.need_composing = False
            self.blit_all(screen)
