import polyoperations as polyop
import polyconvert as polycon


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
        print(expr)
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
        lparen = expr.find('(')
        rparen = expr.rfind(')')
        nexpr = expr[lparen + 1:rparen]
        nexpr = self.array_from_expr(nexpr)
        inside = parenfind(expr, lparen, rparen)
        if expr[lparen - 2] == "-":
            nexpr = polyop.poly_scalar_multiplication(nexpr, -1.0)
            if rparen != len(expr) - 1:
                if expr[rparen + 1] == self.var:
                    if expr[rparen + 2] == "^":
                        multstring = expr[rparen + 1: rparen + 4]
                        multiplier = self.array_no_paren(multstring)
                        nexpr = polyop.poly_poly_multiplication(nexpr, multiplier)
                        nexpr = polycon.poly_conversion_string(nexpr)
                        expr = expr.replace(expr[lparen - 2] + ' (' + str(inside) + ')' + multstring, nexpr)
                    else:
                        multiplier = self.array_no_paren(expr[rparen + 1])
                        nexpr = polyop.poly_poly_multiplication(nexpr, multiplier)
                        nexpr = polycon.poly_conversion_string(nexpr)
                        expr = expr.replace(expr[lparen - 2] + ' (' + str(inside) + ')x', nexpr)
                else:
                    nexpr = polycon.poly_conversion_string(nexpr)
                    print(nexpr)
                    print("AA", expr)
                    print(expr[lparen - 2] + ' (' + str(inside) + ')')
                    expr = expr.replace(expr[lparen - 2] + ' (' + str(inside) + ')', nexpr)
                    print("A", expr)
            else:
                nexpr = polycon.poly_conversion_string(nexpr)
                expr = expr.replace(expr[lparen - 2] + ' (' + str(inside) + ')', nexpr)
            return expr
        else:
            if rparen != len(expr) - 1:
                if expr[rparen + 1] == self.var:
                    if expr[rparen + 2] == "^":
                        multstring = expr[rparen + 1: rparen + 4]
                        multiplier = self.array_no_paren(multstring)
                        nexpr = polyop.poly_poly_multiplication(nexpr, multiplier)
                        nexpr = polycon.poly_conversion_string(nexpr)
                        # print(nexpr)
                        expr = expr.replace('(' + str(inside) + ')' + multstring, nexpr)
                        # print(expr)
                    else:
                        multiplier = self.array_no_paren(expr[rparen + 1])
                        nexpr = polyop.poly_poly_multiplication(nexpr, multiplier)
                        nexpr = polycon.poly_conversion_string(nexpr)
                        # print(nexpr)
                        expr = expr.replace('(' + str(inside) + ')x', nexpr)
                        # print(expr)
                else:
                    nexpr = polycon.poly_conversion_string(nexpr)
                    # print(nexpr)
                    expr = expr.replace('(' + str(inside) + ')', nexpr)
                    # print(expr)
            else:
                nexpr = polycon.poly_conversion_string(nexpr)
                if nexpr[0] == "-":
                    expr = expr.replace(expr[lparen - 2] + ' (' + str(inside) + ')', nexpr)
                else:
                    expr = expr.replace('(' + str(inside) + ')', nexpr)
            return expr

    def array_from_expr(self, expr):
        if not self.isequality:
            if '(' not in expr:
                if ')' in expr:
                    expr.replace(')', '')
                print("a")
                return self.array_no_paren(expr)
            else:
                print("b")
                # print(self.array_paren(expr))
                temp = self.array_paren(expr)
                if '(' not in temp and ')' in temp:
                    temp = temp.replace(')', '')
                return self.array_no_paren(temp)

        else:
            return "Unable to convert equalities to arrays at this time"


a = Expr("x^2 - (5x + (x - (x + 5))) + 1", "x")
print(a.array_from_expr(a.exprString))
