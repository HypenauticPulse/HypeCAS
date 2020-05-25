def poly_consolidate(poly):
    powers = {}
    for coeff, power in poly:
        power = tuple(power)
        powers[power] = powers.get(power, 0) + coeff
    conspoly = [[coeff, list(power)] for power, coeff in powers.items()]
    return conspoly


def poly_degree(poly):
    degree = 0
    for i in poly:
        if sum(i[1]) > degree:
            degree = sum(i[1])
    return degree


def poly_find_degree(poly, variable):
    degree = 0
    for i in poly:
        if i[1][variable - 1] > degree:
            degree = i[1][variable - 1]
    return degree


def poly_remove_zeros(poly):
    zero = []
    for _ in range(len(poly[0][1])):
        zero.append(0.0)
    for i in range(len(poly)):
        if poly[i][0] == 0:
            poly[i] = [0, zero]
    return poly


def poly_pop_zeros(poly):
    zero = []
    for _ in range(len(poly[0][1])):
        zero.append(0.0)
    poly = poly_remove_zeros(poly)
    i = 0
    while i < len(poly):
        if poly[i] == [0, zero]:
            poly.pop(i)
        else:
            i += 1
    return poly


def poly_sort(poly):
    for i in reversed(range(len(poly[0][1]))):
        poly = sorted(poly, key=lambda x: x[1][i], reverse=True)
    return poly


def poly_leading_coeff(poly):
    poly = poly_sort(poly)
    return poly[0][0]


def poly_find_coefficient(poly, power):
    coeff = 0
    found = 0
    i = 0
    while i < len(poly) and not found:
        if poly[i][1] == power:
            coeff = poly[i][0]
            found = 1
        i += 1

    return coeff


# Might move this to univariate polynomials. Depending on how zeros are implemented.
def poly_quadratic_zeros(poly):
    if poly_degree(poly) == 2:
        a = poly_find_coefficient(poly, 2)
        b = poly_find_coefficient(poly, 1)
        c = poly_find_coefficient(poly, 0)
        print(a, b, c)
        discriminant = b ** 2 - 4 * a * c
        print(discriminant)
        if discriminant > 0:
            zero1 = (-b + discriminant ** 0.5) / (2 * a)
            zero2 = (-b - discriminant ** 0.5) / (2 * a)
        else:
            print("The zeroes are complex")
            zero1 = 'C'
            zero2 = 'C'
    else:
        print("The polynomials is not quadratic")
        zero1 = 'NaN'
        zero2 = 'NaN'

    return zero1, zero2


def poly_addition(poly1, poly2):
    result = poly_sort(poly_consolidate(poly1 + poly2))
    return poly_pop_zeros(poly_sort(poly_consolidate(result)))


def poly_subtraction(poly1, poly2):
    ply2 = []
    for i in range(len(poly2)):
        ply2.append([- poly2[i][0], poly2[i][1]])
    result = poly_sort(poly_consolidate(poly1 + ply2))
    return poly_pop_zeros(poly_sort(poly_consolidate(result)))


def poly_scalar_multiplication(poly, scalar):
    result = []
    for i in poly:
        result.append([i[0] * scalar, i[1]])
    return poly_pop_zeros(poly_sort(poly_consolidate(result)))


def poly_poly_multiplication(poly1, poly2):
    result = []
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            power = []
            for k in range(len(poly1[0][1])):
                power.append(poly1[i][1][k] + poly2[j][1][k])
            result.append([poly1[i][0] * poly2[j][0], power])
    return poly_pop_zeros(poly_sort(poly_consolidate(result)))


def poly_scalar_division(poly, scalar):
    result = []
    for i in poly:
        result.append([i[0] / scalar, i[1]])
    return poly_pop_zeros(poly_sort(poly_consolidate(result)))


def poly_poly_division(poly1, poly2):
    quotient = []
    remainder = poly1
    divisor_degree = poly_find_degree(poly2, 1)
    divisor_lc = poly_leading_coeff(poly2)
    while poly_find_degree(remainder, 1) >= divisor_degree:
        remainder = poly_remove_zeros(remainder)
        s_coeff = poly_leading_coeff(remainder) / divisor_lc
        s_degree = []
        for i in range(len(remainder[1])):
            s_degree.append(remainder[0][1][i] - poly2[0][1][i])
        s = [s_coeff, s_degree]
        quotient.append(s)
        remainder = poly_subtraction(remainder, poly_poly_multiplication([s], poly2))
    return quotient, remainder
