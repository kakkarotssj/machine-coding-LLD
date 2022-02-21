from random import randint
from payment.payment_interface import PaymentInterface


class MockPayment(PaymentInterface):
    def make_payment(self, amount):
        return randint(0, 1) == 0
