#Ben Sehnert
#7/29/18
#CS 172- HW2 - Complex numbers class
#Professor D. Augenblick

#import statement
import math

#class definition
class Complex:
    def __init__(self, real, imaginary = 0.0):
        self.real = real
        self.imaginary = imaginary
    #returns a string represtation of the object
    def __str__(self):
        return '{}+{}i'.format(self.real, self.imaginary);
    #Operator overloading for addition
    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary);
    #operator overloading for subtraction
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary);
    #operator overloading for multiplication 
    def __mul__(self, other):
        return Complex(self.real * other.real - self.imaginary * other.imaginary, self.real * other.imaginary + self.imaginary * other.real);
    #operator overloading for true divsion
    def __truediv__(self, other):
        #denominator part of the equation
        r = (other.real ** 2)+(other.imaginary ** 2)
        return Complex((self.real * other.real + self.imaginary * other.imaginary) / r, (self.imaginary * other.real - self.real * other.imaginary) / r)
    #operator overloading for exponentiation
    def __pow__(self, other):
        #returns for 0
        if other == 0:
            return Complex(1,0)
        #returns for 1
        elif other == 1:
            return self;
        #return for powers > 1
        else:
            return(self * self ** (other - 1))
    #accessor for real part
    def getReal(self):
        return self.real;
    #accessor for imaginary part
    def getImaginary(self):
        return self.imaginary

#
if __name__ == '__main__':
    print("Running in standby mode");
    #debugging test cases for each operation
    print("{:~^100s}".format("debugging"))
    def spacer():
        print("\n")
    c1 = Complex(4 ,3)
    c2 = Complex(2 ,8)
    spacer()
    print("complex number 1:",c1,"\ncomplex number 2:",c2)
    print("addition:")
    print(c1 + c2)
    spacer()
    print("complex number 1:",c1,"\ncomplex number 2:",c2)
    print("cubed:")
    print(c1 ** 3)
    spacer()
    print("complex number 1:",c1,"\ncomplex number 2:",c2)
    print("subtraction:")
    print(c2 - c1)
    spacer()
    print("complex number 1:",c1,"\ncomplex number 2:",c2)
    print("division:")
    print(c1/c2)
    spacer()
    print("complex number 1:",c1,"\ncomplex number 2:",c2)
    print("multiplication:")
    print(c1 * c2)
else:
    print("Complex class successfully imported");
    