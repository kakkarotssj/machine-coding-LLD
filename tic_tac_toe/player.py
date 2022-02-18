class Player:
    def __init__(self, name, shape):
        self.name = name
        self.shape = shape

    def get_name(self):
        return self.name

    def get_shape(self):
        return self.shape.value
