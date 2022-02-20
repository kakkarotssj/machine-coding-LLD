from abc import ABC, abstractmethod


class EvictionPolicyInterface(ABC):
    @abstractmethod
    def key_accessed(self, key):
        pass

    @abstractmethod
    def evict(self):
        pass
