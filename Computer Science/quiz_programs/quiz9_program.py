# This prgram is going to print "Hello" over the bug image
import color
import pygame
import pygame_helper

pygame.init()

# load image of bug
img = pygame.image.load("bug.jpg")

# get the dimensions of the image surface
width = img.get_width()
height = img.get_height()

# create a window of the same size
win = pygame.display.set_mode((width, height))

# ensure colors are correct
img = img.convert_alpha()

# create a font object to render text image surfaces
font = pygame.font.SysFont("Veranda", 60)

# Now I am going to place the bug image to the window
win.blit(img, (0, 0))

pygame.display.update()

# I have to establish the coordinates first
msg = font.render("Hello", True, color.white)
msg_width = msg.get_width()
msg_height = msg.get_height()

# Im going to draw a black triangle for the text to be printed on
rectangle = pygame.draw.rect(win, color.black, ((width // 2 - (msg_width // 2), height // 2 - (msg_height // 2), msg_width, msg_height)))

# Now I have to blit the text and text box to the center of the image
win.blit(msg, (width // 2 - (msg_width // 2), height // 2 - (msg_height // 2)))



# update window and pause
pygame.display.update()
pygame_helper.wait_for_click()