import unittest

from data_structures.linked_list import Node, SinglyLinkedList


class NodeTests(unittest.TestCase):
    def setUp(self):
        self.node = Node()
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
        self.next_node = Node(self.data)
        self.node.set_next(self.next_node)
        self.assertEqual(self.next_node, self.node.get_next())
        self.assertEqual(self.next_node.get_data(), self.node.get_next().get_data())


class SinglyLinkedListTests(unittest.TestCase):
    def setUp(self):
        self.linked_list = SinglyLinkedList()
        self.data = 1

    def tearDown(self):
        pass

    def test_insertion(self):
        self.assertEqual(0, self.linked_list.size())
        self.linked_list.insert(self.data)
        self.assertEqual(1, self.linked_list.size())
        self.assertEqual(self.data, self.linked_list.get_head().get_data())

        # insert another item
        self.data = 2
        self.linked_list.insert(self.data)
        self.assertEqual(2, self.linked_list.size())
        self.assertEqual(self.data, self.linked_list.get_head().get_data())

    def test_search(self):
        self.linked_list.insert(self.data)
        self.assertEqual(self.data, self.linked_list.search(self.data).get_data())

    def test_delete(self):
        self.assertEqual(0, self.linked_list.size())
        self.linked_list.insert(self.data)
        self.assertEqual(1, self.linked_list.size())
        self.linked_list.delete(self.data)
        self.assertEqual(0, self.linked_list.size())
        self.assertEqual(None, self.linked_list.get_head())
