from node.Node import Node


class LinkedListV1:
    def __init__(self, init_list=None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next
        current.next = Node(value)
        return


def is_circular(linked_list):
    if linked_list.head is None:
        return False

    slow = linked_list.head
    fast = linked_list.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next
        if slow == fast:
            return True
    return False


if __name__ == '__main__':
    list_with_loop = LinkedListV1([2, -1, 3, 0, 5])
    loop_start = list_with_loop.head.next
    current = list_with_loop.head
    while current.next:
        current = current.next
    current.next = loop_start
