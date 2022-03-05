"""
Our end-customer should be able to perform the following operations:
    Browse books - check price, title etc	.
    Place an order for the book - if present in inventory
    Check their order history and status
    Cancel their order

Think about the following points:
Search criteria for finding relevant books
Use appropriate data structures, feel free to use in-memory DB if you are comfortable
Exception handling and edge cases


1. A user should be able to search books. Zero or some filters on the book. OR of all filters.
2. A user should be able to view the inventory against every book, he/she searching
3. A user should be able to place an order with x inventory on y book. Assuming, if any of the inventory fails, fail whole order
4. A user should be able to view history of orders

Customer:
- name | unique
- orders | list

- search_books(filters: dict) --> list of books
- place_order(order_data: dict) --> true/false
- cancel_order(id) --> true/false
- view_history()

order_data --> hashmap which will store against every book_name --> order count


Book:
- name | unique
- author
- price
- publisher
- version

- to_dict()

BookManager:
- book_inventory | map | key -> book_name value --> map {'book': book_object, 'inventory': x}

- check_inventory()
- search_books()
- reduce_inventory()
- increase_inventory()


Order:
- id | system generated
- info
- status | Status

- set_status()
- to_dict()


OrderManager:
- orders | map

- create_order(order_data)
- cancel_order(id)


Status(Enum):
- PLACED
- CONFIRMED
- IN TRANSIT
- DELIVERED
- CANCELLED
"""


from customer import Customer


def create_demo_customer(name):
    return Customer(name)


def get_book_search_filters():
    return {
        'name': 'book1',
    }


def get_place_order_short_inventory():
    return {'book1': 2, 'book3': 10}


def get_place_order_correct_inventory():
    return {'book1': 2, 'book2': 1}


def main():
    customer = create_demo_customer('Sid')
    print(customer.search_books(get_book_search_filters()))

    try:
        customer.place_order(get_place_order_short_inventory())
    except Exception as exc:
        print(exc)

    try:
        customer.place_order(get_place_order_correct_inventory())
    except Exception as exc:
        print(exc)

    print(customer.view_history())


main()
