from tree.Node import Node
from tree.MyQueue import Queue
from tree.Tree import Tree

if __name__ == '__main__':
    tree = Tree("apple")
    tree.get_root().set_left_child(Node("banana"))
    tree.get_root().set_right_child(Node("cherry"))
    tree.get_root().get_left_child().set_left_child(Node("dates"))

    visited_order = list()

    q = Queue()

    # start at the root node and add it to the queue
    node = tree.get_root()
    q.enq(node)
    print(q)

    # dequeue the next node in the queue
    # "visit" that node
    # also add its children to the queue

    node = q.deq()
    visited_order.append(node)
    if node.has_left_child():
        q.enq(node.get_left_child())
    if node.has_right_child():
        q.enq(node.get_right_child())

    print(f"visit order: {visited_order}")

    # dequeue the next node (banana)
    # visit it, and add its children (dates) to the queue
    node = q.deq()
    visited_order.append(node)
    if node.has_left_child():
        q.enq(node.get_left_child())
    if node.has_right_child():
        q.enq(node.get_right_child())

    print(f"visit order: {visited_order}")

    # dequeue the next node (dates)
    # visit it, and add its children (there are None ) to the queue
    node = q.deq()
    visited_order.append(node)
    if node.has_left_child():
        q.enq(node.get_left_child())
    if node.has_right_child():
        q.enq(node.get_right_child())

    print(f"visit order: {visited_order}")
    print(q)
