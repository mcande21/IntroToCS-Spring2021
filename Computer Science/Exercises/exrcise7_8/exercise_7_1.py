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

# drawing rectangle centered on the screen and filling
# half the vertical space and one third the horizontal
r_width = width // 2
r_height = height // 3
r_x = 0 + width // 2 - r_width // 2
r_y = 0 + height // 2 - r_height // 2
pygame.draw.rect(win, color.darkgray, (r_x, r_y, r_width, r_height))


# instructing pygame to update graphics window
pygame.display.update()

# instructing pygame to wait for click command
pygame_helper.wait_for_click()