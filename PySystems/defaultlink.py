from abstractlink import AbstractLink


class DefaultLink(AbstractLink):

    def __init__(self):
        self.start_nodule
        self.end_nodule

    def get_shape(self):
        return self.shape

    def set_shape(self, shape):
        self.shape = shape

