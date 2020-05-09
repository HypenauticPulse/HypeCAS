from polynomials.Equality import Equality
from polynomials.Polynomial import Polynomial
from polynomials.Expression import Expression
from polyutil_mv import polyoperations_mv as polyop
from polynomials.LinearMultivariatePolynomial import LinearMultivariatePolynomial
from polynomials.LinearSystem import LinearSystem

# sys.stdout = TracePrints()


a = "- x + y + y - y - 15z"
b = "- 5x - y + 12z"

abvars = ["x", "y", "z"]

test = LinearMultivariatePolynomial(a, abvars)
test2 = LinearMultivariatePolynomial(b, abvars)
testsystem = LinearSystem(abvars, a, b)
print(test.exprArray)
print(testsystem.equations)
