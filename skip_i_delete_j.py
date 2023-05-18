class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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
        print(head.data, end=' ')
        head = head.next
    print()


def skip_i_delete_j(head, i, j):
    # Edge case - Skip 0 nodes ( means delete all nodes )
    if i == 0:
        return None
    # Edge case - Delete 0 nodes
    if j == 0:
        return head
    # Invalid input
    if head is None or j < 0 or i < 0:
        return head

    # helper references
    current = head
    previous = None

    # Traverse - Loop until there are Nodes available in the LinkedList
    while current:
        """
            skip ( i - 1 ) nodes
        """
        for _ in range(i - 1):
            if current is None:
                return head
            current = current.next
        previous = current
        current = current.next

        """
            delete next j nodes
        """
        for _ in range(j):
            if current is None:
                break
            next_node = current.next
            current = next_node

        """
            Connect the `previous.next` to the `current`
        """
        previous.next = current

    # Loop ends
    return head


if __name__ == '__main__':
    head = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    print_linked_list(head)
    head = skip_i_delete_j(head, 2, 3)
    print_linked_list(head)

    # Second
    head = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    print_linked_list(skip_i_delete_j(head, 2, 2))
