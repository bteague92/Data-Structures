"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
import sys
sys.path.append('stack')
from stack import Stack
sys.path.append('queue')
from queue import Queue


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        
        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        elif value >= self.value: 
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def contains(self, target):

        if self.value == target:
            return True
        elif target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        elif target > self.value:
            if not self.right:
                return False
            else: 
                return self.right.contains(target)

    def get_max(self):
         
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass      
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal    
    def dft_print(self, node):
        pass
        
        

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass