def poly_consolidate(poly):
    powers = {}
    for coeff, power in poly:
        powers[power] = powers.get(power, 0) + coeff
    conspoly = [[coeff, power] for power, coeff in powers.items()]
    return conspoly


def poly_degree(poly):
    degrees = []
    for i in poly:
        degrees.append(i[1])

    return max(degrees)


def poly_remove_zeros(poly):
    for i in range(len(poly)):
        if poly[i][0] == 0:
            poly[i] = [0, 0]
    return poly


def poly_pop_zeros(poly):
    for i in range(len(poly)):
        if poly[i] == [0, 0]:
            poly.pop(i)
    return poly


def poly_sort(poly):
    return sorted(poly, key=lambda x: x[1], reverse=True)


def poly_leading_coeff(poly):
    poly = poly_sort(poly)
    degree = poly_degree(poly)
    lc = 0
    for i in poly:
        if i[1] == degree:
            lc = i[0]
    return lc


def poly_addition(poly1, poly2):
    result = poly_sort(poly_consolidate(poly1 + poly2))
    return result


def poly_subtraction(poly1, poly2):
    for i in range(len(poly2)):
        poly2[i][0] = - poly2[i][0]
    result = poly_sort(poly_consolidate(poly1 + poly2))
    return result


def poly_scalar_multiplication(poly, scalar):
    result = []
    for i in poly:
        result.append([i[0] * scalar, i[1]])
    return poly_sort(poly_consolidate(result))


def poly_poly_multiplication(poly1, poly2):
    result = []
    for i in poly1:
        for j in poly2:
            result.append([i[0] * j[0], i[1] + j[1]])
    return poly_sort(poly_consolidate(result))


def poly_scalar_division(poly, scalar):
    result = []
    for i in poly:
        result.append([i[0] / scalar, i[1]])
    return poly_sort(poly_consolidate(result))


def poly_poly_division(poly1, poly2):
    count = 0
    for i in poly2:
        if i == [0, 0]:
            count += 1
    if count == len(poly2):
        return -1, -1
    else:
        quotient = []
        remainder = poly1
        divisordegree = poly_degree(poly2)
        divisorlc = poly_leading_coeff(poly2)
        i = 0
        while poly_degree(remainder) >= divisordegree:
            s = [poly_leading_coeff(remainder) / divisorlc, poly_degree(remainder) - divisordegree]
            quotient.append(s)
            remainder = poly_subtraction(remainder, poly_poly_multiplication([s], poly2))
            remainder = poly_remove_zeros(remainder)
            i += 1
        return quotient, remainder
