import unittest

from data_structures.tree_based import Node


class BinaryTreeNodeTests(unittest.TestCase):
    def setUp(self):
        self.node = Node()
        self.data = 5

    def tearDown(self):
        pass

    def test_set_and_get_data(self):
        self.assertEqual(None, self.node.get_data())
        self.node.set_data(self.data)
        self.assertEqual(self.data, self.node.get_data())

    def test_set_and_get_left(self):
        self.assertEqual(None, self.node.get_data())
        left_node = Node(1)
        self.node.set_left(left_node)
        self.assertEqual(left_node, self.node.get_left())

    def test_set_and_get_right(self):
        self.assertEqual(None, self.node.get_data())
        right_node = Node(10)
        self.node.set_right(right_node)
        self.assertEqual(right_node, self.node.get_right())
