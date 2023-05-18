from tree.Node import Node
from tree.Stack import Stack
from tree.Tree import Tree


def pre_order_with_stack_buggy(tree):
    visit_order = list()
    stack = Stack()
    node = tree.get_root()
    stack.push(node)
    node = stack.top()
    visit_order.append(node.get_value())
    count = 0
    loop_limit = 7
    while node and count < loop_limit:
        print(f"""
    loop count: {count}   
    current node: {node}
    stack: {stack}
        """)
        count += 1
        if node.has_left_child():
            node = node.get_left_child()
            stack.push(node)

            # using top() is redundant, but added for clarity
            node = stack.top()
            visit_order.append(node.get_value())

        elif node.has_right_child():
            node = node.get_right_child()
            stack.push(node)
            node = stack.top()
            visit_order.append(node.get_value())

        else:
            stack.pop()
            if not stack.is_empty():
                node = stack.top()
            else:
                node = None

    return visit_order


if __name__ == '__main__':
    # create a tree and add some nodes[p:wa
    tree = Tree("apple")  # root node

    # set first level's left child
    tree.get_root().set_left_child(Node("banana"))

    # set first level's right child
    tree.get_root().set_right_child(Node("Cherry"))

    # set second level's left child
    # by getting the first level's left child first
    tree.get_root().get_left_child().set_left_child(Node("dates"))

    visit_order = pre_order_with_stack_buggy(tree)
    print(visit_order)
