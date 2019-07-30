from data_structures.tree_based import Node


class Tree(Node):
    """Class implementing a binary tree
    """

    def insert(self, data):
        parent = self.get_data()
        if parent:
            if data < parent:
                left = self.get_left()
                if left:
                    left.insert(data)
                else:
                    self.set_left(Tree(data))
            elif data > parent:
                right = self.get_right()
                if right:
                    right.insert(data)
                else:
                    self.set_right(Tree(data))
        else:
            self.set_data(data)

    def print_tree(self):
        left, right = self.get_left(), self.get_right()
        if left:
            left.print_tree()
        print(self.get_data())
        if right:
            right.print_tree()
