import math
import unittest

def calcCucum(r):
    return r*2*math.pi

# print(calcCucum(5))

class TestMycode(unittest.TestCase):
    def test_circum(self):
        actual = calcCucum(5)
        self.assertEqual(actual, 31.41592653589793)

    def test_circmzero(self):
        actual = calcCucum(0)
        self.assertEqual(actual, 0)

    # def test_circumInvalid(self):
    #     self.assertRaises(calcCucum("Frank"))


unittest.main()
        