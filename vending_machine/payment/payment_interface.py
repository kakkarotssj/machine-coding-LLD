from abc import ABC, abstractmethod


class PaymentInterface(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass
