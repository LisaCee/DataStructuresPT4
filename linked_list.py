class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printIt(self):
        curr_node = self.head
        print('---HEAD---')
        while curr_node is not None:
            print(curr_node.value)
            curr_node = curr_node.next
        print('------')

    def add_to_front(self, value):
        old_head = self.head
        new_head = Node(value)
        new_head.next = old_head
        self.head = new_head


def get_middle(linked_list):
    # return middle value of list
    slow_pointer = linked_list.head
    fast_pointer = linked_list.head

    while fast_pointer is not None:
        fast_pointer = fast_pointer.next
        if fast_pointer is not None:
            fast_pointer = fast_pointer.next
            slow_pointer = slow_pointer.next
    return slow_pointer.value


def reverse_list(linked_list):
    curr = linked_list.head
    new = curr.next
    # new tail
    curr.next = None

    while new is not None:
        prev = curr
        curr = new
        new = curr.next
        curr.next = prev
        linked_list.head = curr


ll = LinkedList()
ll.add_to_front(1)
ll.add_to_front(2)
ll.add_to_front(3)
ll.add_to_front(4)
ll.printIt()

print(reverse_list(ll))
ll.printIt()
