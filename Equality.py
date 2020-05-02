from Expression import Expression
from polyutil import polyoperations as polyop


class Equality(Expression):
    def __init__(self, expr, var):
        super().__init__(expr, var)
        self.isequality = self.check_usage()
        self.lhs, self.rhs = self.split()
        self.lhsArray, self.rhsArray = self.gen_array()
        self.degree = self.get_degree()

    def check_usage(self):
        if not self.isequality:
            raise TypeError("Polynomials should not be defined as equalities")
        else:
            return self.isequality

    def split(self):
        for i in range(self.length):
            if '=' in self.exprString[i]:
                return [self.exprString[0: i - 1], self.exprString[i + 2: self.length]]

    def gen_array(self):
        lhsA, rhsA = self.array_from_equ()
        return lhsA, rhsA

    def __add__(self, other):
        if isinstance(other, Equality):
            lhs = polyop.poly_addition(self.lhsArray, other.lhsArray)
            rhs = polyop.poly_addition(self.rhsArray, other.rhsArray)
            return lhs, rhs
        else:
            raise TypeError("The Addend is not an Equality")

    def __sub__(self, other):
        if isinstance(other, Equality):
            lhs = polyop.poly_subtraction(self.lhsArray, other.lhsArray)
            rhs = polyop.poly_subtraction(self.rhsArray, other.rhsArray)
            return lhs, rhs
        else:
            raise TypeError("The Subtrahend is not an Equality")

    def __mul__(self, other):
        if isinstance(other, Equality):
            lhs = polyop.poly_poly_multiplication(self.lhsArray, other.lhsArray)
            rhs = polyop.poly_poly_multiplication(self.rhsArray, other.rhsArray)
            return lhs, rhs
        elif isinstance(other, int):
            lhs = polyop.poly_scalar_multiplication(self.lhsArray, other)
            rhs = polyop.poly_scalar_multiplication(self.rhsArray, other)
            return lhs, rhs
        else:
            raise TypeError("The Multiplier is not an  or Integer")

    def __pow__(self, power, modulo=None):
        if isinstance(power, int):
            if power > 0:
                lefttemp = self.lhsArray
                righttemp = self.rhsArray
                for i in range(power - 1):
                    lefttemp = polyop.poly_poly_multiplication(lefttemp, self.lhsArray)
                    righttemp = polyop.poly_poly_multiplication(righttemp, self.rhsArray)
                return lefttemp, righttemp
            elif power == 0:
                return 0, 0
            else:
                raise TypeError("Only positive integer powers are allowed")
        else:
            raise TypeError("Only positive integer powers are allowed")

    def get_degree(self):
        return max(polyop.poly_degree(self.lhsArray), polyop.poly_degree(self.rhsArray))

    def solve(self):
        if self.degree == 2:
            return polyop.poly_quadratic_zeros(polyop.poly_subtraction(self.lhsArray, self.rhsArray))
        elif self.degree == 1:
            temp = polyop.poly_subtraction(self.rhsArray, self.lhsArray)
            return - temp[1][0] / temp[0][0]
        elif self.degree == 0:
            print("Constants do not have zeros")
            return None
        else:
            print("Unable to find zeros for an Equality with greater than degree two at this time")
            return None
