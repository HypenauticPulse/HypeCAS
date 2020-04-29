import polyinput as polyin
import polyconvert as polycon
import polyoperations as polyop
from pyparsing import *
import string, re
from fractions import Fraction





eq = 'x^2 - 3x + 1'
var = 'x'
a = polycon.poly_conversion_array("2x^2", var)
print(a)
b = polycon.poly_conversion_string(a)
print(b)
