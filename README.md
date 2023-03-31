# Pygame-tool
A tool to help programmers to create a UI with Pygame easier and faster.
## Quick Start
In the simpliest way, You can just follow the instruction of each class(widget) and create instances in order to add some "sprites" to the screen.  

Here is an example:
```
import sys
import pygame
import pygame_tool as pt
import pygame_tool.shortcuts as ps


pygame.init()
screen = ps.create_window((1080, 608))
text = pt.Text("HELLO, WORLD!", style=ps.Styles.DEFAULT_T)
list_ = pt.List(["A", "B", "C"], ps.Styles.DEFAULT_L)
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
  list_.compose() # Use '.compose()' if it has.
  list_.blit(screen)
  text.blit(screen)
  pygame.display.update()

```
In the same way, you can create all kinds of widgets in pygame-tool.

By the way, if you want to move a sprite, do it like this:
```
[target].sprite.rect.topleft = tuple[int, int]
```
## How to Let Widgets Handle Events
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
    button.update(event, mouse_pos)
    if event.type == pygame.QUIT:
      sys.exit()
  button.blit(screen)
  pygame.display.update()
```
## Stages
In order to manage the sprites, we can create a Stage instance. Usually, you only need to create a Stage, append the sprite, and use ".show(screen)" in the mainloop.
It's worth mentioning that the stage won't update the sprites, so you have to update them respectively. The method was introduced above.


This introduction has not been done yet.
