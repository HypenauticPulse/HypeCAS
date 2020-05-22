import polyutils.polyoperations as polyop


def find_parens(s):
    toret = []
    pstack = []

    for i, c in enumerate(s):
        if c == '(':
            pstack.append(i)
        elif c == ')':
            if len(pstack) == 0:
                raise IndexError("No matching closing parens at: " + str(i))
            toret.append([pstack.pop(), i])

    if len(pstack) > 0:
        raise IndexError("No matching opening parens at: " + str(pstack.pop()))

    return toret


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
    if a[0] != '-' and a[0] != '+':
        a = ['+'] + a

    j = 0
    while j < len(a):
        a[j] = a[j] + a[j + 1]
        a.pop(j + 1)
        j += 1

    coeff_power = []
    for k in range(len(a)):
        temp = a[k]
        indices = []
        powers = []
        for m in variables:
            indices.append(temp.find(m))
        if all(index == -1 for index in indices):
            for _ in variables:
                powers.append(0.0)
            coefficient = temp
        else:
            first_index = -1
            for idx, varIndex in enumerate(indices):
                if varIndex != -1:
                    if first_index == -1:
                        first_index = varIndex
                    if idx != len(indices) - 1:
                        next_index = len(temp)
                        for nxtIdx in indices[idx + 1:]:
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


def parse_expr(expression, variables):
    print('called')
    paren_indices = find_parens(expression)
    print('parenthesis indices:', paren_indices)
    result = []
    if paren_indices:
        i = len(paren_indices) - 1
        while i >= 0:
            if i == len(paren_indices) - 1:
                print('last index set')
                left = paren_indices[i][0] + 1
                right = paren_indices[i][1]
                inside = expression[left:right]
                print('inside:', inside)
                inside = parse_expr(inside, variables)
                print('inside (parsed):', inside)
                if left - 1 == 0:
                    if right == len(expression) - 1:
                        result = inside
                    else:
                        if expression[right + 1] == ' ':
                            outside = expression[right + 1: len(expression)]
                            print('outside:', outside)
                            outside = parse_expr(outside, variables)
                            print('outside (parsed)', outside)
                            result = polyop.poly_addition(inside, outside)
                        else:
                            multiplier_end = expression.find(' ', right)
                            if multiplier_end == -1:
                                multiplier_end = len(expression)
                            multiplier = expression[right + 1:multiplier_end]
                            print('multiplier:', multiplier)
                            multiplier = parse_expr(multiplier, variables)
                            print('multiplier (parsed):', multiplier)
                            inside = polyop.poly_poly_multiplication(inside, multiplier)
                            print('multiplied inside:', inside)
                            if multiplier_end == len(expression):
                                result = inside
                            else:
                                outside = expression[multiplier_end:len(expression)]
                                print('outside:', outside)
                                outside = parse_expr(outside, variables)
                                print('outside (parsed)', outside)
                                result = polyop.poly_addition(inside, outside)

                else:
                    if right == len(expression) - 1:
                        if expression[left - 2] == ' ':
                            if expression[left - 3] == '-':
                                inside = polyop.poly_scalar_multiplication(inside, -1.0)
                            print('inside (after negative check):', inside)
                            outside = expression[0:left - 4]
                            print('outside:', outside)
                            outside = parse_expr(outside, variables)
                            print('outside (parsed)', outside)
                            result = polyop.poly_addition(inside, outside)
                        else:
                            multiplier_start = expression.rfind(' ', 0, left - 1)
                            if multiplier_start == -1:
                                multiplier_start = 0
                            else:
                                multiplier_start -= 1
                            multiplier = expression[multiplier_start:left - 1]
                            print('multiplier:', multiplier)
                            multiplier = parse_expr(multiplier, variables)
                            print('multiplier (parsed):', multiplier)
                            inside = polyop.poly_poly_multiplication(inside, multiplier)
                            print('multiplied inside:', inside)
                            if multiplier_start == 0:
                                result = inside
                            else:
                                outside = expression[0:multiplier_start - 1]
                                print('outside:', outside)
                                outside = parse_expr(outside, variables)
                                print('outside (parsed)', outside)
                                result = polyop.poly_addition(inside, outside)
                    else:
                        if expression[left - 2] == ' ' and expression[right + 1] == ' ':
                            if expression[left - 3] == '-':
                                inside = polyop.poly_scalar_multiplication(inside, -1.0)
                            print('inside (after negative check):', inside)
                            outside = expression[0:left - 4] + expression[right + 1:len(expression)]
                            print('outside:', outside)
                            outside = parse_expr(outside, variables)
                            print('outside (parsed)', outside)
                            result = polyop.poly_addition(inside, outside)
                        elif expression[left - 2] == ' ' and expression[right + 1] != ' ':
                            if expression[left - 3] == '-':
                                inside = polyop.poly_scalar_multiplication(inside, -1.0)
                            print('inside (after negative check):', inside)
                            multiplier_end = expression.find(' ', right)
                            if multiplier_end == -1:
                                multiplier_end = len(expression)
                            multiplier = expression[right + 1:multiplier_end]
                            print('multiplier:', multiplier)
                            multiplier = parse_expr(multiplier, variables)
                            print('multiplier (parsed):', multiplier)
                            inside = polyop.poly_poly_multiplication(inside, multiplier)
                            print('multiplied inside:', inside)
                            if multiplier_end == len(expression):
                                outside = expression[0:left - 4]
                            else:
                                outside = expression[0:left - 4] + expression[multiplier_end:len(expression)]
                            print('outside:', outside)
                            outside = parse_expr(outside, variables)
                            print('outside (parsed)', outside)
                            result = polyop.poly_addition(inside, outside)
                        elif expression[left - 2] != ' ' and expression[right + 1] == ' ':
                            multiplier_start = expression.rfind(' ', 0, left - 1)
                            if multiplier_start == -1:
                                multiplier_start = 0
                            else:
                                multiplier_start -= 1
                            multiplier = expression[multiplier_start:left - 1]
                            print('multiplier:', multiplier)
                            multiplier = parse_expr(multiplier, variables)
                            print('multiplier (parsed):', multiplier)
                            inside = polyop.poly_poly_multiplication(inside, multiplier)
                            print('multiplied inside:', inside)
                            if multiplier_start == 0:
                                result = inside
                            else:
                                outside = expression[0:multiplier_start - 1] + expression[right + 1: len(expression)]
                                print('outside:', outside)
                                outside = parse_expr(outside, variables)
                                print('outside (parsed)', outside)
                                result = polyop.poly_addition(inside, outside)
                        elif expression[left - 2] != ' ' and expression[right + 1] != ' ':
                            multiplier_left_start = expression.rfind(' ', 0, left - 1)
                            if multiplier_left_start == -1:
                                multiplier_left_start = 0
                            else:
                                multiplier_left_start -= 1
                            multiplier_right_end = expression.find(' ', right)
                            if multiplier_right_end == -1:
                                multiplier_right_end = len(expression)
                            multiplier_left = expression[multiplier_left_start:left - 1]
                            multiplier_right = expression[right + 1:multiplier_right_end]
                            print('left multiplier:', multiplier_left)
                            print('right multiplier:', multiplier_right)
                            multiplier_left = parse_expr(multiplier_left, variables)
                            multiplier_right = parse_expr(multiplier_right, variables)
                            print('left multiplier (parsed):', multiplier_left)
                            print('right multiplier (parsed):', multiplier_right)
                            inside = polyop.poly_poly_multiplication(inside, multiplier_left)
                            inside = polyop.poly_poly_multiplication(inside, multiplier_right)
                            print('multiplied inside:', inside)
                            if multiplier_left_start == 0 and multiplier_right_end == len(expression):
                                result = inside
                            elif multiplier_left_start != 0 and multiplier_right_end == len(expression):
                                outside = expression[0:multiplier_left_start - 1]
                                print('outside:', outside)
                                outside = parse_expr(outside, variables)
                                print('outside (parsed):', outside)
                                result = polyop.poly_addition(inside, outside)
                            elif multiplier_left_start == 0 and multiplier_right_end != len(expression):
                                outside = expression[multiplier_right_end:len(expression)]
                                print('outside:', outside)
                                outside = parse_expr(outside, variables)
                                print('outside (parsed)', outside)
                                result = polyop.poly_addition(inside, outside)
                            elif multiplier_left_start != 0 and multiplier_right_end != len(expression):
                                outside = expression[0:multiplier_left_start - 1] + expression[multiplier_right_end:len(expression)]
                                print('outside:', outside)
                                outside = parse_expr(outside, variables)
                                print('outside (parsed)', outside)
                                result = polyop.poly_addition(inside, outside)

            i -= 1
    else:
        print('no parentheses')
        result = parse_np(expression, variables)
    print("returning", result)
    return result


expr = "x^2 - x(5x + x(5x^2 + 2)) + 5"
var = ['x', 'y', 'z']

print('final result:', parse_expr(expr, var))

# TODO: add final case for multipliers (when the parenthesis set is at neither the start or end of the expression)
# TODO: recursive function for multiplied parentheses

# Code snippet for multiplied parentheses

# elif left - 2 == paren_indices[i - 1][1]:
#     print('multiplied parentheses')
#     multiplier_left = paren_indices[i - 1][0] + 1
#     multiplier_right = paren_indices[i - 1][1]
#     multiplier = expression[multiplier_left:multiplier_right]
#     print('multiplier:', multiplier)
#     multiplier = parse_expr(multiplier, variables)
#     print('multiplier (parsed):', multiplier)
#     inside = polyop.poly_poly_multiplication(inside, multiplier)
#     print('multiplied inside:', inside)
#     if multiplier_left == 0:
#         result = inside
#     else:
#         outside = expression[0:m]
