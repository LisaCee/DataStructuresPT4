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
        self.head = None
        self.tail = None
        self.limit = limit
        self.size = 0
        self.storage = {}
        # fast lookup
        self.cache = DoublyLinkedList()
        # fast removal

    def print(self):
        curr_node = self.head
        print(curr_node)
        while curr_node.next is not None:
            curr_node = curr_node.next
            print(curr_node)

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def maxCapacity(self):
        if self.size == self.limit:
            self.cache.remove_from_tail()
        # self.storage.pop(key)
        self.size -= 1

    # def recentlyAccessed(self, value):
    #     self.prev = self.head
    #     self.next = self.head.next

    #     self.head.next.prev = value
    #     self.head.next = value

    def get(self, key):
        if key in self.storage:
            node = self.storage[key]
            self.cache.delete(node)
            self.cache.add_to_head(node)
            return self.storage[key]
        else:
            return None

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
        self.maxCapacity()
        if key in self.storage:
            # self.storage[key] = value
            if not self.head:
                self.head = ListNode(value)
                # print('HEAD',self.head)
                self.tail = ListNode(value)
        else:
            node = ListNode(value)
            old_head = self.head
            self.head = node
            self.head.next = old_head
        # get to see if key exists in cache
            # update value
            # move to head of ll
        # if key in self.storage:
        # node = self.storage[key]
        self.storage[key] = value
        # print(self.storage)
        self.size += 1
        # self.cache.delete(node)
        # self.cache.add_to_head(node)

        # if doesn't exist, add to cache
        # add to head of ll
        # check limit
        # remove tail if needed


lru = LRUCache(3)
lru.set('key1', 'a')
lru.set('key2', 'b')
lru.set('key3', 'c')
lru.set('item4', 'd')
lru.print()
