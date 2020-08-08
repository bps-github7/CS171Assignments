"""
Programmer: Ben Sehnert
Program: Equality test (CLI test for complex numbers)
Date: 7/29/18
Software: Complex Number Calculator

takes 3 arguments, first two floats and last an integer

Calculated sum:

sigma (0,k) sum=0, num=0, n+1 : sum += Complex(2.0, 3.0) ^ num
where the real and imaginary arguments to Complex constructor 
are overrideen by the first and second cmd line arguments (if provided).

quoitent: 

(Complex(1.0, 0) - c ** (k + 1))/(Complex(1.0, 0) - c)

Developer notes:

Reaches recursion depth limit when k reaches 1000 
(993 exactly), for unknown reasons.
"""

from Complex import Complex
import sys

def equality(real = 2.0, imaginary = 3.0, k = 10):
    c = Complex(real, imaginary)

    def summation(c,k):
        sum, num = Complex(0), 0
        for i in range(num, k+1): sum += c ** i
        return sum

    def quotient(c,k, parens = Complex(1.0,0)):
        numerator = parens - c ** (k + 1)
        denominator = parens - c
        return numerator / denominator

    return True if str(summation(c,k)) == str(quotient(c,k)) else False

def main():
    #if only the script executable was invoked, use only default arguments
    if len(sys.argv) == 1:
        print(equality())
        return 1
    try:
        real, imaginary, k = float(sys.argv[1]),
        float(sys.argv[2]), int(sys.argv[3])
    except IndexError:
        #copes with various amounts of variables provided
        if len(sys.argv) == 2:
            real = float(sys.argv[1])
        elif len(sys.argv) == 3:
            real, imaginary = float(sys.argv[1]), float(sys.argv[2])
        # Cautionary measure
        elif len(sys.argv) == 4:
            real, imaginary, k = float(sys.argv[1]),
            float(sys.argv[2]), int(sys.argv[3])
    # Another precaution
    if (real, imaginary, k):
        print(equality(real, imaginary, k))
        return 1

if __name__ == '__main__':
    main()
