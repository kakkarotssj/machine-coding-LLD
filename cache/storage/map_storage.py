from storage.storage_interface import StorageInterface


class DoublePointerNode:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.next, self.prev = None, None


class DoublyLinkedList:
    capacity, size = 0, 0
    head, tail = None, None

    def increment_size_by_one(self):
        self.size += 1

    def decrement_size_by_one(self):
        self.size -= 1

    def add_node(self, key, value):
        node = DoublePointerNode(key, value)
        if not self.head:
            self.head, self.tail = node, node

        elif self.head == self.tail:
            self.head = node
            self.head.next = self.tail
            self.tail.prev = self.head

        else:
            self.attach_node_at_start(node)

        self.increment_size_by_one()
        return node

    def delete_node_from_end(self):
        temp = self.tail
        self.tail = temp.prev
        key = temp.key
        del temp
        self.decrement_size_by_one()
        return key

    def delete_node(self, node):
        if node == self.head:
            self.head = self.head.next
        elif node == self.tail:
            self.tail = self.tail.prev
        else:
            node.prev.next, node.next.prev = node.next, node.prev

        del node
        self.decrement_size_by_one()

    def attach_node_at_start(self, node):
        temp = self.head
        self.head = node
        self.head.next = temp
        if temp:
            temp.prev = self.head
            del temp

    def detach_node(self, node):
        if node == self.head:
            self.head = self.head.next
        elif node == self.tail:
            self.tail = self.tail.prev
        else:
            node.prev.next, node.next.prev = node.next, node.prev


class MapStorage(StorageInterface):
    key_to_node_mapping = {}

    def __init__(self, capacity):
        self.dll = DoublyLinkedList()
        self.dll.capacity = capacity

    def get(self, key):
        node = self.key_to_node_mapping.get(key)
        if node:
            return node.value

    def put(self, key, value):
        node = self.key_to_node_mapping.get(key)
        if not node:
            value = self._transform_value_to_map(value)
            node = self.dll.add_node(key, value)
            self.key_to_node_mapping[key] = node

    def delete(self, key):
        node = self.key_to_node_mapping.pop(key)
        if not node:
            raise Exception('Key does not exists. Failed to delete')

        self.dll.delete_node(node)

    def search(self, attr_key, attr_value):
        keys = []
        for key, node in self.key_to_node_mapping.items():
            for _key, _value in node.value.items():
                if _key == attr_key and _value == attr_value:
                    keys.append(key)
                    break

        return keys

    def keys(self):
        return list(self.key_to_node_mapping.keys())

    @staticmethod
    def _transform_value_to_map(value):
        _value = {}
        for i in range(0, len(value), 2):
            _value[value[i]] = value[i+1]

        return _value
