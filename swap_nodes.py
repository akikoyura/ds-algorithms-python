class Node:
    """LinkedListNode class to be used for this problem"""

    def __init__(self, data):
        self.data = data
        self.next = None


def swap_nodes(head, left_index, right_index):
    # Check invalid Input
    if head is None or left_index < 0 or right_index < 0:
        return head

    # helper references
    current = head
    previous = None
    while current:
        if left_index == 0:
            previous = current
        else:
            for _ in range(left_index - 1):
                if current is None:
                    return head
                current = current.next
            previous = current
            current = current.next

        for _ in range(right_index - left_index - 1):
            if current is None:
                break
            next_node = current.next
            current = next_node
        break

    one_previous = previous
    one_current = previous.next
    two_previous = current
    two_current = current.next

    # swapping step
    two_previous.next = one_current
    tmp = one_current.next
    one_current.next = two_current.next
    two_current.next = tmp
    one_previous.next = two_current

    # loop ends
    return head


def swap_nodes_v1(head, left_index, right_index):
    # check invalid input
    if left_index == right_index:
        return head

    # Helper references
    one_previous = None
    one_current = None

    two_previous = None
    two_current = None

    current_index = 0
    current_node = head
    new_head = None

    # Loop - find out previous and current node at both the positions ( indices )
    while current_node is not None:

        # Position_one cannot be equal to position_two
        # so either one of them might be equal to the current_index
        if current_index == left_index:
            one_current = current_node
        elif current_index == right_index:
            two_current = current_node

        # If neither of the position_one or position_two are equal to the current_index
        if one_current is None:
            one_previous = current_node
        two_previous = current_node

        # increment both the current_index and current_node
        current_node = current_node.next
        current_index += 1

    # Loop ends

    # We have identified the two nodes: one_current & two_current to be swapped,
    # Make use of a temporary reference to swap the references
    two_previous.next = one_current
    temp = one_current.next
    one_current.next = two_current.next
    two_current.next = temp

    # If the code at first index is head of the original linked list
    if one_previous is None:
        new_head = two_current
    else:
        one_previous.next = two_current
        new_head = head
    # Swapping logic ends
    return new_head


# helper functions for testing purpose
def create_linked_list(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head


def print_linked_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()


if __name__ == '__main__':
    head = create_linked_list([3, 4, 5, 2, 6, 1, 9])
    position_one = 2
    position_two = 5
    print_linked_list(swap_nodes(head, position_one, position_two))

    left_index = 0
    right_index = 1
    head = create_linked_list([3, 4, 5, 2, 6, 1, 9])
    print_linked_list(swap_nodes_v1(head, left_index, right_index))
