from Expr import Expr
from Poly import Polynomial
from polyutil import polyconvert as polycon

a = Polynomial("x^2 - 3x + 1", "x")
b = Polynomial("x^3 - x^2", "x")
c = Polynomial("x^2 - 5x = - 6", "x")
print("A zeros: ", a.solve())
print("B zeros: ", b.solve())
print("C zeros: ", c.solve())
