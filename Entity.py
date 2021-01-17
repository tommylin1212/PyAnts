from Vector import Vector
import math
import pygame

red = (255, 0, 0)

class Entity:
    type = None
    location = None
    shape = None
    size = None
    speed = None
    heading = None
    max_speed = None
    max_force = None
    mass = None

    def __init__(self):
        self.type = None
        self.location = None
        self.shape = None
        self.size = None
        self.speed = None
        self.heading = None
        self.max_speed = None
        self.max_force = None
        self.mass = None

    def __init__(self, type, location, speed, heading, size, shape, max_speed, max_force, mass):
        self.type = type
        self.location = Vector(location)
        self.shape = shape
        self.size = size
        self.speed = speed
        self.heading = Vector((math.cos(math.radians(heading)),math.sin(math.radians(heading)))).norm()
        self.max_speed = max_speed
        self.max_force = max_force
        self.mass = mass

    def get_type(self):
        return self.type

    def get_location(self):
        return self.location

    def get_shape(self):
        return self.shape

    def get_size(self):
        return self.size

    def get_speed(self):
        return self.speed

    def get_heading(self):
        return self.heading

    def set_type(self, t):
        self.type = t

    def set_location(self, l):
        self.location = l

    def set_shape(self, s):
        self.shape = s

    def set_size(self, s):
        self.size = s

    def set_speed(self, s):
        self.speed = s

    def set_heading(self, h):
        self.heading = h

    def get_x_vector(self):
        return self.speed * math.cos(math.radians(self.heading))

    def get_y_vector(self):
        return self.speed * math.sin(math.radians(self.heading))

    def get_new_heading(self, desired):
        steering = desired-self.heading
        steering = steering.norm()
        steering *= self.max_speed
        steering
        return steering

    def update_new_pos(self, target):
        desired=target-self.location
        desired=desired.norm()
        t_heading = desired#+self.get_new_heading(desired)

        self.set_heading(t_heading.norm()*self.max_speed)
        self.set_location(self.location+self.heading)

    def rotate_triangle(self, location, scale, heading):
        points = [(-0.5, -0.866), (-0.5, 0.866), (2.0, 0.0)]
        rotated_point = [pygame.math.Vector2(p).rotate(self.heading.get_angle()) for p in points]

        triangle_points = [(self.get_location().tuple() + p * scale) for p in rotated_point]
        return triangle_points

    def draw(self, screen):
        points=self.rotate_triangle(self.location.tuple(), self.get_size(), self.heading)
        pygame.draw.polygon(screen, red, points,1)