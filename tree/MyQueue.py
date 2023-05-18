from collections import deque


class Queue(object):
    def __init__(self):
        self.q = deque()

    def enq(self, value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)

    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n____________________________\n"
            s += "\n____________________________\n".join([str(item) for item in self.q])
            s += "\n____________________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"


if __name__ == '__main__':
    q = Queue()
    q.enq("apple")
    q.enq("banana")
    q.enq("cherry")
    print(q)

    print(q.deq())
    print(q)
