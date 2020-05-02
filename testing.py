from Equality import Equality
from Expression import Expression
from Polynomial import Polynomial
from polyutil import polyconvert as polycon, polyoperations as polyop
from debugutils.printfinder import TracePrints
import sys

# sys.stdout = TracePrints()

a = Polynomial("x^3 - 5x^2 + 3x + 1", "x")
b = Polynomial("x^3 - x^2", "x")
c = Equality("x^2 - 5x = - 6", "x")
print(a.zeros_new())