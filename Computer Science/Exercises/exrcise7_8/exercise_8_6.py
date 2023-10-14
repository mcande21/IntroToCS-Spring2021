# importing modules to use in coding
import color
import pygame
import pygame_helper

# calling on pygame
pygame.init()

# creating program window
# dimensions of the graphics window
width = 400
height = 300

# instructing pygame to use dimensions to construct window
win = pygame.display.set_mode((width, height))

# filling the graphics window light gray
win.fill(color.lightgray)

# Drawing a gray circle in the top right of the window
# draw a circle
x = width // 1.5
y = height // 4
radius = height // 8
pygame.draw.circle(win, color.darkgray, (x, y), radius)

# drawing the blue circle relative to the gray circle
bX = x - (radius * 0.5)
bY = y + (radius * 0.5)
bRadius = radius
pygame.draw.circle(win, color.blue, (bX, bY), bRadius)


# instructing pygame to update graphics window
pygame.display.update()

# instructing pygame to wait for click command
pygame_helper.wait_for_click()