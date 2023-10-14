# this program will draw out a smily face because we love smily faces
# importing the modules
import color
import pygame_helper
import pygame

# making the window
# dimensions of the graphics window
width = 800
height = 600

# instructing pygame to use dimensions to construct window
win = pygame.display.set_mode((width, height))

# filling the graphics window light gray
win.fill(color.black)

# drawing out the circle
c_radius = height // 2
c_x = width // 2
c_y = height // 2
pygame.draw.circle(win, color.yellow, (c_x, c_y), c_radius)

# drawing out them eyes
eWidth = c_radius // 4
eHeight = c_radius // 2
eX = c_x - c_x // 3
eY = c_y - c_y // 2
pygame.draw.ellipse(win, color.black, (eX, eY, eWidth, eHeight))

eWidth = c_radius // 4
eHeight = c_radius // 2
eX = c_x + c_x // 3 - eWidth
eY = c_y - c_y // 2
pygame.draw.ellipse(win, color.black, (eX, eY, eWidth, eHeight))

# Drawing the smile
sWidth = c_radius
sHeight = c_radius // 1.5
sX = c_x - c_x // 2.75
sY = c_y + c_y // 100000
pygame.draw.ellipse(win, color.black, (sX, sY, sWidth, sHeight), c_radius // 40)

rWidth = c_radius
rHeight = sHeight // 2
rX = c_x - c_x // 2.75
rY = sY
pygame.draw.rect(win, color.yellow, (rX, rY, rWidth, rHeight))

# instructing pygame to update graphics window
pygame.display.update()

# instructing pygame to wait for click command
pygame_helper.wait_for_click()