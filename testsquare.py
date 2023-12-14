import unittest
from square import area
from square import perimeter
class SquareTestCase(unittest.TestCase):
    def test_int(self):
        self.assertEqual(area(7),7*7)
        self.assertEqual(perimeter(7),4*7)

    def test_negativenumbers(self):
        self.assertEqual(area(-7),'error')
        self.assertEqual(perimeter(-7),'error')
    def test_str(self):
        self.assertEqual(area('cde','cde'),'error')
        self.assertEqual(perimeter('cde','cde'),'error')

if __name__ == '__main__':
    unittest.main()