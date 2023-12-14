import unittest
from circle import area
from circle import perimeter
from math import pi


class CircleTestCase(unittest.TestCase):
    def test_int(self):
        self.assertEqual(area(3),pi*3**2)
        self.assertEqual(perimeter(3),2*pi*3)

    def test_negativenumbers(self):
        self.assertEqual(area(-3),'error')
        self.assertEqual(perimeter(-3),'error')

    def test_str(self):
        self.assertEqual(area('abc'), 'error')
        self.assertEqual(perimeter('abc'), 'error')

if __name__ == '__main__':
    unittest.main()