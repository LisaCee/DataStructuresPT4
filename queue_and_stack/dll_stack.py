from doubly_linked_list import DoublyLinkedList, ListNode
import sys
sys.path.append('../doubly_linked_list')


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList(self)
        self.head = None
        self.tail = None

    def push(self, value):
        new_node = ListNode(value)
        self.size += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        if self.tail is None:
            return None
        else:
            popped_node = self.tail
            self.tail = self.tail.prev
            self.size -= 1
        return popped_node.value

    def len(self):
        return self.size
