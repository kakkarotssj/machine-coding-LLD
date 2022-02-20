from abc import ABC, abstractmethod


class StorageInterface(ABC):
    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def put(self, key, value):
        pass

    @abstractmethod
    def delete(self, key):
        pass

    @abstractmethod
    def search(self, attr_key, attr_value):
        pass

    @abstractmethod
    def keys(self):
        pass
