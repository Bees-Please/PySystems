class AbstractNode:
    # Abstract node, not for display, pretty much just for being here
    # And maintaining an extendable set of standard attributes.
    # Not sure why I went with this structure, but let's roll with it
    # Until someone tells me I'm stupid or makes a pull request.
    def __init__(self):
        self.uid = None
        self.x_pos = None
        self.y_pos = None
        self.size

    def get_uid(self):
        return self.uid

    def set_uid(self, val):
        self.uid = val

    def get_x(self):
        return self.x_pos

    def set_x(self, val):
        self.x_pos = val

    def get_y(self):
        return self.y_pos

    def set_y(self, val):
        self.y_pos = val

    def get_size(self):
        return self.size

    def set_size(self, val):
        self.size = val

    def bottom_left(self):
        return self.x_pos - self.size, self.y_pos - self.size

    def top_right(self):
        return self.x_pos + self.size, self.y_pos + self.size