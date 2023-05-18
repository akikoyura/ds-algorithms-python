class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.pop()


def equal_checker(equation):
    # TODO: Intiate stack object
    stack = Stack()

    for char in equation:
        if char == "(":
            stack.push(char)
        elif char == ")":
            if stack.pop() is None:
                return False

    if stack.size() == 0:
        return True
    else:
        return False
