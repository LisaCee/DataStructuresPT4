"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.value)

    # Commented out for refactor

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    # def __str__(self):
    #     # if self.head is None and self.tail is None:
    #     #     return 'empty list'
    #     curr_node = self.head
    #     output = ''
    #     output += str(curr_node) + ' <-> '
    #     while curr_node.next is not None:
    #         curr_node = curr_node.next
    #         output += str(curr_node) + ' <-> '
    #     return output

    def printIt(self):
        curr_node = self.head
        if not self.head:
            print('--None--')
        else:
            print('---HEAD---')
            while curr_node is not None:
                print(curr_node.value)
                curr_node = curr_node.next
            print('------')

    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            # case 1: empty list
            self.head = new_node
            self.tail = new_node
        else:
            # case 2: not empty list
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        if self.head is None:
            self.tail = None
            return
        else:
            value = self.tail.value
            self.delete(self.tail)
            return value
            # lecture solution
            # removed_head = self.head
            # new_head = removed_head.next
            # self.head = new_head
            # removed_head.next = None
            # self.head.prev = None
            # self.length -= 1
            # if self.head is None:
            #     self.tail = None
            # # optional step to fully remove node from memory
            # val = removed_head.value
            # del removed_head
            # return val
    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        if not self.tail:
            return
        else:
            value = self.tail.value
            self.delete(self.tail)
            return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        if node is self.head:
            return
        value = node.value
        self.delete(node)
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if self.head is None and self.tail is None:
            return
        if node is self.tail:
            return
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        if not self.head and not self.tail:
            return
        # if head == tail?
        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
        # if node is head?
        elif self.head == node:
            self.head = node.next
            self.length -= 1
            node.delete()
        # if node is tail?
        elif self.tail == node:
            self.tail = node.prev
            self.length -= 1
            node.delete()
        else:
            self.length -= 1
            node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        if not self.head and not self.tail:
            return None
        max_val = self.head
        curr_node = self.head
        while curr_node is not None:
            if curr_node.value > max_val.value:
                max_val = curr_node
            curr_node = curr_node.next
        return max_val.value


# dll = DoublyLinkedList()
# dll.add_to_head(3)
# dll.add_to_head(4)
# dll.printIt()
