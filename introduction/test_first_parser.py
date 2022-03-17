from unittest import TestCase

from first_parser import calc


class CalcTestCase(TestCase):
    def test_case1_str_to_float(self):
        self.assertEqual(calc("1"), 1.0)

    def test_case2_add_two_terms(self):
        self.assertEqual(calc("1+2"), 3.0)

    def test_case3_add_more_terms(self):
        for expression, expected in (("1+2+3", 6.0), ("1+2+3+4", 10.0)):
            with self.subTest(expression=expression, expected=expected):
                self.assertEqual(calc(expression), expected)

    def test_case4_add_and_multiply(self):
        for expression, expected in (("1+2*3", 7.0), ("1*2+3", 5.0)):
            with self.subTest(expression=expression, expected=expected):
                self.assertEqual(calc(expression), expected)

    def test_case5_subtract(self):
        self.assertEqual(calc("1-2"), -1.0)
