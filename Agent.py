from Entity import Entity


class Agent:
    health = None
    entity = None

    def __init__(self):
        self.entity = Entity()
        self.health = 0

    def __int__(self, location, speed, heading, size, shape, health):
        self.entity = Entity("Agent", location, speed, heading, size, shape)
        self.health = health

    def do_sim(self, area):
        self.do_move(area)

    def do_move(self, area):
        # empty
        return

    def do_eval(self, area):
        # empty
        return

    def set_health(self, health):
        self.health = health

    def set_speed(self, speed):
        self.entity.set_speed(speed)

    def set_location(self, loc):
        self.entity.set_location(loc)

    def set_heading(self, heading):
        self.entity.set_heading(heading)

    def set_size(self, size):
        self.entity.size(size)

    def get_health(self, health):
        return self.health

    def get_speed(self, speed):
        return self.speed

    def get_location(self, loc):
        return self.location

    def get_heading(self, heading):
        return self.heading

    def get_size(self, size):
        return self.size
