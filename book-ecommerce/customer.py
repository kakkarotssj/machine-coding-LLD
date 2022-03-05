from book import BookManager
from order import OrderManager


class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def search_books(self, filters: dict):
        """
        :param filters: {'name': 'something', 'author': 'something'}
        :return: list of all books found
        """

        books = BookManager.search_books(filters)
        return books

    def place_order(self, order_data: dict):
        """
        :param order_data: {'name': quantity}
        :return:
        """

        is_present, short_inventory = self._validate_inventory_present(order_data)
        if not is_present:
            raise Exception(f'Inventory not present for these items: {short_inventory}')

        for book_name, order_quantity in order_data.items():
            BookManager.reduce_inventory(book_name, order_quantity)

        order = OrderManager.create_order(order_data)
        self.orders.append(order)

    @staticmethod
    def cancel_order(order_id):
        order_data = OrderManager.cancel_order(order_id)
        for book_name, order_quantity in order_data.items():
            BookManager.increase_inventory(book_name, order_quantity)

    def view_history(self):
        return [order.to_dict() for order in self.orders]

    @staticmethod
    def _validate_inventory_present(order_data):
        is_present, short_inventory = True, {}
        for book_name, order_quantity in order_data.items():
            _is_present, current_inventory = BookManager.check_inventory(book_name, order_quantity)
            if _is_present:
                continue

            is_present = False
            short_inventory[book_name] = current_inventory

        return is_present, short_inventory
