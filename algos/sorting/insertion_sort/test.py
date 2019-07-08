import unittest
from algos.sorting import TEST_CASES
from .sort import insertion_sort


class InsertionSortTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sorting(self):
        for case in TEST_CASES["CASES"]:
            self.assertEqual(
                case[1],
                insertion_sort(case[0], order=case[2])
            )
