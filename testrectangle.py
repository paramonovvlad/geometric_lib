import unittest
from rectangle import area
from rectangle import perimeter
class RectangleTestCase(unittest.TestCase):
    def test_int(self):
        self.assertEqual(area(5,3),'error')
        self.assertEqual(perimeter(5,3),'error')

    def test_negativenumbers(self):
        self.assertEqual(area(-5,3),'error')
        self.assertEqual(perimeter(-5,3),'error')

    def test_str(self):
        self.assertEqual(area('bcd','bcd'),'error')
        self.assertEqual(perimeter('bcd','bcd'),'error')

if __name__ == '__main__':
    unittest.main()