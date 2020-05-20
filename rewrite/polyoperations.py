import operator


def poly_consolidate(poly):
    powers = {}
    for coeff, power in poly:
        power = tuple(power)
        powers[power] = powers.get(power, 0) + coeff
    conspoly = [[coeff, list(power)] for power, coeff in powers.items()]
    return conspoly


def poly_sort(poly):
    for i in reversed(range(len(poly[0][1]))):
        poly = sorted(poly, key=lambda x: x[1][i], reverse=True)
    return poly


def poly_remove_zeros(poly):
    zero = []
    for _ in range(len(poly[0][1])):
        zero.append(0.0)
    for i in range(len(poly)):
        if poly[i][0] == 0:
            poly[i] = zero
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


def poly_addition(poly1, poly2):
    result = poly_sort(poly_consolidate(poly1 + poly2))
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
