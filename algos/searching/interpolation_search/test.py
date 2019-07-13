import unittest

from algos import STRATEGIES
from algos.searching import TEST_CASES
from .search import interpolation_search


class InterpolationSearchTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_searching(self):
        for strategy in [STRATEGIES.ITERATIVE, STRATEGIES.RECURSIVE]:
            for case in TEST_CASES:
                self.assertEqual(
                    case[2],
                    interpolation_search(case[0], case[1], strategy=strategy)
                )
