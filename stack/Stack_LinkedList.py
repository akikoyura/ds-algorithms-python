class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.num_elements += 1

    def is_empty(self):
        return self.num_elements == 0

    def size(self):
        return self.num_elements

    def pop(self):
        if self.is_empty():
            return

        node = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return node

