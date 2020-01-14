from dll_stack import Stack
from dll_queue import Queue
# import sys
# sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if new value is less than current node
        if value < self.value:
            # check if current node has a left
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if not self:
            return None
        if self.right:
            return self.right.get_max()
        else:
            return self.value

        # # iterative solution
        # curr_tree_root = self
        # while curr_tree_root.right:
        #     curr_tree_root = curr_tree_root.right
        # return curr_tree_root.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):
        # depth first search
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # go left if you can
        # print current node
        # go right if you can
        if node.left:
            self.in_order_print(node.left)
        if node.right:
            print(node.value)
            self.in_order_print(node.right)
        else:
            print(node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):

         # iterative solution
        # create queue to keep track of nodes
        # place first node on stack
        # while stack isn't empty:
        # dequue top node
        # print node
        # add children to queue
        # remember which children to add first bc that changes output order
        queue = Queue()
        queue.enqueue(node)
        while queue.size > 0:
            current_node = queue.dequeue()
            print(current_node.left)
            if current_node.left:
                queue.enqueue(current_node.left)
            if current_node.right:
                queue.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
        # iterative solution
        # create stack to keep track of nodes
        # place first node on stack
        # while stack isn't empty:
        # pop top node
        # print node
        # add children to stack
        # remember which children to add first bc that changes output order, go r -> l (smaller)
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while stack.size > 0:
            current_node = stack.pop().value
            print(current_node.value)
            if current_node.left:
                stack.push(current_node.left)
            if current_node.right:
                stack.push(current_node.right)
        # recursive solution
        print(self.value)
        # if self.left:
        #     self.left.dft_print(self.left)
        # if self.right:
        #     self.right.dft_print(self.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT

    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


bst = BinarySearchTree(5)
bst.insert(2)
bst.insert(1)
bst.insert(3)
bst.insert(7)
bst.bft_print(bst)
