import unittest
from algos.searching import TEST_CASES
from .search import exponential_search


class ExponentialSearchTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_searching(self):
        for case in TEST_CASES["CASES"]:
            self.assertEqual(
                case[1],
                exponential_search(TEST_CASES["SORTED_SEARCH_ARRAY"], case[0])
            )