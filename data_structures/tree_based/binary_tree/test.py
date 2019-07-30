import unittest

from data_structures.tree_based.binary_tree.tree import Tree


class BinaryTreeTests(unittest.TestCase):
    def setUp(self):
        self.binary_tree = Tree()

    def tearDown(self):
        pass

    def test_tree_insert(self):
        data = 5
        self.assertEqual(None, self.binary_tree.get_data())
        self.binary_tree.insert(data)
        self.assertEqual(data, self.binary_tree.get_data())
        data = 2
        self.binary_tree.insert(data)
        self.assertEqual(data, self.binary_tree.get_left().get_data())
        data = 1
        self.binary_tree.insert(data)
        self.assertEqual(data, self.binary_tree.get_left().get_left().get_data())
        data = 3
        self.binary_tree.insert(data)
        self.assertEqual(data, self.binary_tree.get_left().get_right().get_data())
        data = 10
        self.binary_tree.insert(data)
        self.assertEqual(data, self.binary_tree.get_right().get_data())
        data = 15
        self.binary_tree.insert(data)
        self.assertEqual(data, self.binary_tree.get_right().get_right().get_data())
        data = 9
        self.binary_tree.insert(data)
        self.assertEqual(data, self.binary_tree.get_right().get_left().get_data())

