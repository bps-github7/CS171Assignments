'''
Programmer: Ben Sehnert
Program: Complex number class
Date: 7/30/2020
Software: Complex Number class


Module Level Docstring: Implements a Complex number class
with overridden magic methods for addition, subtraction,
multiplication and division.
'''

class Complex:
    '''
    Class level docstring: Generates a Complex number
    capable of doing basic arithmetic up to exponentiation
    given a real and imaginary number as arguments to the constructor

    surrounds negative numbers with parenthesis 
    and rounds decimals to 4 significant digits.
    '''
    version = 2.1

    def __init__(self, real, imaginary = 0.0):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        real, img = round(self.real,4), round(self.imaginary,4)
        return '({})+{}i'.format(real, img)\
        if self.real < 0 else '{}+({})i'.format(real, img)\
        if self.imaginary < 0 else '({})+({})i'.format(real, img)\
        if self.real < 0 and self.imaginary < 0\
        else '{}+{}i'.format(real, img)

    #Operator overloading for addition, subtraction, multiplication, true division and power
    def __add__(self, other):
        return Complex(self.real + other.real,
        self.imaginary + other.imaginary)
    
    def __sub__(self, other):
        return Complex(self.real - other.real,
        self.imaginary - other.imaginary)

    def __mul__(self, other):
        return Complex(self.real * other.real\
        - self.imaginary * other.imaginary,
        self.real * other.imaginary + self.imaginary * other.real)

    def __truediv__(self, other):
        return Complex((self.real * other.real +\
        self.imaginary * other.imaginary) /\
        ((other.real ** 2) + (other.imaginary ** 2)),
        (self.imaginary * other.real - self.real * other.imaginary)\
        / ((other.real ** 2) + (other.imaginary ** 2)))

    def __pow__(self, other):
        return Complex(1,0) if other == 0 else self\
        if other == 1 else (self * self ** (other - 1))

if __name__ == '__main__':
    print("Running in standby mode")