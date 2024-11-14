import unittest
from Add import add

class TestCalculator(unittest.TestCase):
    def test_add(self):
        result = add.add(4, 6)
        self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()
