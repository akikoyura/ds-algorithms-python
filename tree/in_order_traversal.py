# define in-order traversal
from tree.Node import Node
from tree.Stack import Stack
from tree.Tree import Tree


def in_order(tree):
    visited_order = list()

    def traverse(node):
        if node:
            traverse(node.get_left_child())
            visited_order.append(node.get_value())
            traverse(node.get_right_child())

    traverse(tree.get_root())

    return visited_order


if __name__ == '__main__':
    # create a tree and add some nodes
    tree = Tree("apple")  # root node

    # set first level's left child
    tree.get_root().set_left_child(Node("banana"))

    # set first level's right child
    tree.get_root().set_right_child(Node("cherry"))

    # set second level's left child
    # by getting the first level's left child first
    tree.get_root().get_left_child().set_left_child(Node("dates"))

    visited_order = in_order(tree)

    # check solution: should get ['dates', 'banana', 'apple', 'cherry']
    print(visited_order)
