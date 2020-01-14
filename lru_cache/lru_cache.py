from doubly_linked_list import DoublyLinkedList, ListNode
import sys
sys.path.append('../doubly_linked_list')


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.storage = {}
        # fast lookup
        self.limit = limit
        self.length = 0
        self.order = DoublyLinkedList()
        # fast removal

        # most recent at tail
        # least recent at head

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if key not in self.storage:
            return None
        # if no key in storage, return None
        # read from storage
        node = self.storage[key]
        # move key to tail
        self.order.move_to_end(node)
        return node.value[1]

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # key does exist
            # move existing node to tail
        if key in self.storage:
            node = self.storage[key]
            # update value in storage
            node.value = (key, value)
            # self.storage[key] = value
            self.order.move_to_end(node)
            return

        # key does not exist
            # store key: value in storage
            # create node with key
            # add node to tail of order (DLL)

        self.order.add_to_tail((key, value))
        self.storage[key] = self.order.tail
        self.length += 1

        # check if limit exceeded
        # remove lru key:value
        # remove current head from order
        if self.length > self.limit:
            del self.storage[self.order.head.value[0]]
            self.order.remove_from_head()
            self.length -= 1
