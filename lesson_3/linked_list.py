from node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        return str(self.head)

    def append(self, data):
        new_node = Node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove_first(self):
        temp = self.head
        self.head = temp.next

    def remove_last(self):
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

    def contains(self, val):
        temp = self.head
        if val == temp.data:
            return True
        while temp is not None:
            temp = temp.next
            if temp.next is None:
                return False
            elif val == temp.data:
                return True

    def reverse_list(self):
        temp = self.head
        next_n = None
        prev_n = None
        while temp is not None:
            next_n = temp.next
            temp.next = prev_n
            prev_n = temp
            temp = next_n
        self.head = prev_n




