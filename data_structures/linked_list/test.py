import unittest

from data_structures.linked_list import BaseNode


class BaseNodeTests(unittest.TestCase):
    def setUp(self):
        self.node = BaseNode()
        self.data = 1

    def tearDown(self):
        pass

    def test_get_data(self):
        self.assertEqual(None, self.node.get_data())

    def test_set_data(self):
        self.node.set_data(self.data)
        self.assertEqual(self.data, self.node.get_data())

    def test_get_next(self):
        self.assertEqual(None, self.node.get_next())

    def test_set_next(self):
        self.data = 2
        self.next_node = BaseNode(self.data)
        self.node.set_next(self.next_node)
        self.assertEqual(self.next_node, self.node.get_next())
        self.assertEqual(self.next_node.get_data(), self.node.get_next().get_data())
