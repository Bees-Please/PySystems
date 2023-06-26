from abstractlink import AbstractLink


class DefaultNode(AbstractLink):

    def __init__(self):
        self.start_node
        self.end_node

    def get_shape(self):
        return self.shape

    def set_shape(self, shape):
        self.shape = shape

