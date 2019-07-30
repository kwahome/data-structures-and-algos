import unittest

from data_structures.tree_based.binary_tree.tree import Tree


class BinaryTreeTests(unittest.TestCase):
    def setUp(self):
        self.binary_tree = Tree()

    def tearDown(self):
        pass

    def test_tree_insert(self):
        parent_value = 5
        self.assertEqual(None, self.binary_tree.get_data())
        self.binary_tree.insert(parent_value)
        self.assertEqual(parent_value, self.binary_tree.get_data())
        left_child = 1
        self.binary_tree.insert(left_child)
        self.assertEqual(left_child, self.binary_tree.get_left().get_data())
        right_child = 10
        self.binary_tree.insert(right_child)
        self.assertEqual(right_child, self.binary_tree.get_right().get_data())

