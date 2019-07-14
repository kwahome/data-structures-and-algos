class Node:
    """Class implementing a `node` in a tree

    Each tree node contains following parts:
        - data
        - a pointer to left child
        - a pointer to right child
    """

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        #: compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()

