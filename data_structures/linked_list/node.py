class Node:
    """Class implementing a `node` in a linked list

    Each node contains following parts:
        - value
        - a pointer to the next node
    """

    def __init__(self, value):
        self.value = value
        self.next = None  #: the pointer initially points to nothing

    def traverse(self):
        pass

