from tree.Node import Node
from tree.MyQueue import Queue
from tree.Stack import Stack


class Tree(object):
    def __init__(self, val=None):
        self.root = Node(val)

    def get_root(self):
        return self.root

    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq((node, level))
        while len(q) > 0:
            node, level = q.deq()
            if node is None:
                visit_order.append(("<empty>", level))
                continue
            visit_order.append((node, level))

            if node.has_left_child():
                q.enq((node.get_left_child(), level + 1))
            else:
                q.enq((None, level + 1))

            if node.has_right_child():
                q.enq((node.get_right_child(), level + 1))
            else:
                q.enq((None, level + 1))

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level
        return s


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

    # Walk through the steps with code
    visit_order = list()
    stack = Stack()

    # start at the root node, visit it and then add it to the stack
    node = tree.get_root()
    stack.push(node)

    print(f"""
    visit_order {visit_order} 
    stack: 
    {stack}
    """)

    # visit apple (root)
    visit_order.append(node.get_value())
    print(f"""visit_order {visit_order}  
    {stack}
    """)

    # check if apple (root) has a left child
    print(f"""{node} has left child? {node.has_left_child()}""")

    # since apple has a left child (banana)
    # we'll visit banana and add it to the stack
    if node.has_left_child():
        node = node.get_left_child()
        stack.push(node)

    print(f"""
    visit_order {visit_order}
    stack: 
    {stack}
    """)

    # visit banana (first level's left child)
    print(f"visit {node}")
    visit_order.append(node.get_value())
    print(f"""visit_order {visit_order}""")

    # check if banana has a left child (second level's left child)
    print(f"{node} has left child ? {node.has_left_child()}")

    # since banana has a left child "dates"
    # we'll visit "dates" and add it to the stack
    if node.has_left_child():
        node = node.get_left_child()
        stack.push(node)

    print(f"""
    visit_order {visit_order}
    stack: {stack}
    """)

    # visit dates (second level's left child)
    visit_order.append(node.get_value())
    print(f"visit order {visit_order}")

    # check if "dates" has a left child -> return boolean value
    print(f"{node} has left child? {node.has_left_child()}")

    # since dates doesn't have a left child, we'll check if it has a right child
    print(f"{node} has right child? {node.has_right_child()}")

    # since "dates" is a leaf node (has no children), we can start to retrace our steps
    # in other words, we can pop it off the stack.
    print(stack.pop())

    print(stack)

    # now we'll set the node to the new top of the stack, which is banana
    node = stack.top()
    print(node)

    # we already checked for banana's left child, so we'll check for its right child
    print(f"{node} has right child? {node.has_right_child()}")

    # banana doesn't have a right child, so we're also done tracking it.
    # so we can pop banana off the stack
    print(f"pop {stack.pop()} off stack")
    print(f"""
    stack {stack}
    """)

    # now we'll track the new top of the stack, which is apple
    node = stack.top()
    print(node)

    # we've already checked if apple has a left child; we'll check if it has a right child
    print(f"{node} has right child? {node.has_right_child()}")

    # since it has a right child (cherry),
    # we'll visit cherry and add it to the stack.

    if node.has_right_child():
        node = node.get_right_child()
        stack.push(node)

    print(f"""
    visit_order {visit_order}
    stack {stack}
    """)

    # visit cherry ( first level's right child)
    print(f"visit {node}")
    visit_order.append(node.get_value())
    print(f"""visit_order: {visit_order}""")

    # Now we'll check if cherry (first level's right child) has a left child
    print(f"{node} has left child? {node.has_left_child()}")

    # it doesn't, so we'll check if it has a right child
    print(f"{node} has right child? {node.has_right_child()}")

    # since cherry has neither left nor right child nodes,
    # we are done tracking it, and can pop it off the stack
    print(f"pop {stack.pop()} off the stack")

    print(f"""
    visit_order {visit_order}
    stack
    {stack}
    """)

    # now we're back to the apple at the top of the stack.
    # since we're already checked apple's left and right child nodes.
    # we can pop apple off the stack

    print(f"pop {stack.pop()} off stack")
    print(f"pre-order traversal visited nodes in this order: {visit_order}")

    print(f"""stack 
    {stack}
    """)
