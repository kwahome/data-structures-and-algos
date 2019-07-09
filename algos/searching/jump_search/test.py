import unittest
from algos.searching import TEST_CASES
from .search import jump_search


class JumpSearchTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_searching(self):
        # for strategy in [STRATEGIES.ITERATIVE, STRATEGIES.RECURSIVE]:
        for case in TEST_CASES["CASES"]:
            self.assertEqual(
                case[1],
                jump_search(TEST_CASES["SORTED_SEARCH_ARRAY"], case[0])
            )
