from polyutil import polyconvert as polycon, polyoperations as polyop


def test():
    print("Test")


class Expression:
    def __init__(self, expr, var):
        self.exprString = expr
        self.var = var
        self.length = len(self.exprString)
        self.isequality = self.check_equality()

    def check_equality(self):
        for i in range(self.length):
            if '=' in self.exprString[i]:
                return True
        return False

    def array_no_paren(self, expr):
        coeffpower = []
        expr = expr.split()
        if len(expr) % 2 == 0:
            x = 1
        else:
            x = 0

        for i in range(x, len(expr), 2):
            temp = expr[i].split(self.var)
            if temp[0] == '':
                temp[0] = '1'
            if not x and i == x:
                if len(temp) == 1:
                    coeffpower.append([float(temp[0]), int(0)])
                elif temp[1] == '':
                    coeffpower.append([float(temp[0]), int(1)])
                else:
                    coeffpower.append([float(temp[0]), int(temp[1].split('^')[1])])
            else:
                if len(temp) == 1:
                    coeffpower.append([float(expr[i - 1] + temp[0]), int(0)])
                elif temp[1] == '':
                    coeffpower.append([float(expr[i - 1] + temp[0]), int(1)])
                else:
                    coeffpower.append([float(expr[i - 1] + temp[0]), int(temp[1].split('^')[1])])
        return polyop.poly_sort(polyop.poly_consolidate(coeffpower))

    @staticmethod
    def parenfind(expr, start, end):
        return expr[expr.find("(", start, end) + 1:expr.find(")")]

    def array_paren(self, expr):
        lparen = expr.find("(")
        rparen = expr.rfind(")")
        inside = expr[lparen + 1: rparen]
        if "(" in expr:
            inside = self.array_from_expr(inside)
            if expr[lparen - 2] == "-":
                if rparen + 1 != len(expr):
                    if expr[rparen + 1] == "*":
                        multiplyend = expr.find(" ", rparen)
                        if multiplyend != -1:
                            if polyop.poly_leading_coeff(inside) < 0:
                                inside = polyop.poly_scalar_multiplication(inside, -1)
                                inside = polyop.poly_poly_multiplication(inside, self.array_no_paren(
                                    expr[rparen + 2: multiplyend]))
                                inside = polycon.poly_conversion_string(inside)
                                expr = expr.replace(expr[lparen - 2], '+')
                                expr = expr.replace(expr[lparen: multiplyend], inside)
                            else:
                                inside = polyop.poly_scalar_multiplication(inside, -1)
                                inside = polyop.poly_poly_multiplication(inside, self.array_no_paren(
                                    expr[rparen + 2: multiplyend]))
                                inside = polycon.poly_conversion_string(inside)
                                expr = expr.replace(expr[lparen - 2: multiplyend], inside)
                    else:
                        if polyop.poly_leading_coeff(inside) < 0:
                            inside = polyop.poly_scalar_multiplication(inside, -1)
                            inside = polycon.poly_conversion_string(inside)
                            expr = expr.replace(expr[lparen - 2], '+')
                            expr = expr.replace(expr[lparen: rparen + 1], inside)
                        else:
                            inside = polyop.poly_scalar_multiplication(inside, -1)
                            inside = polycon.poly_conversion_string(inside)
                            expr = expr.replace(expr[lparen - 2: rparen + 1], inside)
                else:
                    if polyop.poly_leading_coeff(inside) < 0:
                        inside = polyop.poly_scalar_multiplication(inside, -1)
                        inside = polycon.poly_conversion_string(inside)
                        expr = expr.replace(expr[lparen - 2], '+')
                        expr = expr.replace(expr[lparen: rparen + 1], inside)
                    else:
                        inside = polyop.poly_scalar_multiplication(inside, -1)
                        inside = polycon.poly_conversion_string(inside)
                        expr = expr.replace(expr[lparen - 2: rparen + 1], inside)
            else:
                if rparen + 1 != len(expr):
                    if expr[rparen + 1] == "*":
                        multiplyend = expr.find(" ", rparen)
                        if multiplyend != -1:
                            inside = polyop.poly_poly_multiplication(inside, self.array_no_paren(
                                expr[rparen + 2: multiplyend]))
                            inside = polycon.poly_conversion_string(inside)
                            expr = expr.replace(expr[lparen - 2: multiplyend], inside)
                else:
                    inside = polycon.poly_conversion_string(inside)
                    expr = expr.replace(expr[lparen: rparen + 1], inside)
        return self.array_no_paren(expr)

    def array_from_expr(self, expr):
        if '(' not in expr:
            return self.array_no_paren(expr)
        else:
            return self.array_paren(expr)

    def array_from_equ(self):
        if self.isequality:
            return self.array_from_expr(self.lhs), self.array_from_expr(self.rhs)
