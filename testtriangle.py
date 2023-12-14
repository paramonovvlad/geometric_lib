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
        self.assertEqual(perimeter(a,b,c),a+b+c)

    def test_negativenumbers(self):
        a = -9
        b = 10
        c = -11
        h = 13
        self.assertEqual(area(a,h),'error')
        self.assertEqual(perimeter(a,b,c),'error')
    def test_str(self):
        a = 'def'
        b = 'def'
        c = 'def'
        h = 'def'
        self.assertEqual(area('def','def'),'error')
        self.assertEqual(perimeter('def','def','def'),'error')

if __name__ == '__main__':
    unittest.main()
