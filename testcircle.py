import unittest
from circle import area
from circle import perimeter
from math import pi


class CircleTestCase(unittest.TestCase):
    def test_int(self):
        self.assertAlmostEqual(area(3),28.26, delta=0.01)
    def test_int(self):
        self.assertAlmostEqual(perimeter(3),18.84, delta=0.01)

    def test_negativenumbers(self):
        with self.assertRaises(ValueError):
            (area(-3))
    def test_negativenumbers(self):
        with self.assertRaises(ValueError):
            (perimeter(-3))


    def test_str(self):
        with self.assertRaises(TypeError):
            (area('abc'))

    def test_str(self):
        with self.assertRaises(TypeError):
            (perimeter('abc'))

if __name__ == '__main__':
    unittest.main()