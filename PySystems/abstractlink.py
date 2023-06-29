class AbstractLink:
    # Same idea as abstractnode, not for display purposes.
    # If anyone has architecture tips, please send them
    # My way.
    def __init__(self):
        self.uid
        self.x1_pos
        self.y1_pos
        self.x2_pos
        self.y2_pos

    def get_uid(self):
        return self.uid

    def set_uid(self, val):
        self.uid = val

    def get_x1(self):
        return self.x1_pos

    def set_x1(self, val):
        self.x1_pos = val

    def get_x2(self):
        return self.x2_pos

    def set_x2(self, val):
        self.x2_pos = val

    def get_y1(self):
        return self.y1_pos

    def set_y1(self, val):
        self.y1_pos = val

    def get_y2(self):
        return self.y2_pos

    def set_y2(self, val):
        self.y2_pos = val
