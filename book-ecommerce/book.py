class Book:
    def __init__(self, name, author, price, publisher, version):
        self.name = name
        self.author = author
        self.price = price
        self.publisher = publisher
        self.version = version

    def to_dict(self):
        return {
            'name': self.name,
            'author': self.author,
            'price': self.price
        }

    # getter setter methods here


class BookManager:
    book_inventory = {
        'book1': {'book': Book('book1', 'Sid', 250.5, 'publisher1', '10'), 'inventory': 4},
        'book2': {'book': Book('book2', 'Sharma', 145, 'publisher2', '11'), 'inventory': 2},
        'book3': {'book': Book('book3', 'random', 120, 'publisher1', '15'), 'inventory': 0},
    }

    @classmethod
    def check_inventory(cls, name, quantity):
        if quantity > cls.book_inventory[name]['inventory']:
            return False, cls.book_inventory[name]['inventory']

        return True, cls.book_inventory[name]['inventory']

    @classmethod
    def search_books(cls, filters: dict):
        # filters = BookManager._clean_filters(filters)
        response = []

        for book in cls.book_inventory.values():
            book_object = book['book']
            for filter_key, filter_value in filters.items():
                if getattr(book_object, filter_key) == filter_value:
                    response.append(book_object.to_dict())
                    break

        return response

    @classmethod
    def reduce_inventory(cls, name, quantity):
        cls.book_inventory[name]['inventory'] -= quantity

    @classmethod
    def increase_inventory(cls, name, quantity):
        cls.book_inventory[name]['inventory'] += quantity

    @staticmethod
    def _clean_filters(filters):
        updated_filters = {}
        for filter_key, filter_value in filters.items():
            if hasattr(Book, filter_key):
                updated_filters[filter_key] = filter_value

        return updated_filters
