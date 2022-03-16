from unittest import TestCase

from first_parser import calc


class CalcTestCase(TestCase):
    def test_case1_str_to_float(self):
        self.assertEqual(calc("1"), 1.0)
