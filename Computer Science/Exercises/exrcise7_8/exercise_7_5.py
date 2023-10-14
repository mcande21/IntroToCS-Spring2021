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

# Draw a dark gray square that is centered in the
# window and fills a quarter the height of the window.
side = height // 4
square_x = width // 2 - side // 2
square_y = height // 2 - side // 2
pygame.draw.rect(win, color.darkgray, (square_x, square_y, side, side))

# drawing blue rectange placed below the grey rectangle
bSide = side
bSquare_x = square_x
bSquare_y = square_y + side
pygame.draw.rect(win, color.blue, (bSquare_x, bSquare_y, bSide, bSide))


# instructing pygame to update graphics window
pygame.display.update()

# instructing pygame to wait for click command
pygame_helper.wait_for_click()