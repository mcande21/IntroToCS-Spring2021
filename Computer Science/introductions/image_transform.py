# program to edit images with pygame
import color
import pygame
import pygame_helper

def darken(r, g, b):
    """
    Darken a pixel/RGB value by 30%
    :param r:
    :param g:
    :param b:
    :return: updated/darken (R,G,B) value
    """
    r = int(r * 0.7)
    g = int(g * 0.7)
    b = int(b * 0.7)
    return (r,g,b)

def make_red(r, g, b):
    return(r, 0, 0)

# scramble the values
def scramble(r, g, b):
    return(g, b, r)

def negavtive(r, g, b):
    return(255 - r, 255 - g, 255 - b)

#compute grey scale by taking average of values
def bandw(r, g, b):
    sum = r + g + b
    gray = sum // 3
    return (gray, gray, gray)

# weighted average of pixel values to get a more pleasing grayscale
# weights are derived from the biology of human eye
def better_gray(r,g,b):
    gray = int(0.3*r + 0.59*g + 0.11*b)
    return (gray, gray, gray)

# this is a wierd effect that changes all the pixels to white or black
def weird_effect(r,g,b):
    if r % 2 == 1:
        return color.black
    else:
        return color.white

def maybe_gray(r, g, b):
    if g < 100 and b < 100:
        return (r, g, b)
    else:
        g = int(0.3 * r + 0.59 * g + 0.11 * b)
        b = int(0.3 * r + 0.59 * g + 0.11 * b)
        return (r, g, b)


pygame.init()

# load the image
image = pygame.image.load("hidden_message.png")
width = image.get_width()
height = image.get_height()

# make a window the same size as the image
win = pygame.display.set_mode((width, height))

# now that we have our window we can process any transparency in our image
image = image.convert_alpha()

# blit the image dawg
win.blit(image, (0, 0))

pygame.display.update()
pygame_helper.wait_for_click()

# loop through all rows and y coordinates in the image
for y in range(height):
    # going to loop through all columns or x coordinates
    for x in range(width):
        # x,y is one specific pixel in the image
        # read the RGB value from the pixel
        (r, g, b, a) = image.get_at((x,y))
        # change this value
        (r1, g1, b1) = maybe_gray(r, g, b)
        # update the RGB color at that pixel
        image.set_at((x,y), (r1, g1, b1))

# re-blit the image
    win.blit(image, (0,0))
    pygame.display.update()
pygame_helper.wait_for_click()

