#Ben Sehnert
#7/29/18
#CS 172- HW2 - Complex numbers class
#Professor D. Augenblick

# import statements for complex class and sys module
from Complex import *
import sys


#function definitions
def a(c,k):
    '''
left side of complex number summation
    '''
    #initilizes complex object
    sum = Complex(0)
    num = 0
    #tests is summation is complete
    while num <= k: 
        sum += c ** num 
        num += 1
    return sum

def b(c,k):
    '''
right side of complex number summation
    '''
    one = Complex(1.0,0)
    numerator = one - c ** (k + 1)
    denominator = one - c
    return numerator / denominator 

#variable definitions
c = Complex(2.0,3.0)
k = 10
#user Interface
print("Result from sum:",a(c,k))
print("Result from quotient:",b(c,k))
print("Equality:",a(c,k),"=",b(c,k))