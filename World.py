import random
from Entity import Entity
from Vector import Vector
import pygame

green = (0, 255, 0)


class World:
    entities = []
    desired = []

    def __init__(self, size, agent_num, screen):
        self.screen = screen
        self.size = Vector(size)
        self.agent_num = agent_num

    def start(self):
        for i in range(self.agent_num):
            self.entities.append(
                Entity("agent", (random.randint(0, self.size.getX()), random.randint(0, self.size.getY())),
                       random.uniform(0, 2),
                       random.uniform(0, 360),
                       random.uniform(6, 10), "circle", 1, 1, 0.003))
            self.desired.append(Vector((random.uniform(0, self.size.getX()), random.uniform(0, self.size.getY()))))

    def do_step(self):
        for num, e in enumerate(self.entities):

            if (e.get_location() - self.desired[num]).get_length() < 1:
                self.desired[num] = Vector((random.randint(0, self.size.getX()), random.randint(0, self.size.getY())))
            e.update_new_pos(self.desired[num])
            # e.draw(self.screen)
            pygame.draw.circle(self.screen, green, self.desired[num].tuple(), 1)
            self.draw_entity(e)

    def draw_entity(self, e):
        e.draw(self.screen)
