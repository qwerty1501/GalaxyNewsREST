from django.test import TestCase
from .operator import operator


class OperatorTestCase(TestCase):
    def test_multiply(self):
        result = operator(1, 2, '*')
        self.assertEqual(5, result)