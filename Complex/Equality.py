### Programmer: Ben Sehnert
### Program: Equality test (CLI test for complex numbers)
### Date: 7/29/18
### Software: Complex Number Calculator

from Complex import Complex
import sys

def equality(real = 2.0, imaginary = 3.0, k = 10):
    c = Complex(real, imaginary)

    def summation(c,k):
        '''left side of complex number summation'''
        sum, num = Complex(0), 0
        while num <= k: 
            sum += c ** num 
            num += 1
        return sum

    def quotient(c,k):
        '''right side of complex number summation'''
        one = Complex(1.0,0)
        numerator = one - c ** (k + 1)
        denominator = one - c
        return numerator / denominator

    return True if str(summation(c,k)) == str(quotient(c,k)) else False

def main():
    print(equality(real = float(sys.argv[1]), imaginary = float(sys.argv[2]),
    k = float(sys.argv[3])) if len(sys.argv) > 2 else\
    "must pass in all three arguments or none"\
    if (len(sys.argv) < 2 and len(sys.argv) > 1) else equality())

if __name__ == '__main__':
    main()