import pygame
import random
import math
from Entity import Entity
from Vector import Vector

pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
screen = pygame.display.set_mode((800, 800))

colors = [red, green, blue]

running = True
x = 400
y = 400
r = 10
v = 1
random.seed(None, 2)

heading = random.uniform(0, 360)


def get_distxy(vel, h):
    distx = vel * math.cos(math.radians(heading))
    disty = vel * math.sin(math.radians(heading))
    return distx, disty


def check_bounds(c, h, x, y):
    if x < 0 + r or x > 800 - r:
        h = 180 - h
        c = (c + 1) % 3
    if y < 0 + r or y > 800 - r:
        h = 360 - h
        c = (c + 1) % 3
    return h, c


entities = []
desireds = []
for i in range(100):
    entities.append(
        Entity("agent", (random.randint(0, 800), random.randint(0, 800)), random.uniform(0, 2), random.uniform(0, 360),
               random.uniform(6, 10), "circle", 1, 0.5, 1))
    desireds.append(Vector((random.uniform(0, 800), random.uniform(0, 800))))
test_E = Entity("agent", (400, 400), 1, 35, 6, "circle", 1, 0.5, 1)
desired = Vector((200, 200))
c = 0
# Game Loop
while running:
    # print(desired.tuple())
    screen.fill(black)
    for num, e in enumerate(entities):

        if (e.get_location() - desireds[num]).get_length() < 1:
            desireds[num] = Vector((random.randint(0, 800), random.randint(0, 800)))
        e.update_new_pos(desireds[num])
        e.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
