from node.Node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

    def prepend(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        return

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def search(self, value):
        current = self.head
        while current.value != value:
            current = current.next
        return current

    def remove(self, value):
        dummy = Node(0)
        dummy.next = self.head
        current = dummy
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            else:
                current = current.next
        self.head = dummy.next
        return self.head

    def insert(self, value, pos):
        if self.head is None or pos == 0:
            self.prepend(value)
            return

        current = self.head
        position = 0
        while current.next:
            if (position + 1) == pos:
                node = Node(value)
                node.next = current.next
                current.next = node
                return
            else:
                current = current.next
            position = position + 1
        else:
            self.append(value)

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])


def reverse(link_list):
    new_list = LinkedList()
    current = link_list.head
    prev = None
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    new_list.head = prev
    return new_list


if __name__ == '__main__':
    llist = LinkedList()
    for value in [4, 2, 5, 1, -3, 0]:
        llist.append(value)

    flipped = reverse(llist)
    is_correct = list(flipped) == list([0, -3, 1, 5, 2, 4]) and list(llist) == list(reverse(flipped))
    print("Pass" if is_correct else "Fail")
