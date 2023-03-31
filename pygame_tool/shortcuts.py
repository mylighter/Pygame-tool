from .styles import *
import pygame
import os


class BTNMode:
    SWITCH = 0
    TRIGGER = 1


class Styles:
    DEFAULT_T = TextStyle()
    DEFAULT_L = ListStyle(DEFAULT_T)
    DEFAULT_B = ButtonStyle()
    DEFAULT_SB = ScaleBarStyle()


def create_window(size, flags=0):
    os.environ['SDL_VIDEO_CENTERED'] = "1"
    screen = pygame.display.set_mode(size, flags)
    return screen
