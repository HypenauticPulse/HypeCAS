from Expr import Expr
from polyutil import polyoperations as polyop


class Polynomial(Expr):
    def __init__(self, expr, var):
        super().__init__(expr, var)
        self.exprArray, self.lhsArray, self.rhsArray = self.gen_array()
        self.degree = self.get_degree()

    def gen_array(self):
        if not self.isequality:
            return self.array_from_expr(self.exprString), None, None
        else:
            lhs, rhs = self.array_from_equ()
            return None, lhs, rhs

    def __add__(self, other):
        if self.isequality:
            raise TypeError("The Augend is an Equality")
        elif isinstance(other, Polynomial):
            if not other.isequality:
                return polyop.poly_addition(self.exprArray, other.exprArray)
            else:
                raise TypeError("The Addend is an Equality")
        else:
            raise TypeError("The Addend is not a Polynomial")

    def __sub__(self, other):
        if self.isequality:
            raise TypeError("The Minuend is an Equality")
        elif isinstance(other, Polynomial):
            if not other.isequality:
                return polyop.poly_subtraction(self.exprArray, other.exprArray)
            else:
                raise TypeError("The Subtrahend is an Equality")
        else:
            raise TypeError("The Subtrahend is not a Polynomial")

    def __mul__(self, other):
        print(type(other))
        if self.isequality:
            raise TypeError("The Multiplicand is an Equality")
        elif isinstance(other, Polynomial):
            if not other.isequality:
                return polyop.poly_poly_multiplication(self.exprArray, other.exprArray)
            else:
                raise TypeError("The Multiplier is an Equality")
        elif isinstance(other, int):
            return polyop.poly_scalar_multiplication(self.exprArray, other)
        else:
            raise TypeError("The Multiplier is not a Polynomial or Integer")

    def __pow__(self, power, modulo=None):
        if self.isequality:
            raise TypeError("The Multiplicand is an Equality")
        else:
            temp = self.exprArray
            for i in range(power - 1):
                temp = polyop.poly_poly_multiplication(temp, self.exprArray)
            return temp

    def get_degree(self):
        if self.isequality:
            return max(polyop.poly_degree(self.lhsArray), polyop.poly_degree(self.rhsArray))
        else:
            return polyop.poly_degree(self.exprArray)

    def solve(self):
        if not self.isequality:
            if self.degree == 2:
                return polyop.poly_quadratic_zeros(self.exprArray)
            elif self.degree == 1:
                return - self.exprArray[1][0] / self.exprArray[0][0]
            elif self.degree == 0:
                print("Constants do not have zeros")
                return None
            else:
                print("Unable to find zeros for a Polynomial with greater than degree two at this time")
                return None
        else:
            if self.degree == 2:
                return polyop.poly_quadratic_zeros(polyop.poly_subtraction(self.rhsArray, self.lhsArray))
            elif self.degree == 1:
                temp = polyop.poly_subtraction(self.rhsArray, self.lhsArray)
                return - temp[1][0] / temp[0][0]
            elif self.degree == 0:
                print("Constants do not have zeros")
                return None
            else:
                print("Unable to find zeros for an Equality with greater than degree two at this time")
                return None
