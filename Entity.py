from Vector import Vector
import math
import pygame

red = (255, 0, 0)


class Entity:
    kind = None
    location = None
    shape = None
    size = None
    speed = None
    heading = None
    max_speed = None
    max_force = None
    mass = None

    def __init__(self):
        self.kind = None
        self.location = None
        self.shape = None
        self.size = None
        self.speed = None
        self.heading = None
        self.max_speed = None
        self.max_force = None
        self.mass = None

    def __init__(self, kind, location, speed, heading, size, shape, max_speed, max_force, mass):
        self.kind = kind
        self.location = Vector(location)
        self.shape = shape
        self.size = size
        self.speed = 4*1/size
        self.heading = Vector((math.cos(math.radians(heading)), math.sin(math.radians(heading)))).norm()
        self.max_speed = max_speed
        self.max_force = max_force
        self.mass = size*size

    def get_kind(self):
        return self.kind

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

    def set_kind(self, t):
        self.kind = t

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
        turning_vector = desired - self.heading
        if turning_vector.get_length() * self.mass < self.max_force:

            return desired
        else:

            return (turning_vector.norm()/self.mass) + self.heading

    def update_new_pos(self, target):
        desired = target - self.location
        desired = self.get_new_heading(desired)
        self.set_heading(desired.norm())
        self.set_location(self.location + self.heading*self.speed)

    def rotate_triangle(self, scale):
        points = [(-0.5, -0.866), (-0.5, 0.866), (2.0, 0.0)]
        rotated_point = [pygame.math.Vector2(p).rotate(self.heading.get_angle()) for p in points]

        triangle_points = [(self.get_location().tuple() + p * scale) for p in rotated_point]

        '''ox, oy = self.get_location().tuple()
        px, py = 

        qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
        qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
        '''

        return triangle_points

    def draw(self, screen):
        points = self.rotate_triangle(self.get_size())
        return pygame.draw.polygon(screen, red, points, 1)
