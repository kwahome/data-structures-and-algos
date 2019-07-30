class Node:
    """Class implementing a `node` in a tree

    Each tree node contains following parts:
        - data
        - a pointer to left child
        - a pointer to right child
    """

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def get_data(self):
        """Getter for node value.

        :return: data value
        """
        return self.value

    def set_data(self, value):
        """Setter for node value.

        :param value:
        :return:
        """
        self.value = value

    def get_left(self):
        """Getter for left child.

        :return: left child node
        """
        return self.left

    def set_left(self, child):
        """Setter for left child.

        :param child: left child node
        :return:
        """
        self.left = child

    def get_right(self):
        """Getter for right child.

        :return: right child node
        """
        return self.right

    def set_right(self, child):
        """Setter for right child.

        :param child: right child node
        :return:
        """
        self.right = child
