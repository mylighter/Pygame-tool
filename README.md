# Pygame-tool
## Brief Introduction
A tool to help programmers to create a UI with Pygame easier and faster.
## Quick Start
### Definitions
##### Sprite
In Pygame Tool, each widget has its own "space", which is a Rect used to format the widget, and the widget together with its "space" is called a "sprite".
## Sprite
In the simpliest way, You can just follow the instruction of each widget and create instances of them.

Here is an example for creating and using a widget:
```
import sys
import pygame
import pygame_tool as pt
import pygame_tool.shortcuts as ps


pygame.init()
screen = ps.create_window((1080, 608))
text = pt.Text("HELLO, WORLD!", style=ps.Styles.DEFAULT_T) # <-- Create a new widget
list_ = pt.List(["A", "B", "C"], ps.Styles.DEFAULT_L) # <-- Create a new widget
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
  list_.compose() # Use '.compose()' if it has.
  list_.blit(screen) # <-- Blit the widget on the screen
  text.blit(screen) # <-- Blit the widget on the screen
  pygame.display.update()

```
In the same way, you can create all kinds of widgets in pygame-tool.

### Positions
In this case, if you want to move a sprite, you can do it like this (only works here, don't do the same thing on a sprite contained by a stage!):
```
[target].sprite.rect.topleft = tuple[int, int]
```
### Let Widgets Handle Events
Widgets such as Button is expected to be able to handle click event. As a result, all widgets that can be triggered have a function ".update()".

Function ".update()" takes an event and check it. If the event needs handling, the function will use the event as well as the current position of your mouse to handle the specific event.

This function should be used like this:
```
import sys
import pygame
import pygame_tool as pt
import pygame_tool.shortcuts as ps


pygame.init()
screen = ps.create_window((1080, 608))
button = pt.Button("Click!", style=ps.Styles.DEFAULT_B)
while True:
  mouse_pos = pygame.mouse.get_pos()
  for event in pygame.event.get():
    button.update(event, mouse_pos) #<---
    if event.type == pygame.QUIT:
      sys.exit()
  button.blit(screen)
  pygame.display.update()
```
## Stages
In order to manage the sprites, we can create a Stage instance. Usually, you only need to create a Stage, append the sprite, and use ".show(screen)" in the mainloop.
It's worth mentioning that the stage won't update the sprites, so you have to update them respectively. The method was introduced above.

Here's an example for how to use a stage to operate a group of sprites:
```
import pygame
import os
import sys
import pygame_tool as tool
import pygame_tool.extensions as ext
import pygame_tool.shortcuts as ps


os.environ['SDL_VIDEO_CENTERED'] = "1"
data = [('First', 1), ('Second', 0.3), ('Third', 0.4), ('Fourth', 0.8), ('Fifth', 0.5), ('Sixth', 0.34)]
screen = ps.create_window((1080, 608))
d_stage = tool.stage.Stage()
a_button = tool.Button(ps.Styles.DEFAULT_B, "Testing", mode=1)
a_switch = ext.Switch(ps.Styles.DEFAULT_B, 'Test', position=(400, 400))
a_slipper = ext.Slipper(position=(640, 240))
a_text = tool.Text(
    text="HELLO WORLD!", style=ps.Styles.DEFAULT_B, position=(0, 0)
)
a_barchart = ext.Barchart(
    data, ps.Styles.DEFAULT_L, ps.Styles.DEFAULT_SB, (60, 60)
)
d_stage.append(a_button)
d_stage.append(a_text)
d_stage.append(a_barchart)
d_stage.append(a_switch)
d_stage.append(a_slipper)
a_button.space.rel_pos.left = 400
a_text.space.rel_pos.left = 500


while True:
    screen.fill((81, 81, 81))
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        a_button.update(event, mouse)
        a_switch.update(event, mouse)
        a_slipper.update(event, mouse)
        if event.type == pygame.QUIT:
            sys.exit()
    d_stage.show(screen)
    pygame.display.update()
```
### Positions
Positions of sprites on stages are more complicated. There are two types: Absolute Position and Relative Position
#### Absolute Position
This one is quite easy and useless. If you want to use absolute positions, you could just not use stages.

The code of moving the sprites is the same as that in Sprite-Positions. It's worth mentioning that you should always compose the sprites seperately and use ```Stage.blit()``` instead of using ```Stage.show()```

#### Relative Position
This is why stages are created. Sometimes you'll find that you need to move a group of sprites. At this time, you could put them in one stage and move the whole stage. Just do like this:
```
Stage.ox, Stage.oy = tuple[int, int]
```

And you'll find that you sometimes need to place the sprites on different points on a stage. In that case, you can just use:
```
Widget.sprite.rel_pos.topleft = tuple[int, int]
```
By the way, ```Widget.sprite.rel_pos``` is a pygame.Rect instance. Therefore, you can simply move it as a normal rect.

At last, don't forget that if you have changed the position (no matter which position, the stage's one or the sprites' ones) when the mainloop is running, you should set "Stage.need_composing" to True.

