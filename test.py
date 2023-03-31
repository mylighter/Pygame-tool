import pygame
import os
import sys
import pygame_tool as tool
import pygame_tool.extensions as ext
import pygame_tool.shortcuts as ps


os.environ['SDL_VIDEO_CENTERED'] = "1"
data = [('First', 1), ('Second', 0.3), ('Third', 0.4), ('Fourth', 0.8), ('Fifth', 0.5), ('Sixth', 0.34)]
screen = ps.create_window((1080, 608))
default = tool.styles.ButtonStyle()
d_stage = tool.stage.Stage()
tester = tool.Button(default, "Testing", mode=1)
tester2 = ext.Switch(default, 'Test', position=(400, 400))
tester3 = ext.Slipper(position=(640, 240))
text_test = tool.Text(
    text="HELLO WORLD!", style=ps.Styles.DEFAULT_B, position=(0, 0)
)
tst_barchart = ext.Barchart(
    data, ps.Styles.DEFAULT_L, ps.Styles.DEFAULT_SB, (60, 60)
)
d_stage.append(tester)
d_stage.append(text_test)
d_stage.append(tst_barchart)
d_stage.append(tester2)
d_stage.append(tester3)
tester.space.rel_pos.left = 400
text_test.space.rel_pos.left = 500


while True:
    screen.fill((81, 81, 81))
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        tester.update(event, mouse)
        changed = tester2.update(event, mouse)
        tester3.update(event, mouse)
        if event.type == pygame.QUIT:
            sys.exit()
    d_stage.show(screen)
    pygame.display.update()
