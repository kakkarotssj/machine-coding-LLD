"""
Design a cache --> an in-memory key-value store

key --> string
value --> object/map
example --> "sde_bootcamp": { "title": "SDE-Bootcamp", "price": 30000.00, "enrolled": false, "estimated_time": 30 }

* functions to support
1). get(string key) --> null if not present and map/object if present
2). search(String attributeKey, String attributeValue) --> returns a list of keys that have the given attribute key, value pair.
3). put(String key, List<Pair<String, String>> listOfAttributePairs) --> Adds the key and the attributes to the key-value store. If the key already exists then the value is replaced.
4). delete(String key) --> Deletes the key, value pair from the store
5). keys() => Return a list of all the keys

* The value object should override the toString method to print the object as a comma-separated list of key-value pairs for the attributes.
* The data type of an attribute should get fixed after its first occurrence. Example: Once we encounter an attribute age with an integer value then any entry with an age attribute having a non-integer value should result in an exception.

* Nothing should be printed inside any of these methods. All scanning and printing should happen in the Driver/Main class only. Exception Handling should also happen in the Driver/Main class.


SAMPLE INPUT:
put sde_bootcamp title SDE-Bootcamp price 30000.00 enrolled false estimated_time 30
get sde_bootcamp
keys
put sde_kickstart title SDE-Kickstart price 4000 enrolled true estimated_time 8
get sde_kickstart
keys
put sde_kickstart title SDE-Kickstart price 4000.00 enrolled true estimated_time 8
get sde_kickstart
keys
delete sde_bootcamp
get sde_bootcamp
keys
put sde_bootcamp title SDE-Bootcamp price 30000.00 enrolled true estimated_time 30
search price 30000.00
search enrolled true



IMPLEMENTATION LOGIC:
1). Implement this cache, such that new eviction policies can be injected later.
2). Implement this storage, such that any storage type can be implemented and used
3). We will define two interface classes of storage and evictionpolicy such that they can be implemented



"""


from enum import Enum

from cache import Cache


class CommandInputs(Enum):
    EXIT = 'exit'
    PUT_DATA = 'put'
    GET_KEY_DATA = 'get'
    LIST_ALL_KEYS = 'keys'
    SEARCH_ATTRIBUTES = 'search'
    DELETE_KEY = 'delete'


def driver():
    while True:
        command = input()
        if command == CommandInputs.EXIT.value:
            break

        try:
            if command[:3] == CommandInputs.PUT_DATA.value:
                try:
                    inputs = command[4:].split(' ')
                    key, value = inputs[0], inputs[1:]
                    Cache.put_data(key, value)
                except Exception as exc:
                    print(f'Invalid command input. Please see documentation. {exc}')
            elif command[:3] == CommandInputs.GET_KEY_DATA.value:
                try:
                    inputs = command[4:].split(' ')
                    key = inputs[0]
                    print(Cache.get_data(key))
                except Exception as exc:
                    print(f'Invalid command input. Please see documentation {exc}')
            elif command[:4] == CommandInputs.LIST_ALL_KEYS.value:
                print(Cache.list_all_keys())
            elif command[:6] == CommandInputs.SEARCH_ATTRIBUTES.value:
                try:
                    inputs = command[7:].split(' ')
                    key, value = inputs[0], inputs[1]
                    print(Cache.search_attributes(key, value))
                except Exception as exc:
                    print(f'Invalid command input. Please see documentation {exc}')
            elif command[:6] == CommandInputs.DELETE_KEY.value:
                try:
                    key = command[7:].split(' ')[0]
                    Cache.delete(key)
                except Exception as exc:
                    print(f'Invalid command input. Please see documentation {exc}')

        except Exception as exc:
            print(exc)


driver()
