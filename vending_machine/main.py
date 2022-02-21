"""
N slots - 1 dimensional - x | x | x|  y | y

Each slot - K capacity
Product - Name, price

Each slot - Only one type of product
Each product – 1 unit space

"""

from vending_machine import VendingMachine


def driver():
    vm = VendingMachine()

    current_inventory = vm.get_inventory()
    print(current_inventory)

    # negative case, where we try to add inventory more than depth, this will throw error, so handle with try except
    products = [{'product_name': 'biscuit1', 'quantity': 3, 'slot_sequence': 1, 'price': 10}]
    try:
        vm.add_inventory(products)
    except Exception as exc:
        print(f'FAILED: {exc}')

    # positive case
    products = [{'product_name': 'biscuit1', 'quantity': 2, 'slot_sequence': 1, 'price': 10},
                {'product_name': 'biscuit2', 'quantity': 2, 'slot_sequence': 2, 'price': 10}]
    vm.add_inventory(products)

    current_inventory = vm.get_inventory()
    print(current_inventory)

    # select products negative case
    try:
        products = [{'product_name': 'biscuit3', 'quantity': 3}]
        total_price = vm.select_products(products)
    except Exception as exc:
        print(f'FAILED: {exc}')

    # select products positive case
    products = [{'product_name': 'biscuit1', 'quantity': 2}, {'product_name': 'biscuit2', 'quantity': 2}]
    total_price = vm.select_products(products)
    print(total_price)

    # buy products and assumed this is called only on valid data
    products = [{'product_name': 'biscuit1', 'quantity': 1}, {'product_name': 'biscuit2', 'quantity': 1}]
    status = vm.buy_products(products)
    print(status)
    print(vm.get_inventory())


driver()
