import unittest
from algos.sorting import ASCENDING, DESCENDING, TEST_CASES
from .sort import selection_sort


class SelectionSortTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_ascending_sorting(self):
        self.assertListEqual(
            TEST_CASES["SORTED"][ASCENDING],
            selection_sort(TEST_CASES["UNSORTED"], order=ASCENDING)
        )

    def test_descending_sorting(self):
        self.assertListEqual(
            TEST_CASES["SORTED"][DESCENDING],
            selection_sort(TEST_CASES["UNSORTED"], order=DESCENDING)
        )
