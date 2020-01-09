from doubly_linked_list import DoublyLinkedList, ListNode
import sys
sys.path.append('../doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList(self)
        self.size = 0
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = ListNode(value)
        self.size += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            return None
        else:
            dequeued_node = self.head
            self.head = self.head.next
            self.size -= 1
        return dequeued_node.value

    def len(self):
        return self.size
