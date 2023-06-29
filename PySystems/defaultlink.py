from abstractlink import AbstractLink

# deafultlink's are for real actual display
# "If it's more intuitive it's probably the right answer" - My classmate Carrie on why they
# should be named nubbins or nubs
class DefaultLink(AbstractLink):

    # Nubbins (or nubs) are the points on the outside of the node in which lines should be connected to.
    # Basically, the lines do not connect to the center of a node all of the time, therefore
    # non-center points on the perimeter of the shape shall be used and called nubbins.
    def __init__(self):
        self.start_nubbin
        self.end_nubbin

    def get_shape(self):
        return self.shape

    def set_shape(self, shape):
        self.shape = shape


