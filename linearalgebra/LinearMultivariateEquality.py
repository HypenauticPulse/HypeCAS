from linearalgebra.LinearMultivariateExpression import LinearMultivariateExpression


class LinearMultivariateEquality(LinearMultivariateExpression):
    def __init__(self, exprstring, variables):
        super().__init__(exprstring, variables)
        self.isequality = self.check_usage()
        self.lhs, self.rhs = self.split()
        self.lhsArray, self.rhsArray = self.gen_array()

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
        print(self.lhs, self.rhs)
        lhsarray, rhsarray = self.array_from_equ(self.lhs, self.rhs)
        return lhsarray, rhsarray

