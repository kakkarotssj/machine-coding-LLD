from constants import SystemConstants
from payment.mock_payment import MockPayment
from product import Product
from slot import Slot


class VendingMachine:
    def __init__(self):
        self.slots = [Slot() for _ in range(SystemConstants.SLOTS_COUNT.value)]
        self.payment_gateway = MockPayment()

    def _check_inventory_exists(self, product_name, requested_quantity) -> (bool, float):
        actual_quantity, total_price = 0, 0
        product_price = 0
        for slot in self.slots:
            if slot.get_product() and slot.get_product().get_name() == product_name:
                actual_quantity += slot.get_quantity()
                if product_price == 0:
                    product_price = slot.get_product().get_price()

        return actual_quantity >= requested_quantity, requested_quantity*product_price

    def get_inventory(self) -> list:
        data = []
        for slot in self.slots:
            inventory = {
                'name': None,
                'price': None,
                'quantity': 0
            }
            if not slot.get_product():
                data.append(inventory)
                continue

            data.append({
                'name': slot.get_product().get_name(),
                'price': slot.get_product().get_price(),
                'quantity': slot.get_quantity(),
            })

        return data

    def select_products(self, products: list):
        """
        :param products: [{'name': product_name, 'quantity': quantity}]
        :return: total amount
        """

        total_price = 0
        for product in products:
            is_available, price = self._check_inventory_exists(product['product_name'], product['quantity'])
            if not is_available:
                raise Exception(f'{product["product_name"]} does not have {product["quantity"]} in the system')
            total_price += price

        return total_price

    def buy_products(self, products: list):
        """
        Assuming this is called only after select_products is called
        """

        total_price = 0
        for product in products:
            _, price = self._check_inventory_exists(product['product_name'], product['quantity'])
            total_price += price

        if self.payment_gateway.make_payment(total_price):
            self._dispatch_products(products)
            return 'Success'

        return 'Failed'

    def _dispatch_products(self, products: list):
        product_name_to_quantity_map = {product['product_name']: product['quantity'] for product in products}

        for slot in self.slots:
            if slot.get_product() and slot.get_product().get_name() in product_name_to_quantity_map:
                actual_quantity, requested_quantity = slot.get_quantity(), product_name_to_quantity_map[slot.get_product().get_name()]
                new_quantity = 0
                if actual_quantity < requested_quantity:
                    product_name_to_quantity_map[slot.get_product().get_name()] = requested_quantity-actual_quantity
                    slot.product = None
                else:
                    product_name_to_quantity_map[slot.get_product().get_name()] = 0
                    new_quantity = actual_quantity-requested_quantity
                slot.set_quantity(new_quantity)

        return

    def _add_inventory_validate(self, product_name, product_data) -> bool:
        slot_sequence = product_data['slot_sequence']
        if slot_sequence > len(self.slots):
            return False

        for slot in self.slots:
            if slot.sequence == slot_sequence:
                if slot.get_product() and slot.get_product().get_name() != product_name:
                    return False
                else:
                    empty_slots = SystemConstants.DEPTH.value - slot.get_quantity()
                    if empty_slots < product_data['quantity']:
                        return False

        return True

    def add_inventory(self, products: list):
        """
        :param products: [{"product_name": "biscuit1", "quantity": 2, "slot_sequence": 1, "price": 10}]
        """

        invalid_requests = []
        for product_data in products:
            product_name = product_data['product_name']
            if not self._add_inventory_validate(product_name, product_data):
                invalid_requests.append(product_name)

        if invalid_requests:
            raise Exception(f'Failed to validate request for add inventory for these products {invalid_requests}')

        for product_data in products:
            for slot in self.slots:
                if slot.sequence == product_data['slot_sequence']:
                    if not slot.get_product():
                        slot.set_product(Product(product_data['product_name'], product_data['price']))
                        slot.set_quantity(product_data['quantity'])
                    else:
                        slot.set_quantity(slot.get_quantity()+product_data['quantity'])

        return

    def _remove_inventory_validate(self, product_name, product_data):
        items_present = 0
        for slot in self.slots:
            if slot.get_product() and slot.get_product() == product_name:
                items_present += slot.get_quantity()

        return items_present >= product_data['quantity']

    def remove_inventory(self, products: list):
        """
        :param products: [{"product_name": "biscuit1", "quantity": 2}]
        """

        invalid_requests = []
        for product_data in products:
            product_name = product_data['product_name']
            if not self._remove_inventory_validate(product_name, product_data):
                invalid_requests.append(product_name)

        if invalid_requests:
            raise Exception(f'Failed to validate request for remove inventory for these products {invalid_requests}')

        for product_data in products:
            product_name = product_data['name']
            items_to_remove = product_data['quantity']
            for slot in self.slots:
                if items_to_remove < 0:
                    break
                if slot.get_product() and slot.get_product().get_name() == product_name:
                    new_quantity = 0
                    if items_to_remove < slot.get_quantity():
                        new_quantity = slot.get_quantity() - items_to_remove
                        items_to_remove = 0
                    else:
                        items_to_remove -= slot.get_quantity()
                    slot.set_quantity(new_quantity)

        return
