from uuid import uuid4

from constants import OrderStatuses


class Order:
    def __init__(self, info):
        self.id = str(uuid4())
        self.info = info
        self.status = OrderStatuses.PLACED.value

    def set_status(self, status):
        self.status = status

    def to_dict(self):
        return {
            'id': self.id,
            'info': self.info,
            'status': self.status
        }


class OrderManager:
    orders = {}

    @classmethod
    def create_order(cls, order_data):
        order = Order(order_data)
        cls.orders[order.id] = order
        return order

    @classmethod
    def cancel_order(cls, id):
        order = cls.orders.get(id)
        if not order:
            raise Exception(f'Order not found for id: {id}')

        order.set_status(OrderStatuses.CANCELLED.value)
        return order.info
