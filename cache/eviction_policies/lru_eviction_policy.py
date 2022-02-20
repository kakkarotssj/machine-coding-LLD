from eviction_policies.eviction_policy_interface import EvictionPolicyInterface


class LRUEvictionPolicy(EvictionPolicyInterface):
    storage = None

    def key_accessed(self, key):
        node = self.storage.key_to_node_mapping[key]
        self.storage.dll.detach_node(node)
        self.storage.dll.attach_node_at_start(node)

    def evict(self):
        key = self.storage.dll.delete_node_from_end()
        self.storage.key_to_node_mapping.pop(key)
