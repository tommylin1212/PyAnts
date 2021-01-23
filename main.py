import pygame
import random
from World import World

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)

screenW = 800
screenH = 800

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
screen = pygame.display.set_mode((screenW, screenH))

colors = [red, green, blue]

running = True

random.seed(None, 2)

heading = random.uniform(0, 360)


world = World((screenW, screenH), 100, screen)
world.start()
# Game Loop

while running:

    screen.fill(black)
    world.do_step()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
