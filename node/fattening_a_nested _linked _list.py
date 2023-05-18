class NodeV1:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedListV2:
    def __init__(self, head):
        self.head = head

    def append(self, value):
        if self.head is None:
            self.head = NodeV1(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = NodeV1(value)

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(int(str(node.value)))
            node = node.next
        return out


def merge(list1, list2):
    current = dummy = NodeV1(None)
    while list1 and list2:
        if list1.value < list2.value:
            current.next = list1
            list1, current = list1.next, list1
        else:
            current.next = list2
            list2, current = list2.next, list2
    if list1 or list2:
        current.next = list1 if list1 else list2
    return dummy.next
