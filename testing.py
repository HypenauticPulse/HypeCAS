import polyinput as polyin
import polyconvert as polycon
import polyoperations as polyop

# [eq, var] = polyin.get_input()
# poly = polycon.poly_conversion_array(eq, var)
# print(polyop.poly_scalar_multiplication(poly, 5))


[eq1, eq2, var] = polyin.get_input_dual()
poly1 = polycon.poly_conversion_array(eq1, var)
poly2 = polycon.poly_conversion_array(eq2, var)

quotient = []
remainder = poly1
divisorDegree = polyop.poly_degree(poly2)
divisorLC = polyop.poly_leading_coeff(poly2)
i = 0
while polyop.poly_degree(remainder) >= divisorDegree:
    s = [polyop.poly_leading_coeff(remainder)/divisorLC, polyop.poly_degree(remainder) - divisorDegree]
    quotient.append(s)
    remainder = polyop.poly_subtraction(remainder, polyop.poly_poly_multiplication([s], poly2))
    remainder = polyop.poly_remove_zeros(remainder)
    i += 1

# return quotient, remainder
