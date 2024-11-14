import unittest
from calclutor import calc
class TestCalculator(unittest.TestCase):
    def test_add(self):
        result =calc.add(4,6)
        self.assertEqual(result,10)
if _name== 'main_':
    unittest.main