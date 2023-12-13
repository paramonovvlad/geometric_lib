import unittest
from circle import area
from circle import perimeter
from rectangle import area
from rectangle import perimeter
from square import area
from square import perimeter
from triangle import area
from triangle import perimeter
from math import pi

class CircleTestCase(unittest.TestCase):
    def test_int(self):
        self.assertEqual(area(3),pi)
        self.assertEqual(perimeter(3),2*pi*3)

    def test_negativenumbers(self):
        self.assertEqual(area(-3),pi*-3**2)
        self.assertEqual(perimeter(-3),2*pi*-3)

    def test_str(self):
        self.assertEqual(area('abc'), pi * 'abc' ** 2)
        self.assertEqual(perimeter('abc'), 2 * pi * 'abc')

class RectangleTestCase(unittest.TestCase):
    def test_int(self):
        self.assertEqual(area(5,3),5*3)
        self.assertEqual(perimeter(5,3),2*(5+3))

    def test_negativenumbers(self):
        self.assertEqual(area(-5,3),-5*3)
        self.assertEqual(perimeter(-5,3),2*(-5+3))

    def test_str(self):
        self.assertEqual(area('bcd','bcd'),'bcd'*'bcd')
        self.assertEqual(perimeter('bcd','bcd'),2*('bcd'+'bcd'))


class SquareTestCase(unittest.TestCase):
    def test_int(self):
        self.assertEqual(area(7),7*7)
        self.assertEqual(perimeter(7),4*7)

    def test_negativenumbers(self):
        self.assertEqual(area(-7),-7*-7)
        self.assertEqual(perimeter(-7),4*-7)
    def test_str(self):
        self.assertEqual(area('cde','cde'),'cde'*'cde')
        self.assertEqual(perimeter('cde','cde'),4*('cde'+'cde'))

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
        self.assertEqual(area(a,h),a*h/2)
        self.assertEqual(perimeter(a,b,c),a+b+c)
    def test_str(self):
        a = 'def'
        b = 'def'
        c = 'def'
        h = 'def'
        self.assertEqual(area('def','def'),'def'*'def'/2)
        self.assertEqual(perimeter('def','def','def'),'def'+'def'+'def')
