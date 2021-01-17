class Location:
    loc = (0, 0)

    def __init__(self):
        self.loc = None

    def __init__(self, loc):
        self.loc = loc

    def get_loc(self):
        return self.loc

    def set_loc(self, loc):
        self.loc = loc
