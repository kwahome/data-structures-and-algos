import unittest

from algos.searching import TEST_CASES
from .search import linear_search


class LinearSearchTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_searching(self):
        for case in TEST_CASES:
            self.assertEqual(
                case[2],
                linear_search(case[0], case[1])
            )
