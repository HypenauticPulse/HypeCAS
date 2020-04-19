import polyinput as polyin
import polyconvert as polycon
import polyoperations as polyop
from pyparsing import *
import string, re
from fractions import Fraction





eq = 'x^2 - 3x + 1'
var = 'x'

poly = polycon.poly_format(eq, var)

print(poly)

discriminant = 'NaN'

[zero1, zero2] = polyop.poly_quadratic_zeros(poly)
if zero1 != 'NaN' and zero2 != 'NaN':
    print("First Zero:", zero1)
    print("First Zero Fraction approximation:", Fraction(zero1).limit_denominator())
    print("Second Zero:", zero2)
    print("Second Zero Fraction approximation:", Fraction(zero2).limit_denominator())
