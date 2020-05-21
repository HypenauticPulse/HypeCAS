import rewrite.polyoperations as polyop


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
    paren_indices = find_parens(expression)
    result = []
    if paren_indices:
        i = len(paren_indices) - 1
        while i >= 0:
            if i == len(paren_indices) - 1:
                left = paren_indices[i][0] + 1
                right = paren_indices[i][1]
                inside = expression[left:right]
                inside = parse_expr(inside, variables)
                if left - 1 == 0:
                    if right == len(expression) - 1:
                        result = inside
                    else:
                        if expression[right + 1] == ' ':
                            outside = expression[right + 1: len(expression)]
                            outside = parse_expr(outside, variables)
                            result = polyop.poly_addition(inside, outside)
                        else:
                            multiplier_end = expression.find(' ', right)
                            if multiplier_end == -1:
                                multiplier_end = len(expression)
                            multiplier = expression[right + 1:multiplier_end]
                            multiplier = parse_expr(multiplier, variables)
                            inside = polyop.poly_poly_multiplication(inside, multiplier)
                            if multiplier_end == len(expression):
                                result = inside
                            else:
                                outside = expression[multiplier_end:len(expression)]
                                outside = parse_expr(outside, variables)
                                result = polyop.poly_addition(inside, outside)

                else:
                    if right == len(expression) - 1:
                        if expression[left - 2] == ' ':
                            if expression[left - 3] == '-':
                                inside = polyop.poly_scalar_multiplication(inside, -1.0)
                            outside = expression[0:left - 4]
                            outside = parse_expr(outside, variables)
                            result = polyop.poly_addition(inside, outside)
                        elif expression[left - 2] == ')':
                            j = i - 1
                            paren_multiplier_start = left - 1
                            while j >= 0:
                                if paren_indices[j][1] == paren_indices[j + 1][0] - 1:
                                    paren_multiplier_start = paren_indices[j][0]
                                j -= 1
                            paren_multiplier = expression[paren_multiplier_start:left - 1]
                            paren_multiplier = parse_expr(paren_multiplier, variables)
                            inside = polyop.poly_poly_multiplication(inside, paren_multiplier)
                            if paren_multiplier_start == 0:
                                result = inside
                            else:
                                if expression[paren_multiplier_start - 1] == ' ':
                                    if expression[paren_multiplier_start - 2] == '-':
                                        inside = polyop.poly_scalar_multiplication(inside, -1.0)
                                    outside = expression[0:paren_multiplier_start - 3]
                                    outside = parse_expr(outside, variables)
                                    result = polyop.poly_addition(inside, outside)
                                else:
                                    multiplier_start = expression.rfind(' ', 0, paren_multiplier_start)
                                    if multiplier_start == -1:
                                        multiplier_start = 0
                                    else:
                                        multiplier_start -= 1
                                    multiplier = expression[multiplier_start:paren_multiplier_start]
                                    multiplier = parse_expr(multiplier, variables)
                                    inside = polyop.poly_poly_multiplication(inside, multiplier)
                                    if multiplier_start == 0:
                                        result = inside
                                    else:
                                        outside = expression[0:multiplier_start - 1]
                                        outside = parse_expr(outside, variables)
                                        result = polyop.poly_addition(inside, outside)
                        else:
                            multiplier_start = expression.rfind(' ', 0, left - 1)
                            if multiplier_start == -1:
                                multiplier_start = 0
                            else:
                                multiplier_start -= 1
                            multiplier = expression[multiplier_start:left - 1]
                            multiplier = parse_expr(multiplier, variables)
                            inside = polyop.poly_poly_multiplication(inside, multiplier)
                            if multiplier_start == 0:
                                result = inside
                            else:
                                outside = expression[0:multiplier_start - 1]
                                outside = parse_expr(outside, variables)
                                result = polyop.poly_addition(inside, outside)
                    else:
                        if expression[left - 2] == ')':
                            j = i - 1
                            paren_multiplier_start = left - 1
                            while j >= 0:
                                if paren_indices[j][1] == paren_indices[j + 1][0] - 1:
                                    paren_multiplier_start = paren_indices[j][0]
                                j -= 1
                            paren_multiplier = expression[paren_multiplier_start:left - 1]
                            paren_multiplier = parse_expr(paren_multiplier, variables)
                            inside = polyop.poly_poly_multiplication(inside, paren_multiplier)
                            if paren_multiplier_start == 0 and right == len(expression) - 1:
                                result = inside
                            else:
                                if expression[paren_multiplier_start - 1] == ' ' and expression[right + 1] == ' ':
                                    if expression[paren_multiplier_start - 2] == '-':
                                        inside = polyop.poly_scalar_multiplication(inside, -1.0)
                                    outside = expression[0:paren_multiplier_start - 3] + expression[right + 1:len(expression)]
                                    outside = parse_expr(outside, variables)
                                    result = polyop.poly_addition(inside, outside)
                                elif expression[paren_multiplier_start - 1] == ' ' and expression[right + 1] != ' ':
                                    if expression[paren_multiplier_start - 2] == '-':
                                        inside = polyop.poly_scalar_multiplication(inside, -1.0)
                                    multiplier_end = expression.find(' ', right)
                                    if multiplier_end == -1:
                                        multiplier_end = len(expression)
                                    multiplier = expression[right + 1:multiplier_end]
                                    multiplier = parse_expr(multiplier, variables)
                                    inside = polyop.poly_poly_multiplication(inside, multiplier)
                                    if multiplier_end == len(expression):
                                        outside = expression[0:paren_multiplier_start - 3]
                                    else:
                                        outside = expression[0:paren_multiplier_start - 3] + expression[multiplier_end:len(expression)]
                                    outside = parse_expr(outside, variables)
                                    result = polyop.poly_addition(inside, outside)
                                elif expression[paren_multiplier_start - 1] != ' ' and expression[right + 1] == ' ':
                                    multiplier_start = expression.rfind(' ', 0, paren_multiplier_start)
                                    if multiplier_start == -1:
                                        multiplier_start = 0
                                    else:
                                        multiplier_start -= 1
                                    multiplier = expression[multiplier_start:paren_multiplier_start]
                                    multiplier = parse_expr(multiplier, variables)
                                    inside = polyop.poly_poly_multiplication(inside, multiplier)
                                    if multiplier_start == 0:
                                        result = inside
                                    else:
                                        outside = expression[0:multiplier_start - 1] + expression[right + 1: len(expression)]
                                        outside = parse_expr(outside, variables)
                                        result = polyop.poly_addition(inside, outside)
                                elif expression[paren_multiplier_start - 1] != ' ' and expression[right + 1] != ' ':
                                    multiplier_left_start = expression.rfind(' ', 0, paren_multiplier_start)
                                    if multiplier_left_start == -1:
                                        multiplier_left_start = 0
                                    else:
                                        multiplier_left_start -= 1
                                    multiplier_right_end = expression.find(' ', right)
                                    if multiplier_right_end == -1:
                                        multiplier_right_end = len(expression)
                                    multiplier_left = expression[multiplier_left_start:paren_multiplier_start]
                                    multiplier_right = expression[right + 1:multiplier_right_end]
                                    multiplier_left = parse_expr(multiplier_left, variables)
                                    multiplier_right = parse_expr(multiplier_right, variables)
                                    inside = polyop.poly_poly_multiplication(inside, multiplier_left)
                                    inside = polyop.poly_poly_multiplication(inside, multiplier_right)
                                    if multiplier_left_start == 0 and multiplier_right_end == len(expression):
                                        result = inside
                                    elif multiplier_left_start != 0 and multiplier_right_end == len(expression):
                                        outside = expression[0:multiplier_left_start - 1]
                                        outside = parse_expr(outside, variables)
                                        result = polyop.poly_addition(inside, outside)
                                    elif multiplier_left_start == 0 and multiplier_right_end != len(expression):
                                        outside = expression[multiplier_right_end:len(expression)]
                                        outside = parse_expr(outside, variables)
                                        result = polyop.poly_addition(inside, outside)
                                    elif multiplier_left_start != 0 and multiplier_right_end != len(expression):
                                        outside = expression[0:multiplier_left_start - 1] + expression[multiplier_right_end:len(expression)]
                                        outside = parse_expr(outside, variables)
                                        result = polyop.poly_addition(inside, outside)
                        elif expression[left - 2] == ' ' and expression[right + 1] == ' ':
                            if expression[left - 3] == '-':
                                inside = polyop.poly_scalar_multiplication(inside, -1.0)
                            outside = expression[0:left - 4] + expression[right + 1:len(expression)]
                            outside = parse_expr(outside, variables)
                            result = polyop.poly_addition(inside, outside)
                        elif expression[left - 2] == ' ' and expression[right + 1] != ' ':
                            if expression[left - 3] == '-':
                                inside = polyop.poly_scalar_multiplication(inside, -1.0)
                            multiplier_end = expression.find(' ', right)
                            if multiplier_end == -1:
                                multiplier_end = len(expression)
                            multiplier = expression[right + 1:multiplier_end]
                            multiplier = parse_expr(multiplier, variables)
                            inside = polyop.poly_poly_multiplication(inside, multiplier)
                            if multiplier_end == len(expression):
                                outside = expression[0:left - 4]
                            else:
                                outside = expression[0:left - 4] + expression[multiplier_end:len(expression)]
                            outside = parse_expr(outside, variables)
                            result = polyop.poly_addition(inside, outside)
                        elif expression[left - 2] != ' ' and expression[right + 1] == ' ':
                            multiplier_start = expression.rfind(' ', 0, left - 1)
                            if multiplier_start == -1:
                                multiplier_start = 0
                            else:
                                multiplier_start -= 1
                            multiplier = expression[multiplier_start:left - 1]
                            multiplier = parse_expr(multiplier, variables)
                            inside = polyop.poly_poly_multiplication(inside, multiplier)
                            if multiplier_start == 0:
                                outside = expression[right + 1: len(expression)]
                            else:
                                outside = expression[0:multiplier_start - 1] + expression[right + 1: len(expression)]
                            outside = parse_expr(outside, variables)
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
                            multiplier_left = parse_expr(multiplier_left, variables)
                            multiplier_right = parse_expr(multiplier_right, variables)
                            inside = polyop.poly_poly_multiplication(inside, multiplier_left)
                            inside = polyop.poly_poly_multiplication(inside, multiplier_right)
                            if multiplier_left_start == 0 and multiplier_right_end == len(expression):
                                result = inside
                            elif multiplier_left_start != 0 and multiplier_right_end == len(expression):
                                outside = expression[0:multiplier_left_start - 1]
                                outside = parse_expr(outside, variables)
                                result = polyop.poly_addition(inside, outside)
                            elif multiplier_left_start == 0 and multiplier_right_end != len(expression):
                                outside = expression[multiplier_right_end:len(expression)]
                                outside = parse_expr(outside, variables)
                                result = polyop.poly_addition(inside, outside)
                            elif multiplier_left_start != 0 and multiplier_right_end != len(expression):
                                outside = expression[0:multiplier_left_start - 1] + expression[multiplier_right_end:len(expression)]
                                result = polyop.poly_addition(inside, outside)

            i -= 1
    else:
        result = parse_np(expression, variables)
    return result


expr = "5x + x(x(x + 1) + 5)(x + 2)x^2 + 5"
var = ['x', 'y', 'z']

print('final result:', parse_expr(expr, var))
