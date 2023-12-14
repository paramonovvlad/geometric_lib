import unittest
from circle import area
from circle import perimeter
from math import pi


class CircleTestCase(unittest.TestCase):
    def test_int(self):
        self.assertEqual(area(3),round(pi*3**2, 2))

    def test_int(self):

        self.assertEqual(perimeter(3),round(2*pi*3, 2))


    def test_negativenumbers(self):
        with self.assertRaises(ValueError):
            area(-3)

    def test_negativenumbers(self):
        with self.assertRaises(ValueError):
            perimeter(-3)


    def test_str(self):
        with self.assertRaises(TypeError):
            area('abc')

    def test_str(self):
        with self.assertRaises(TypeError):
            perimeter('abc')


if __name__ == '__main__':
    unittest.main()