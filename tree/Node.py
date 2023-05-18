class Node(object):
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.value = val

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def has_right_child(self):
        return self.right is not None

    def has_left_child(self):
        return self.left is not None

    # define __repr__ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"
