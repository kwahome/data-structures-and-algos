import unittest

from .reversal import inplace_reverse


class StringReversalTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_reversing_string(self):
        self.assertEqual("!dlroW olleH", inplace_reverse("Hello World!"))
