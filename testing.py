from polynomials.MultivariatePolynomial import MultivariatePolynomial as MvP
from polynomials.LinearMultivariatePolynomial import LinearMultivariatePolynomial as LMvP
from polyutils import polyoperations as polyop, polyconversion as polycon

a = '9x^2y + 6xy^2 - 5xy + 5'
var = ['x', 'y']

test = MvP(a, var)
print(test.expr_array)
integral = polyop.pr_definite_integral(test.expr_array, test.variables, 'y', 1, 5)
print(integral)
print(polycon.poly_conversion_string(integral, var))
