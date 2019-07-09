import unittest
import copy

from algos.sorting import TEST_CASES
from .sort import merge_sort


class MergeSortTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sorting(self):
        for case in TEST_CASES["CASES"]:
            unsorted_array = copy.deepcopy(case[0])
            expected_output = copy.deepcopy(case[1])
            ordering = case[2]
            self.assertEqual(
                expected_output,
                merge_sort(unsorted_array, order=ordering)
            )
