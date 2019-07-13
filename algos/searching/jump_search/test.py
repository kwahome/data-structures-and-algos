import unittest

from algos import STRATEGIES
from algos.searching import TEST_CASES
from .search import jump_search


class JumpSearchTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_searching(self):
        for strategy in [STRATEGIES.ITERATIVE, STRATEGIES.RECURSIVE]:
            for case in TEST_CASES:
                self.assertEqual(
                    case[2],
                    jump_search(case[0], case[1], strategy=strategy)
                )
