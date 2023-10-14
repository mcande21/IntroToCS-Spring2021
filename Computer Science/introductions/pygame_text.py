# This program is an example of displaying text in a pygame window
import color
import pygame
import pygame_helper

pygame.init()
width = 600
height = 600

win = pygame.display.set_mode((width, height))

win.fill(color.white)

# create a font object
font = pygame.font.SysFont("Veranda", 60)

# render som text into a pygame surface
# True => tunrs on "anti-aliasing", which smooths the curves of the text
msg = font.render("Example Text", True, color.black)

# center the text
msg_width = msg.get_width()
msg_height = msg.get_height()
msg_x = width // 2 - msg_width // 2
msg_y = height // 2 - msg_height // 2

win.blit(msg, (msg_x, msg_y))

pygame.display.update()
pygame_helper.wait_for_click()