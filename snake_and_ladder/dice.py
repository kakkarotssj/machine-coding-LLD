import random


class Dice:
    def __init__(self, faces=6):
        self.faces = faces

    def roll_dice(self):
        return random.randint(1, self.faces)
