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
    trigger = 0
    i = 0
    if a[0] != '-':
        a = ['+'] + a
    print(a)
    j = 0
    print(a)
    while j < len(a):
        a[j] = a[j] + a[j + 1]
        a.pop(j + 1)
        j += 1
    print(a)
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
    power = []
    for _ in range(len(variables)):
        power.append(0.0)
    result = [0.0, power]
    i = 0
    while i < len(paren_indices):
        print("pass")
        if i != len(paren_indices) - 1:
            if paren_indices[i][0] > paren_indices[i + 1][0] and paren_indices[i][1] < paren_indices[i + 1][1]:
                left = paren_indices[i + 1][0] + 1
                right = paren_indices[i + 1][1]
                inside = parse_expr(expression[left: right], variables)
                print("inside", inside)
                print("expr", expression)
                if right != len(expression) - 1:
                    if expression[left - 2] == ' ' and expression[right + 1] != '(' and all(
                            expression[right + 1] != variable for variable in variables):
                        if expression[left - 2] == '-':
                            inside = polyop.poly_scalar_multiplication(inside, -1)
                        expression = expression[0:left - 4] + expression[right + 1: len(expression)]
                        print(expression)
                        inside = polyop.poly_addition(inside, parse_np(expression, variables))
                        print("inside", inside)
                        result = polyop.poly_addition(result, inside)
                    elif expression[left - 2] != ' ':
                        multiplier_start = expression.rfind(' ', 0, left)
                        print(expression[multiplier_start + 1: left - 1])
                        multiplier = parse_np(expression[multiplier_start + 1: left - 1], variables)
                        print(multiplier)
                        inside = polyop.poly_poly_multiplication(inside, multiplier)
                        print(inside)
                        result = polyop.poly_addition(result, inside)

                else:
                    if expression[left - 2] == ' ':
                        if expression[left - 3] == '-':
                            inside = polyop.poly_scalar_multiplication(inside, -1)
                        expression = expression[0:left - 4]
                        print(expression)
                        inside = polyop.poly_addition(inside, parse_np(expression, variables))
                        print("inside", inside)
                        result = polyop.poly_addition(result, inside)
                print("expr1", expression)
                paren_indices.pop(i + 1)
            else:
                left = paren_indices[i][0] + 1
                right = paren_indices[i][1]
                inside = parse_np(expression[left: right], variables)
                result = polyop.poly_addition(result, inside)
        else:
            left = paren_indices[i][0] + 1
            right = paren_indices[i][1]
            inside = parse_np(expression[left: right], variables)
            print("inside1", inside)
            print("expr", expression)
            if right != len(expression) - 1:
                if expression[left - 2] == ' ' and expression[right + 1] != '(' and all(
                        expression[right + 1] != variable for variable in variables):
                    if expression[left - 3] == '-':
                        inside = polyop.poly_scalar_multiplication(inside, -1)
                    expression = expression[0:left - 4] + expression[right+1: len(expression)]
                    print(expression)
                    inside = polyop.poly_addition(inside, parse_np(expression, variables))
                    print("inside", inside)
                    result = polyop.poly_addition(result, inside)
            else:
                if expression[left - 2] == ' ':
                    if expression[left - 3] == '-':
                        inside = polyop.poly_scalar_multiplication(inside, -1)
                    expression = expression[0:left - 4]
                    print(expression)
                    inside = polyop.poly_addition(inside, parse_np(expression, variables))
                    print("inside", inside)
                    result = polyop.poly_addition(result, inside)

            print("inside1", inside)
        i += 1
    print("returning")
    return inside

#
# expr = "- x^2yz^3wt(2.5xy^2zt^2 - (10x^2yw^-5 + 5xz) + 15xyz) + (150)"
# var = ['x', 'y', 'z', 'w', 't']
expr = "- x^2yz^3(2.5xy^2z - (10x^2y + 5xz) + 15xyz) + (150)"
var = ['x', 'y', 'z']

parse_expr(expr, var)
