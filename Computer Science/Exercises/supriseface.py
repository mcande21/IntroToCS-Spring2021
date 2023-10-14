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
eHeight = c_radius // 2.5
eX = c_x - c_x // 3
eY = c_y - c_y // 1.75
pygame.draw.ellipse(win, color.black, (eX, eY, eWidth, eHeight))

eWidth = c_radius // 4
eHeight = c_radius // 2.5
eX = c_x + c_x // 3 - eWidth
eY = c_y - c_y // 1.75
pygame.draw.ellipse(win, color.black, (eX, eY, eWidth, eHeight))

# drawing the mouth
mWidth = c_radius // 1.25
mHeight = c_radius // 1.8
mX = c_x - mWidth // 2
mY = c_y + mHeight // 8
pygame.draw.ellipse(win, color.black, (mX, mY, mWidth, mHeight))

# imma try to draw eyebrows
# yeahhhh I couldnt figure it out... kept getting "points must be number pairs"
# I'll comment out the code so you can see it
lX = c_x - 5 * c_radius // 8
lY = c_y - c_radius // 2
rX = c_x - 3 * c_radius // 8
rY = c_y - 3 * c_radius // 4
pygame.draw.line(win, color.black, (lX, lY), (rX, rY), c_radius // 20)

RX = c_x + 5 * c_radius // 8
RY = c_y - c_radius // 2
tX = c_x + 3 * c_radius // 8
tY = c_y - 3 * c_radius // 4
pygame.draw.line(win, color.black, (RX, RY), (tX, tY), c_radius // 20)

# instructing pygame to update graphics window
pygame.display.update()

# instructing pygame to wait for click command
pygame_helper.wait_for_click()