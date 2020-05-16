from linearalgebra.LinearMultivariateExpression import LinearMultivariateExpression


class LinearMultivariatePolynomial(LinearMultivariateExpression):
    def __init__(self, exprstring, variables):
        super().__init__(exprstring, variables)
        self.exprArray = self.gen_array()

    def gen_array(self):
        if self.islinear:
            return self.parse(self.exprString)
        else:
            return TypeError("This polynomial is not linear")
