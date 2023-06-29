from abstractnode import AbstractNode

# Default node for actual display
class DefaultNode(AbstractNode):

    def __init__(self):
        self.shape = None

    def get_shape(self):
        return self.shape

    def set_shape(self, shape):
        self.shape = shape

