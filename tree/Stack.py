# Let's define a stack to help keep track of the tree nodes
class Stack(object):
    def __init__(self):
        self.list = list()

    # add an element to the list
    def push(self, value):
        self.list.append(value)

    # remove the last element from the list
    def pop(self):
        return self.list.pop()

    # get the value of the last element in the list
    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None

    # check if the list empty
    def is_empty(self):
        return len(self.list) == 0

    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack> \n______________________________\n"
            s += "\n______________________________\n".join([str(item) for item in self.list[::-1]])
            s += "\n______________________________\n<bottom of stack>"
            return s
        else:
            return "<stack is empty>"


if __name__ == '__main__':
    # instantiate Stack
    stack = Stack()
    # add elements into the stack
    stack.push("apple")
    stack.push("banana")
    stack.push("cherry")
    stack.push("dates")

    # remove and print the last element (top of the stack)
    print(stack.pop())
    print("\n")
    print(stack)
