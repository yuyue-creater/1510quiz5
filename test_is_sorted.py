from unittest import TestCase
from is_sorted import is_sorted


class Test(TestCase):

    def test_empty(self):
        self.assertEqual(False, is_sorted([]))

    def test_one_integer(self):
        self.assertEqual(True, is_sorted([1]))

    def test_increasing(self):
        self.assertEqual(True, is_sorted([1, 2, 3]))

    def test_decreasing(self):
        self.assertEqual(False, is_sorted([3, 1, 2]))

    def test_zeroes(self):
        self.assertEqual(True, is_sorted([0, 0, 0]))

    def test_negatives_decreasing(self):
        self.assertEqual(False, is_sorted([-1, -2, -3]))

    def test_negative_increasing(self):
        self.assertEqual(False, is_sorted([-3, -1, -2]))

    def test_negative_order(self):
        self.assertEqual(True, is_sorted([-3, -2, -1]))
