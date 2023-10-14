# animation including an imagine in pygame
import random

import color
import pygame
import pygame_helper

def move(x, y, dx, dy, dt):
    """
    A function that moves a ball based on a starting location and velocity
    :param x: initial x-coordinate
    :param y: initial y - coordinate
    :param dx: horizontal velocity
    :param dy: vertical velocity
    :param dt: time elapsed
    :return: (x, y, dx, dy) of the update location and velocity
    """
    x = x + dx * dt
    y = y + dy * dt

    # check if we hit a side wall
    if x < 0:
        x = 0
        dx = -dx
    elif x + ball_width >= side:
        x = side - ball_width
        dx = -dx

    if y < 0:
        y = 0
        dy = -dy
    elif y + ball_height >= side:
        y = side - ball_height
        dy = -dy

    return (x, y, dx, dy)


pygame.init()

side = 600
win = pygame.display.set_mode((side, side))

win.fill(color.black)

# load an image file with pygame
ball = pygame.image.load("ball.png").convert_alpha()
# get width returns the number of pixels wide for the surface
ball_width = ball.get_width()
ball_height = ball.get_height()
ball_x = side // 2 - ball_width // 2
ball_y = side // 2 - ball_height // 2

# initial velocity (px/s)
ball_dx = side // random.random()
ball_dy = side // random.random()

pygame_helper.wait_for_click()

# create a pygame "stopwatch" object
clock = pygame.time.Clock()
# loop for animation
while True:
    # erase the window
    win.fill(color.black)

    # check the amount of time since the last iteration
    # tick tells us how many milliseconds have elapsed since the last tie we called the function
    # divide by 1000 we get seconds
    # 60 limits the animation frame rate to 60 fps
    time_elapsed = clock.tick(60) / 1000

    # move the ball
    ball_x, ball_y, ball_dx, ball_dy = move(ball_x, ball_y, ball_dx, ball_dy, time_elapsed)

    # draw the ball
    win.blit(ball, (ball_x, ball_y))

    # update the screen
    pygame.display.update()


win.blit(ball, (ball_x, ball_y))

pygame.display.update()
pygame_helper.wait_for_click()