import unittest
from square import area
from square import perimeter
class SquareTestCase(unittest.TestCase):
    def test_int(self):
        self.assertEqual(area(7),7*7)
    def test_int(self):
        self.assertEqual(perimeter(7),4*7)

    def test_negativenumbers(self):
        with self.assertRaises(ValueError):
            (area(-7))

    def test_negativenumbers(self):
        with self.assertRaises(ValueError):
            (perimeter(-7))
    def test_str(self):
        with self.assertRaises(TypeError):
            (area('cde','cde'))

    def test_str(self):
        with self.assertRaises(TypeError):
            (perimeter('cde','cde'))
if __name__ == '__main__':
    unittest.main()