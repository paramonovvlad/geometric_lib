import unittest
from rectangle import area
from rectangle import perimeter
class RectangleTestCase(unittest.TestCase):
    def test_int(self):
        self.assertEqual(area(5,3),15)
    def test_int(self):
        self.assertEqual(perimeter(5,3),16)

    def test_negativenumbers(self):
        with self.assertRaises(ValueError):
            (area(-5, 3))
    def test_negativenumbers(self):
        with self.assertRaises(ValueError):
            (perimeter(-5, 3))


    def test_str(self):
        with self.assertRaises(TypeError):
            (area('bcd','bcd'))
    def test_str(self):
        with self.assertRaises(TypeError):
            (perimeter('bcd', 'bcd'))

if __name__ == '__main__':
    unittest.main()