from polynomials.MultivariatePolynomial import MultivariatePolynomial as MvP
from polynomials.LinearMultivariatePolynomial import LinearMultivariatePolynomial as LMvP
from polyutils import polyoperations as polyop

a = 'x + 9y - 15z + 5'
var = ['x', 'y', 'z']

test = LMvP(a, var)
print(test.expr_array)
print(polyop.poly_leading_coeff(test.expr_array))
print(polyop.poly_find_coefficient(test.expr_array, [0, 2, 0]))

print(test.evaluate([1, 2, 1]))