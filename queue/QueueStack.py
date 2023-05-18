class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()


class Queue:
    def __init__(self):
        self.in_storage = Stack()
        self.out_storage = Stack()

    def size(self):
        return self.in_storage.size() + self.out_storage.size()

    def enqueue(self, item):
        self.in_storage.push(item)

    def dequeue(self):
        if not self.out_storage.items:
            while self.in_storage.items:
                self.out_storage.push(self.in_storage.pop())
        return self.out_storage.pop()
