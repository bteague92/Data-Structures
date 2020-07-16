# animals = ["deer", "duck", "bear"]

# """
# O(1)   (Constant)
# """
# def funcOne(animal_list):
#     for _ in range(1000):
#         print(animal_list[0])

# """
# O(n)    (Linear)
# """
# def funcOne(animal_list): # O(n * (1 + 1 + 1 + (100000 * 1))) = O(n * 100003) = O(100003n) = O(n)
#     for i in range(len(animal_list)): #Linear( O(1) )
#         print(animal_list[i]) # O(1)
#         print(animal_list[i]) # O(1)
#         #O(1+1) = O(2)
#         my_number = 0 # 0(1)
#         for _ in range(100000): #O(100000)
#             my_number += 1


# """
# O(n) - Linear Time
# """
# animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat',
#            'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']
# ​
# ​
# def print_animals(animal_list):
#     for i in range(len(animal_list)):
#         print(animal_list[i])
# ​
# ​
# """
# What about this one? What runtime complexity is this one?
# """
# ​
# ​
# def print_animals(animal_list):
#     for i in range(len(animal_list)):
#         print(animal_list[i])
#         my_number = 0
#         for _ in range(100000):
#             my_number += 1
# ​
# ​
# """
# CFU: Slack Thread: Why doesn't the nested for loop make the time complexity O(n^2)?
# """
# ​
# ​
# """
# O(n^2) & O(n^3) - Polynomial Time
# """
# animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat',
#            'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']
# ​
# ​
# # Print a list of all possible animal pairs
# ### O(n2)
# def print_animal_pairs():
#     for animal_1 in animals:#O(n)
#         for animal_2 in animals:#O(n)
#             print(f"{animal_1} - {animal_2}")
# ​
# ​
# # Print a list of all possible animal triples
# ### O(n3)
# def print_animal_triples():
#     for animal_1 in animals: #O(n)
#         for animal_2 in animals:#O(n)
#             for animal_3 in animals: #O(n)
#                 print(f"{animal_1} - {animal_2} - {animal_3}")
# ​
# ​
# # Print a list of all possible animal triples
# def print_animal_triples():
#     for animal in animals:
#         print(animal)
# ​
#     for animal_1 in animals:
#         for animal_2 in animals:
#             for animal_3 in animals:
#                 print(f"{animal_1} - {animal_2} - {animal_3}")
# ​
# ​
# """
# CFU: Slack Thread
# What's the time complexity to print all animal quintuples? What about "ten"tuples?
# """
# ​
# ​
# """
# O(log n) - Logarithmic Time
# """
# animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat',
#            'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']
# ​
# ​
# # free all the animals, half at a time
# # (remove them from the array)
# def free_animals(animal_list):
#     while len(animal_list) > 0:
#         animal_list = animal_list[0: len(animal_list) // 2]
# ​
# # We are reducing by half at each step
# # This is the inverse of doubling at each step O(2^n) - Exponential Time
# ​
# ​
# """
# CFU: Slack Thread
# What's the worst the number of steps can get for a O(log n) time complexity
# algorithm with an input size of 10 million?
# """

# class Node:
#     """
#     Data:
#     Stores two pieces of data:
#     1. The Value
#     2. The Next Node
# ​
#     Methods/Behavior/Operations:
#     1. Get value
#     2. Set value
#     3. Get next
#     4. Set next
#     """
#     def __init__(self, value=None, next_node=None):
#         # the value at this linked list node
#         self.value = value
#         # reference to the next node in the list
#         self.next_node = next_node
# ​
#     def get_value(self):
#         return self.value
# ​
#     def get_next(self):
#         return self.next_node
# ​
#     def set_next(self, new_next):
#         # set this node's next_node reference to the passed in node
#         self.next_node = new_next
# ​
# ​
# class LinkedList:
#     """
#     Data:
#     1. A reference to the head Node
#     2. A reference to the tail Node
# ​
#     Behavior/Methods:
#     1. Add To Tail
#     2. Prepend (Add a new node and point that Node's next_node at the old Head; update Head pointer)
#     3. Remove Head
#     4. Remove Tail
#     5. Contains?
#     6. Get Maximum?
#     """
#     def __init__(self):
#         # reference to the head of the list
#         self.head = None
#         # reference to the tail of the list
#         self.tail = None
# ​
#     def add_to_tail(self, value):
#         # wrap the input value in a node
#         new_node = Node(value, None)
#         # check if there is no head (i.e., the list is empty)
#         if not self.head:
#             # if the list is initially empty, set both head and tail to the new node
#             self.head = new_node
#             self.tail = new_node
#         # we have a non-empty list, add the new node to the tail
#         else:
#             # set the current tail's next reference to our new node
#             self.tail.set_next(new_node)
#             # set the list's tail reference to the new node
#             self.tail = new_node
# ​
#     def remove_head(self):
#         # return None if there is no head (i.e. the list is empty)
#         if not self.head:
#             return None
#         # if head has no next, then we have a single element in our list
#         if not self.head.get_next():
#             # get a reference to the head
#             head = self.head
#             # delete the list's head reference
#             self.head = None
#             # also make sure the tail reference doesn't refer to anything
#             self.tail = None
#             # return the value
#             return head.get_value()
#         # otherwise we have more than one element in our list
#         value = self.head.get_value()
#         # set the head reference to the current head's next node in the list
#         self.head = self.head.get_next()
#         return value
# ​
#     def remove_tail(self):
#         if not self.head:
#             return None

#         if self.head is self.tail:
#             value = self.head.get_value()
#             self.head = None
#             self.tail = None
#             return value

#         current = self.head
# ​
#         while current.get_next() is not self.tail:
#             current = current.get_next()
# ​
#         value = self.tail.get_value()
#         self.tail = current
#         return value
# ​
#     def contains(self, value):
#         if not self.head:
#             return False
# ​
#         # Recursive solution
#         # def search(node):
#         #   if node.get_value() == value:
#         #     return True
#         #   if not node.get_next():
#         #     return False
#         #   return search(node.get_next())
#         # return search(self.head)

#         # get a reference to the node we're currently at; update this as we traverse the list
#         current = self.head
#         # check to see if we're at a valid node
#         while current:
#             # return True if the current value we're looking at matches our target value
#             if current.get_value() == value:
#                 return True
#             # update our current node to the current node's next node
#             current = current.get_next()
#         # if we've gotten here, then the target node isn't in our list
#         return False
# ​
#     def get_max(self):
#         if not self.head:
#             return None
#         # reference to the largest value we've seen so far
#         max_value = self.head.get_value()
#         # reference to our current node as we traverse the list
#         current = self.head.get_next()
#         # check to see if we're still at a valid list node
#         while current:
#             # check to see if the current value is greater than the max_value
#             if current.get_value() > max_value:
#                 # if so, update our max_value variable
#                 max_value = current.get_value()
#             # update the current node to the next node in the list
#             current = current.get_next()
#         return max_value
