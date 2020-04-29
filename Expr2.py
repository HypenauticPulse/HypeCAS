import polyoperations as polyop
import polyconvert as polycon


def test():
    print("Test")


def parenfind(expr, start, end):
    return expr[expr.find("(", start, end) + 1:expr.find(")")]


class Expr:
    def __init__(self, expr, var):
        self.exprString = expr
        self.var = var
        self.length = len(self.exprString)
        self.lhs, self.rhs, self.isequality = self.check_equality()

    def check_equality(self):
        for i in range(self.length):
            if '=' in self.exprString[i]:
                return [self.exprString[0:i - 1], self.exprString[i + 2: self.length], True]
        return [None, None, False]

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

    def array_paren(self, expr):
        lparen = expr.find("(")
        rparen = expr.rfind(")")
        inside = expr[lparen + 1: rparen]
        if "(" in expr:
            print("a", inside)
            inside = self.array_from_expr(inside)
            print("b", inside)
            if expr[lparen - 2] == "-":
                # TODO: finalize cases: multiplication at the end by the form ax^b and all type of multiplication at
                #  the front
                if rparen + 1 != len(expr):
                    if rparen + 2 != len(expr):
                        if expr[rparen + 2] == "^":
                            print("lc:", polyop.poly_leading_coeff(inside))
                            if polyop.poly_leading_coeff(inside) < 0:
                                inside = polyop.poly_scalar_multiplication(inside, -1)
                                print("c2", inside)
                                inside = polyop.poly_poly_multiplication(inside, self.array_no_paren(expr[rparen + 1: rparen + 4]))
                                print("d2", inside)
                                inside = polycon.poly_conversion_string(inside)
                                print("e2", inside)
                                expr = expr.replace(expr[lparen - 2], '+')
                                expr = expr.replace(expr[lparen: rparen + 4], inside)
                            else:
                                inside = polyop.poly_scalar_multiplication(inside, -1)
                                print("c2", inside)
                                inside = polyop.poly_poly_multiplication(inside, self.array_no_paren(expr[rparen + 1: rparen + 4]))
                                print("d2", inside)
                                inside = polycon.poly_conversion_string(inside)
                                print("e2", inside)
                                expr = expr.replace(expr[lparen - 2: rparen + 4], inside)
                        elif expr[rparen + 2] == self.var:
                            print("lc:", polyop.poly_leading_coeff(inside))
                            if polyop.poly_leading_coeff(inside) < 0:
                                inside = polyop.poly_scalar_multiplication(inside, -1)
                                print("c2", inside)
                                inside = polyop.poly_poly_multiplication(inside,
                                                                         self.array_no_paren(expr[rparen + 1: rparen + 3]))
                                print("d2", inside)
                                inside = polycon.poly_conversion_string(inside)
                                print("e2", inside)
                                expr = expr.replace(expr[lparen - 2], '+')
                                expr = expr.replace(expr[lparen: rparen + 3], inside)
                            else:
                                inside = polyop.poly_scalar_multiplication(inside, -1)
                                print("c2", inside)
                                inside = polyop.poly_poly_multiplication(inside, self.array_no_paren(expr[rparen + 1: rparen + 3]))
                                print("d2", inside)
                                inside = polycon.poly_conversion_string(inside)
                                print("e2", inside)
                                expr = expr.replace(expr[lparen - 2: rparen + 3], inside)

                        else:
                            print("lc:", polyop.poly_leading_coeff(inside))
                            if polyop.poly_leading_coeff(inside) < 0:
                                inside = polyop.poly_scalar_multiplication(inside, -1)
                                print("c1", inside)
                                inside = polycon.poly_conversion_string(inside)
                                print("d1", inside)
                                expr = expr.replace(expr[lparen - 2], '+')
                                expr = expr.replace(expr[lparen: rparen + 1], inside)
                            else:
                                inside = polyop.poly_scalar_multiplication(inside, -1)
                                print("c1", inside)
                                inside = polycon.poly_conversion_string(inside)
                                print("d1", inside)
                                expr = expr.replace(expr[lparen - 2: rparen + 1], inside)
                    else:
                        if expr[rparen + 1] == self.var:
                            print("lc:", polyop.poly_leading_coeff(inside))
                            if polyop.poly_leading_coeff(inside) < 0:
                                inside = polyop.poly_scalar_multiplication(inside, -1)
                                print("c2", inside)
                                inside = polyop.poly_poly_multiplication(inside, self.array_no_paren(expr[rparen + 1]))
                                print("d2", inside)
                                inside = polycon.poly_conversion_string(inside)
                                print("e2", inside)
                                expr = expr.replace(expr[lparen - 2], '+')
                                expr = expr.replace(expr[lparen: rparen + 2], inside)
                            else:
                                inside = polyop.poly_scalar_multiplication(inside, -1)
                                print("c2", inside)
                                inside = polyop.poly_poly_multiplication(inside, self.array_no_paren(expr[rparen + 1]))
                                print("d2", inside)
                                inside = polycon.poly_conversion_string(inside)
                                print("e2", inside)
                                expr = expr.replace(expr[lparen - 2: rparen + 2], inside)
                else:
                    print("lc:", polyop.poly_leading_coeff(inside))
                    if polyop.poly_leading_coeff(inside) < 0:
                        inside = polyop.poly_scalar_multiplication(inside, -1)
                        print("c1", inside)
                        inside = polycon.poly_conversion_string(inside)
                        print("d1", inside)
                        expr = expr.replace(expr[lparen - 2], '+')
                        expr = expr.replace(expr[lparen: rparen + 1], inside)
                    else:
                        inside = polyop.poly_scalar_multiplication(inside, -1)
                        print("c1", inside)
                        inside = polycon.poly_conversion_string(inside)
                        print("d1", inside)
                        expr = expr.replace(expr[lparen - 2: rparen + 1], inside)
            # TODO: extend the new cases from subtraction to addition
            else:
                if rparen + 1 != len(expr):
                    if expr[rparen + 1] == self.var:
                        inside = polyop.poly_poly_multiplication(inside, self.array_no_paren(expr[rparen + 1]))
                        print("c2", inside)
                        inside = polycon.poly_conversion_string(inside)
                        print("d2", inside)
                        expr = expr.replace(expr[lparen: rparen + 2], inside)
                    else:
                        inside = polycon.poly_conversion_string(inside)
                        print("c2", inside)
                        expr = expr.replace(expr[lparen: rparen + 1], inside)
                else:
                    inside = polycon.poly_conversion_string(inside)
                    print("c2", inside)
                    expr = expr.replace(expr[lparen: rparen + 1], inside)
            print("expr", expr)
        return self.array_no_paren(expr)

    def array_from_expr(self, expr):
        if not self.isequality:
            if '(' not in expr:
                return self.array_no_paren(expr)
            else:
                return self.array_paren(expr)
        else:
            return "Unable to convert equalities to arrays at this time"


a = Expr("(x^2 - (x - (x + 1)x^2)x)", "x")
print(a.array_from_expr(a.exprString))
