from math import *
from numpy.lib.scimath import sqrt
def roots(a,b,c):
    return (-b+sqrt(b**2-4*a*c))/(2*a), (-b-sqrt(b**2-4*a*c))/(2*a)

def test_roots_float(a=1,b=3,c=1):
    return roots(a,b,c)
print (test_roots_float(a=1, b=3, c=1))

def test_roots_complex(a=10,b=6,c=4):
    return roots(a,b,c)
print (test_roots_complex(a=10, b=6, c=4))
print (roots(a=5, b=3, c=1))






