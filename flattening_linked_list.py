# Helper code

# A class behaves like a data-type, just like an int, float or any other built-in ones.
# User defined class
class Node:
    def __init__(self, value):
        # <-- For simple LinkedList, "value" argument will be an int, whereas, for NestedLinkedList, "value" will be a LinkedList
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


# User defined class
class LinkedList:
    def __init__(self, head):  # <-- Expects "head" to be a Node made up of an int or LinkedList
        self.head = head

    '''
    For creating a simple LinkedList, we will pass an integer as the "value" argument
    For creating a nested LinkedList, we will pass a LinkedList as the "value" argument
    '''

    def append(self, value):

        # If LinkedList is empty
        if self.head is None:
            self.head = Node(value)
            return
        # Create a temporary Node object
        node = self.head
        # Iterate till the end of the current LinkedList
        while node.next is not None:
            node = node.next
        # Append the newly created Node at the end of the current LinkedList
        node.next = Node(value)

    '''We will need this function to convert a LinkedList object into a Python list of integers'''

    def to_list(self):
        out = []  # <-- Declare a Python list
        node = self.head  # <-- Create a temporary Node object

        while node:  # <-- Iterate until we have nodes available
            out.append(int(str(
                node.value)))  # <-- node.value is actually of type Node, therefore convert it into int before appending to the Python list
            node = node.next
        return out


def merge(list1, list2):
    merge = LinkedList(None)
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    list1_elt = list1.head
    list2_elt = list2.head
    while list1_elt is not None and list2_elt is not None:
        if list1_elt is None:
            merge.append(list2_elt)
            list2_elt = list2_elt.next
        elif list2_elt is None:
            merge.append(list1_elt)
            list1_elt = list1_elt.next
        elif list1_elt.value <= list2_elt.value:
            merge.append(list1_elt)
            list1_elt = list1_elt.next
        else:
            merge.append(list2_elt)
            list2_elt = list2_elt.next
    return merge


class NestedLinkedList(LinkedList):
    def flatten(self):
        return self._flatten(self.head)

    def _flatten(self, node):
        if node.next is None:
            return merge(node.value, None)
        return merge(node.value, self._flatten(node.next))
