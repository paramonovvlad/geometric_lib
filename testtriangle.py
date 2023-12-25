import unittest
from triangle import area
from triangle import perimeter
class TriangleTestCase(unittest.TestCase):
    def test_int(self):
        a = 9
        b = 10
        c = 11
        h = 13
        self.assertEqual(area(a,h),a*h/2)
    def test_int(self):
        a = 9
        b = 10
        c = 11
        h = 13
        self.assertEqual(perimeter(a,b,c),a+b+c)

    def test_negativenumbers(self):
        a = -9
        b = 10
        c = -11
        h = 13
        with self.assertRaises(ValueError):
            (area(a,h))

    def test_negativenumbers(self):
        a = -9
        b = 10
        c = -11
        h = 13
        with self.assertRaises(ValueError):
            (perimeter(a, b, c))





if __name__ == '__main__':
    unittest.main()
