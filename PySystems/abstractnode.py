class AbstractNode:

    def __init__(self):
        self.uid = None
        self.x_pos = None
        self.y_pos = None

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
