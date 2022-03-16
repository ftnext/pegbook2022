from unittest import TestCase

from first_parser import calc


class CalcTestCase(TestCase):
    def test_case1_str_to_float(self):
        self.assertEqual(calc("1"), 1.0)

    def test_case2_add_two_terms(self):
        self.assertEqual(calc("1+2"), 3.0)
