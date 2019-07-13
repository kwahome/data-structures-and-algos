import unittest
import copy

from algos import STRATEGIES
from algos.sorting import TEST_CASES
from .sort import selection_sort


class SelectionSortTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sorting(self):
        for strategy in [STRATEGIES.ITERATIVE, STRATEGIES.RECURSIVE]:
            for case in TEST_CASES:
                # deepcopy objects to maintain tests cases as they are mutated with each loop
                unsorted_array = copy.deepcopy(case[0])
                expected_output = copy.deepcopy(case[1])
                ordering = case[2]
                self.assertEqual(
                    expected_output,
                    selection_sort(unsorted_array, order=ordering, strategy=strategy)
                )
