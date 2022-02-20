from eviction_policies.lru_eviction_policy import LRUEvictionPolicy
from storage.map_storage import MapStorage


class Cache:

    CAPACITY = 2
    storage = MapStorage(CAPACITY)
    eviction_policy = LRUEvictionPolicy()
    eviction_policy.storage = storage

    @classmethod
    def put_data(cls, key, value):
        if cls.storage.dll.size == cls.storage.dll.capacity:
            cls.eviction_policy.evict()

        cls.storage.put(key, value)
        cls.eviction_policy.key_accessed(key)

    @classmethod
    def get_data(cls, key):
        value = cls.storage.get(key)
        if value:
            cls.eviction_policy.key_accessed(key)
        return value

    @classmethod
    def list_all_keys(cls):
        return cls.storage.keys()

    @classmethod
    def search_attributes(cls, attr_key, attr_value):
        return cls.storage.search(attr_key, attr_value)

    @classmethod
    def delete(cls, key):
        cls.storage.delete(key)
