import unittest

from decimal_to_roman_converter import decimal_to_roman


class DecimalToRomanTest(unittest.TestCase):

    def testInvalidEntryString(self):
        self.assertRaises(TypeError, decimal_to_roman, 'invalid')


if __name__ == '__main__':
    unittest.main()