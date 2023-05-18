# Use this class as the nodes in your linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class SortedLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        """
        Append a value to the Linked List in ascending sorted order

        Args:
           value(int): Value to add to Linked List
        """
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next is not None and node.value < value:
            node = node.next

        node.next = Node(value)


# Test cases
linked_list = SortedLinkedList()
linked_list.append(3)
print("Pass" if (linked_list.head.value == 3) else "Fail")

linked_list.append(2)
print("Pass" if (linked_list.head.value == 2) else "Fail")

linked_list.append(4)
node = linked_list.head.next.next
print("Pass" if (node.value == 4) else "Fail")


def sort(array):

    sorted_array = []
    linked_list = SortedLinkedList()

    for value in array:
        linked_list.append(value)

    node = linked_list.head
    while node:
        sorted_array.append(node.value)
        node = node.next

    return sorted_array
