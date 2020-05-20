import rewrite.polyoperations as polyop


def num_parse(expression):
    if expression == '-' or expression == '+':
        expression += '1'
        expression = float(expression)
    elif '/' in expression:
        coeff_temp = expression.split('/')
        expression = float(coeff_temp[0]) / float(coeff_temp[1])
    else:
        expression = float(expression)
    return expression


def parse_np(expression, variables):
    a = expression.split()

    trigger = 0
    i = 0
    if a[0] != '-':
        a = ['+'] + a

    j = 0
    while j < len(a):
        a[j] = a[j] + a[j + 1]
        a.pop(j + 1)
        j += 1

    coeff_power = []
    for k in range(len(a)):
        temp = a[k]
        indexes = []
        powers = []
        for m in variables:
            indexes.append(temp.find(m))
        if all(index == -1 for index in indexes):
            for _ in variables:
                powers.append(0.0)
            coefficient = temp
        else:
            first_index = -1
            for idx, varIndex in enumerate(indexes):
                if varIndex != -1:
                    if first_index == -1:
                        first_index = varIndex
                    if idx != len(indexes) - 1:
                        next_index = len(temp)
                        for nxtIdx in indexes[idx + 1:]:
                            if next_index == len(temp):
                                if nxtIdx != -1:
                                    next_index = nxtIdx
                        if next_index != len(temp):
                            if varIndex + 1 != next_index:
                                powers.append(num_parse(temp[varIndex + 2:next_index]))
                            else:
                                powers.append(1.0)
                        else:
                            if varIndex != len(temp) - 1:
                                powers.append(num_parse(temp[varIndex + 2: len(temp)]))
                            else:
                                powers.append(1.0)
                    else:
                        if varIndex != len(temp) - 1:
                            powers.append(num_parse(temp[varIndex + 2: len(temp)]))
                        else:
                            powers.append(1.0)
                else:
                    powers.append(0.0)
            coefficient = temp[0:first_index]
        coefficient = num_parse(coefficient)
        coeff_power.append([coefficient, powers])

    return coeff_power


expr = "y + x^2 + y^2 + 2x^2"
expr2 = "x^2 + 5y^2"
var = ['x', 'y']
test = parse_np(expr, var)
test2 = parse_np(expr2, var)

print(test)
print(polyop.poly_consolidate(test))
print(polyop.poly_sort(polyop.poly_consolidate(test)))
print(polyop.poly_scalar_multiplication(test, -1))
print(polyop.poly_poly_multiplication(test, test2))
