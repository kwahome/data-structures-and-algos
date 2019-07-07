import unittest
from algos.sorting import ASCENDING, DESCENDING, TEST_CASES
from .sort import quick_sort


class QuickSortTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_ascending_sorting(self):
        self.assertListEqual(
            TEST_CASES["SORTED"][ASCENDING],
            quick_sort(TEST_CASES["UNSORTED"], order=ASCENDING)
        )

    def test_descending_sorting(self):
        self.assertListEqual(
            TEST_CASES["SORTED"][DESCENDING],
            quick_sort(TEST_CASES["UNSORTED"], order=DESCENDING)
        )
