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

    def in_order_print(self, node):
        if node:
            node.in_order_print(node.left)
            print(node.value)
            node.in_order_print(node.right)        

    def bft_print(self, node):
        breadth_queue = []
        breadth_queue.append(node) 
        output_for_tests = ""
        while breadth_queue != []:
            node = breadth_queue.pop(0)
            print(node.value)
            if node.left:
                breadth_queue.append(node.left)
            if node.right:
                breadth_queue.append(node.right)
   
    def dft_print(self, node):
        depth_stack = []
        depth_stack.append(node) 

        while depth_stack != []:
            node = depth_stack.pop(-1)
            print(node.value)
            if node.left:
                depth_stack.append(node.left)
            if node.right:
                depth_stack.append(node.right)
        
        

    # STRETCH Goals -------------------------
    # Note: Research may be required

    def pre_order_dft(self, node):
        depth_stack = []
        depth_stack.append(node) 

        while depth_stack != []:
            node = depth_stack.pop(-1)
            print(node.value)
            if node.right:
                depth_stack.append(node.right)
            if node.left:
                depth_stack.append(node.left)

    def post_order_dft(self, node):
        depth_stack = []
        depth_stack.append(node) 

        while depth_stack != []:
            node = depth_stack.pop(-1)
            if node.left:
                self.post_order_dft(node.left)
            if node.right:
                self.post_order_dft(node.right)
            print(node.value)