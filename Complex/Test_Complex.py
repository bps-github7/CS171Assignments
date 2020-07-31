### Programmer: Ben Sehnert
### Program: Unit test for Complex.py module
### Date: 7/30/2020
### Software: Complex Number Calculator

'''
Module Docstring: implements unit tests for Complex numbers class
'''

import unittest
from Complex import Complex

class Test_Complex(unittest.TestCase):
    '''
Class Docstring: provides unittests for Complex class
Assuring the reliability of the following overridden magic methods
- __add__ | given c1 + c2 expected return value: 6+11i
- __sub__ | given c1 - c2 expected return value: 2+(-5)i
- __mul__ | given c1 * c2 expected return value: (-16)+38i
- __div__ | given c1 / c2 expected return value: 0.4705+(-0.3823)i
- __pow__ | given c1 ** 3 expected return value: (-44)+117i
    '''
    def test_addition(self, c1 = Complex(4,3), c2 = Complex(2,8)):
        self.assertEqual(str(c1 + c2), '6+11i')
    
    def test_subtraction(self, c1 = Complex(4,3), c2 = Complex(2,8)):
        self.assertEqual(str(c1 - c2), '2+(-5)i')

    def test_multiplication(self, c1 = Complex(4,3), c2 = Complex(2,8)):
        self.assertEqual(str(c1 * c2), '(-16)+38i')

    def test_division(self, c1 = Complex(4,3), c2 = Complex(2,8)):
        self.assertEqual(str(c1 / c2), '0.4706+(-0.3824)i')
    
    def test_cube(self, c1 = Complex(4,3)):
        self.assertEqual(str(c1 ** 3), '(-44)+117i')

###for visual confirmation
def addition(c1 = Complex(4,3), c2 = Complex(2,8)):
    return c1 + c2

def subtraction(c1 = Complex(4,3), c2 = Complex(2,8)):
    return c1 - c2

def multiplication(c1 = Complex(4,3), c2 = Complex(2,8)):
    return c1 * c2

def division(c1 = Complex(4,3), c2 = Complex(2,8)):
    return c1 / c2

def cube(c1 = Complex(4,3)):
    return c1 ** 3

def main():
    print("{:~^100s}".format("Testing"))
    print("addition: ",addition())
    print("subtraction: ",subtraction())
    print("multiplication: ",multiplication())
    print("division: ",division())
    print("cubed: ",cube())

if __name__ == '__main__':
    # unittest.main()
    main()

