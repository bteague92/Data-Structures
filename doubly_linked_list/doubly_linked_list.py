"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    def delete(self):
        if self.prev:
            if self.next:
                self.prev.next = self.next
                self.next.prev = self.prev
            else:
                self.prev.next = None
        else:
            if self.next:
                self.next.prev = None
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        if node == None:
            self.length = 0
        else:
            self.length = 1
    def __len__(self):
        return self.length
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value, None)
        self.length += 1
        if self.head:
            head = self.head
            self.head = new_node
            head.prev = self.head
            self.head.next = head
        else:
            self.head = new_node
            self.tail = new_node
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        self.length -= 1
        if self.head:
            if self.head.next:
                value = self.head.value
                self.head = self.head.next
                return value
            else:
                value = self.head.value
                self.head = None
                self.tail = None
                return value
        else:
            return None
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value, None)
        self.length += 1
        if self.head:
            tail = self.tail
            self.tail = new_node
            self.tail.prev = tail
            tail.next = self.tail
        else:
            self.head = new_node
            self.tail = new_node
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        self.length -= 1
        if not self.head:
            return None
        else:
            if self.head is self.tail:
                value = self.head.value
                self.head = None
                self.tail = None
                return value
            else:
                self.tail = self.tail.prev
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return
        else:
            value = node.value
            self.delete(node)
            self.add_to_head(value)
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return
        else:
            value = node.value
            self.delete(node)
            self.add_to_tail(value)
    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        self.length -= 1
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif self.head is node:
            self.head = node.next
            node.delete()
        elif self.tail is node:
            self.tail = node.prev
            node.delete()
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        current = self.head
        max_value = current.value
        while current is not None:
            if current.value > max_value:
                max_value = current.value
            current = current.next

        return max_value