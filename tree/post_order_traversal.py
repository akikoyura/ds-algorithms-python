# define post_order traversal
from tree.Node import Node
from tree.Tree import Tree


def post_order(tree):
    visited_list = list()

    def traverse(node):
        if node:
            traverse(node.get_left_child())
            traverse(node.get_right_child())
            visited_list.append(node.get_value())

    traverse(tree.get_root())

    return visited_list


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

    visit_order = post_order(tree)
    print(visit_order)
