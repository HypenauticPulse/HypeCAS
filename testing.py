from linearalgebra.LinearMultivariatePolynomial import LinearMultivariatePolynomial
from linearalgebra.LinearSystem import LinearSystem
from polynomials.Polynomial import Polynomial

# sys.stdout = TracePrints()


# a = "- x + y + y - y - 15z = 15"
# b = "- 5x - y + 12z = 0"
#
# abvars = ["x", "y", "z"]
#
# test = LinearMultivariatePolynomial(a, abvars)
# test2 = LinearMultivariatePolynomial(b, abvars)
# testsystem = LinearSystem(abvars, a, b)
# print(test.exprArray)
# print(testsystem.leftequations, testsystem.rightequations)

a = "x^2 + (5x + 2)x + (x + 2)x"
var = 'x'
test = Polynomial(a, var)
print(test.exprArray)