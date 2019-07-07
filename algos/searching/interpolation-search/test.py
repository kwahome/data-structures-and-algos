import unittest
from algos.searching import TEST_CASES
from .search import interpolation_search


class InterpolationSearchTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_existing_target_found(self):
        self.assertEqual(
            TEST_CASES["EXISTING_TARGET"]["EXPECTED"],
            interpolation_search(
                TEST_CASES["SORTED_ARRAY"], TEST_CASES["EXISTING_TARGET"]["VALUE"]
            )
        )

    def test_nonexistent_target_not_found(self):
        self.assertEqual(
            TEST_CASES["NONEXISTING_TARGET"]["EXPECTED"],
            interpolation_search(
                TEST_CASES["SORTED_ARRAY"], TEST_CASES["NONEXISTING_TARGET"]["VALUE"]
            )
        )
