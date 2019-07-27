import unittest

from data_structures.linked_list import InsertPositions, SearchPositions
from data_structures.linked_list.doubly_linked import DoublyLinkedList


class DoublyLinkedListTests(unittest.TestCase):
    def setUp(self):
        self.linked_list = DoublyLinkedList()
        self.data = 1

    def tearDown(self):
        pass

    def test_inserting_after(self):
        #: insert positionally after in an empty linked list defaults operation to beginning of list
        self.position = InsertPositions.AFTER
        self.assertEqual(0, self.linked_list.size())
        self.assertEqual(None, self.linked_list.get_head())
        self.assertEqual(None, self.linked_list.get_tail())
        self.linked_list.insert(self.data, position=self.position)
        self.assertEqual(1, self.linked_list.size())
        self.assertEqual(self.data, self.linked_list.get_head().get_data())
        self.assertEqual(self.data, self.linked_list.get_tail().get_data())
        self.assertEqual(None, self.linked_list.get_head().get_previous())
        self.assertEqual(None, self.linked_list.get_head().get_next())
        self.assertEqual(None, self.linked_list.get_tail().get_previous())
        self.assertEqual(None, self.linked_list.get_tail().get_next())
        self.assertListEqual([1], self.linked_list.to_array())

        #: insert another item after the first item
        #: we don't expect inserted item at head of the list
        self.reference, self.data = self.data, 2
        self.linked_list.insert(self.data, position=self.position, reference_value=self.reference)
        self.assertEqual(2, self.linked_list.size())
        self.assertNotEqual(self.data, self.linked_list.get_head().get_data())
        self.assertEqual(self.reference, self.linked_list.get_head().get_data())
        self.assertEqual(self.data, self.linked_list.get_head().get_next().get_data())
        self.assertEqual(self.data, self.linked_list.get_tail().get_data())
        self.assertEqual(self.reference, self.linked_list.get_tail().get_previous().get_data())
        self.assertEqual(None, self.linked_list.get_tail().get_next())
        self.assertListEqual([1, 2], self.linked_list.to_array())

        #: insert another item after the a non-present item defaults operation to beginning of list
        #: we expect inserted item at head of the list
        self.reference, self.data = 4, 3
        self.linked_list.insert(self.data, position=self.position, reference_value=self.reference)
        self.assertEqual(3, self.linked_list.size())
        self.assertEqual(self.data, self.linked_list.get_head().get_data())
        self.assertEqual(1, self.linked_list.get_head().get_next().get_data())
        self.assertEqual(
            self.data, self.linked_list.get_head().get_next().get_previous().get_data()
        )
        self.assertEqual(2, self.linked_list.get_tail().get_data())
        self.assertEqual(2, self.linked_list.get_head().get_next().get_next().get_data())
        self.assertEqual(
            1, self.linked_list.get_head().get_next().get_next().get_previous().get_data()
        )
        self.assertListEqual([3, 1, 2], self.linked_list.to_array())

        #: insert another item after an item that is in between the head and tail of the list
        #: we don't expect inserted item at head of the list
        self.reference, self.data = 1, 4
        self.linked_list.insert(self.data, position=self.position, reference_value=self.reference)
        self.assertEqual(4, self.linked_list.size())
        self.assertNotEqual(self.data, self.linked_list.get_head().get_data())
        self.assertEqual(1, self.linked_list.get_head().get_next().get_data())
        self.assertEqual(3, self.linked_list.get_head().get_next().get_previous().get_data())
        self.assertEqual(self.data, self.linked_list.get_head().get_next().get_next().get_data())
        self.assertEqual(
            1, self.linked_list.get_head().get_next().get_next().get_previous().get_data()
        )
        self.assertEqual(
            2, self.linked_list.get_head().get_next().get_next().get_next().get_data()
        )
        self.assertEqual(
            self.data,
            self.linked_list.get_head().get_next().get_next().get_next().get_previous().get_data()
        )
        self.assertListEqual([3, 1, 4, 2], self.linked_list.to_array())

    def test_inserting_before(self):
        #: insert positionally after in an empty linked list defaults operation to beginning of list
        self.position = InsertPositions.BEFORE
        self.assertEqual(0, self.linked_list.size())
        self.assertEqual(None, self.linked_list.get_head())
        self.assertEqual(None, self.linked_list.get_tail())
        self.linked_list.insert(self.data, position=self.position)
        self.assertEqual(1, self.linked_list.size())
        self.assertEqual(self.data, self.linked_list.get_head().get_data())
        self.assertEqual(self.data, self.linked_list.get_tail().get_data())
        self.assertEqual(None, self.linked_list.get_head().get_previous())
        self.assertEqual(None, self.linked_list.get_head().get_next())
        self.assertEqual(None, self.linked_list.get_tail().get_previous())
        self.assertEqual(None, self.linked_list.get_tail().get_next())
        self.assertListEqual([1], self.linked_list.to_array())

        #: insert another item before the first item
        #: we expect inserted item at head of the list as there's only one item in the list
        self.reference, self.data = self.data, 2
        self.linked_list.insert(self.data, position=self.position, reference_value=self.reference)
        self.assertEqual(2, self.linked_list.size())
        self.assertEqual(self.data, self.linked_list.get_head().get_data())
        self.assertEqual(self.reference, self.linked_list.get_head().get_next().get_data())
        self.assertEqual(self.reference, self.linked_list.get_tail().get_data())
        self.assertEqual(self.data, self.linked_list.get_tail().get_previous().get_data())
        self.assertEqual(None, self.linked_list.get_tail().get_next())
        self.assertListEqual([2, 1], self.linked_list.to_array())

        #: insert another item after the a non-present item defaults operation to beginning of list
        #: we expect inserted item at head of the list
        self.reference, self.data = 4, 3
        self.linked_list.insert(self.data, position=self.position, reference_value=self.reference)
        self.assertEqual(3, self.linked_list.size())
        self.assertEqual(self.data, self.linked_list.get_head().get_data())
        self.assertEqual(2, self.linked_list.get_head().get_next().get_data())
        self.assertEqual(
            self.data, self.linked_list.get_head().get_next().get_previous().get_data()
        )
        self.assertEqual(1, self.linked_list.get_tail().get_data())
        self.assertEqual(1, self.linked_list.get_head().get_next().get_next().get_data())
        self.assertEqual(
            2, self.linked_list.get_head().get_next().get_next().get_previous().get_data()
        )
        self.assertListEqual([3, 2, 1], self.linked_list.to_array())

        #: insert another item after an item that is in between the head and tail of the list
        #: we don't expect inserted item at head of the list
        self.reference, self.data = 1, 4
        self.linked_list.insert(self.data, position=self.position, reference_value=self.reference)
        self.assertEqual(4, self.linked_list.size())
        self.assertNotEqual(self.data, self.linked_list.get_head().get_data())
        self.assertEqual(2, self.linked_list.get_head().get_next().get_data())
        self.assertEqual(3, self.linked_list.get_head().get_next().get_previous().get_data())
        self.assertEqual(self.data, self.linked_list.get_head().get_next().get_next().get_data())
        self.assertEqual(
            2, self.linked_list.get_head().get_next().get_next().get_previous().get_data()
        )
        self.assertEqual(
            1, self.linked_list.get_head().get_next().get_next().get_next().get_data()
        )
        self.assertEqual(
            1, self.linked_list.get_tail().get_data()
        )
        self.assertEqual(
            self.data,
            self.linked_list.get_head().get_next().get_next().get_next().get_previous().get_data()
        )
        self.assertListEqual([3, 2, 4, 1], self.linked_list.to_array())

    def test_inserting_at_beginning(self):
        self.assertEqual(0, self.linked_list.size())
        self.assertEqual(None, self.linked_list.get_head())
        self.assertEqual(None, self.linked_list.get_tail())
        self.linked_list.push(self.data)
        self.assertEqual(1, self.linked_list.size())
        self.assertEqual(self.data, self.linked_list.get_head().get_data())
        self.assertEqual(self.data, self.linked_list.get_tail().get_data())
        self.assertEqual(None, self.linked_list.get_head().get_previous())
        self.assertEqual(None, self.linked_list.get_head().get_next())
        self.assertEqual(None, self.linked_list.get_tail().get_previous())
        self.assertEqual(None, self.linked_list.get_tail().get_next())
        self.assertListEqual([1], self.linked_list.to_array())

        #: insert another item
        self.previous, self.data = self.data, 2
        self.linked_list.push(self.data)
        self.assertEqual(2, self.linked_list.size())
        self.assertEqual(self.data, self.linked_list.get_head().get_data())
        self.assertEqual(self.previous, self.linked_list.get_head().get_next().get_data())
        self.assertEqual(self.data, self.linked_list.get_tail().get_previous().get_data())
        self.assertEqual(None, self.linked_list.get_tail().get_next())
        self.assertListEqual([2, 1], self.linked_list.to_array())

    def test_inserting_at_end(self):
        self.assertEqual(0, self.linked_list.size())
        self.assertEqual(None, self.linked_list.get_head())
        self.assertEqual(None, self.linked_list.get_tail())
        self.linked_list.append(self.data)
        self.assertEqual(1, self.linked_list.size())
        self.assertEqual(self.data, self.linked_list.get_head().get_data())
        self.assertEqual(self.data, self.linked_list.get_tail().get_data())
        self.assertEqual(None, self.linked_list.get_head().get_previous())
        self.assertEqual(None, self.linked_list.get_head().get_next())
        self.assertListEqual([1], self.linked_list.to_array())

        #: insert another item
        self.previous, self.data = self.data, 2
        self.linked_list.append(self.data)
        self.assertEqual(2, self.linked_list.size())
        self.assertEqual(self.previous, self.linked_list.get_head().get_data())
        self.assertEqual(self.data, self.linked_list.get_head().get_next().get_data())
        self.assertEqual(self.previous, self.linked_list.get_tail().get_previous().get_data())
        self.assertEqual(None, self.linked_list.get_tail().get_next())
        self.assertListEqual([1, 2], self.linked_list.to_array())

    def test_search(self):
        self.assertEqual(0, self.linked_list.size())
        self.linked_list.insert(self.data)
        self.assertEqual(1, self.linked_list.size())
        self.assertEqual(self.data, self.linked_list.search(self.data).get_data())
        #: no node before, inserted item at head of list
        self.assertEqual(None, self.linked_list.search(self.data, position=SearchPositions.BEFORE))
        #: no node after, only one item in the list
        self.assertEqual(None, self.linked_list.search(self.data, position=SearchPositions.AFTER))

        #: insert new item and search positionally
        self.previous, self.data = self.data, 2
        #: insert with default behaviour; i.e. at the beginning of the linked list
        self.linked_list.insert(self.data)
        #: search self.data, nothing should be before, self.previous should be after
        #: because the insert was done at the beginning
        self.assertEqual(None, self.linked_list.search(self.data, position=SearchPositions.BEFORE))
        self.assertEqual(
            self.previous,
            self.linked_list.search(self.data, position=SearchPositions.AFTER).get_data()
        )
        #: search self.previous, self.data should be before, nothing should be after
        #: because the insert was done at the beginning
        self.assertEqual(
            self.data,
            self.linked_list.search(self.previous, position=SearchPositions.BEFORE).get_data()
        )
        self.assertEqual(
            None, self.linked_list.search(self.previous, position=SearchPositions.AFTER)
        )

        #: search non-existing item
        self.assertEqual(
            None, self.linked_list.search("does not exist")
        )
        #: search for node after
        self.assertEqual(
            None, self.linked_list.search("does not exist", position=SearchPositions.AFTER)
        )
        #: search for node before
        self.assertEqual(
            None, self.linked_list.search("does not exist", position=SearchPositions.BEFORE)
        )

    def test_delete(self):
        self.assertEqual(0, self.linked_list.size())
        self.linked_list.insert(self.data)
        self.assertEqual(1, self.linked_list.size())
        self.assertListEqual([1], self.linked_list.to_array())
        self.linked_list.delete(self.data)
        self.assertEqual(0, self.linked_list.size())
        self.assertListEqual([], self.linked_list.to_array())
        self.assertEqual(None, self.linked_list.get_head())

        #: use a bigger list
        self.assertEqual(0, self.linked_list.size())
        self.linked_list.push(self.data)
        self.linked_list.append(2)
        self.linked_list.insert(3, position=InsertPositions.AFTER, reference_value=self.data)
        self.linked_list.insert(4, position=InsertPositions.BEFORE, reference_value=self.data)
        self.assertEqual(4, self.linked_list.size())
        self.assertListEqual([4, 1, 3, 2], self.linked_list.to_array())

        #: delete a non-existent item
        self.linked_list.delete("non-existent")
        self.assertEqual(4, self.linked_list.size())
        self.assertListEqual([4, 1, 3, 2], self.linked_list.to_array())
        self.assertEqual(4, self.linked_list.get_head().get_data())
        self.assertEqual(2, self.linked_list.get_tail().get_data())

        #: delete 1
        self.linked_list.delete(self.data)
        self.assertEqual(3, self.linked_list.size())
        self.assertListEqual([4, 3, 2], self.linked_list.to_array())
        self.assertEqual(3, self.linked_list.get_head().get_next().get_data())
        self.assertEqual(4, self.linked_list.search(3).get_previous().get_data())

        #: delete 4; head of the list
        self.linked_list.delete(4)
        self.assertEqual(2, self.linked_list.size())
        self.assertListEqual([3, 2], self.linked_list.to_array())
        self.assertEqual(3, self.linked_list.get_head().get_data())
        self.assertEqual(None, self.linked_list.get_head().get_previous())
        self.assertEqual(2, self.linked_list.get_head().get_next().get_data())
        self.assertEqual(3, self.linked_list.get_tail().get_previous().get_data())
        self.assertEqual(None, self.linked_list.get_tail().get_next())

        #: delete 2; tail of the list
        self.linked_list.delete(2)
        self.assertEqual(1, self.linked_list.size())
        self.assertListEqual([3], self.linked_list.to_array())
        self.assertEqual(3, self.linked_list.get_head().get_data())
        self.assertEqual(None, self.linked_list.get_head().get_previous())
        self.assertEqual(None, self.linked_list.get_head().get_next())
        self.assertEqual(None, self.linked_list.get_tail().get_previous())
        self.assertEqual(None, self.linked_list.get_tail().get_next())
