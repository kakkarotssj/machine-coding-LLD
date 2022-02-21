from product import Product


class Slot:
    sequence = 1

    def __init__(self):
        self.quantity = 0
        self.product = None
        self.sequence = Slot.sequence
        self.increment_sequence()

    def get_quantity(self):
        return self.quantity

    def get_product(self):
        return self.product

    def set_quantity(self, quantity: int):
        self.quantity = quantity

    def set_product(self, product: Product):
        self.product = product

    @classmethod
    def increment_sequence(cls):
        cls.sequence += 1
