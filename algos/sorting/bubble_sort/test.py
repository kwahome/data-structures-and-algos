import unittest
from algos.sorting import TEST_CASES
from .sort import bubble_sort


class BubbleSortTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sorting(self):
        for case in TEST_CASES["CASES"]:
            self.assertEqual(
                case[1],
                bubble_sort(case[0], order=case[2])
            )
