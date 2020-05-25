from polynomials.Expression import Expression
from polyutils import polyoperations as polyop


class MultivariatePolynomial(Expression):
    def __init__(self, expr_string, variables):
        super().__init__(expr_string, variables)
        self.expr_array = self.gen_array()
        self.num_vars = len(self.variables)
        self.degree = polyop.poly_degree(self.expr_array)

    def gen_array(self):
        return self.parse_expr(self.expr_string, self.variables)

    def evaluate(self, inputval):
        result = 0
        for i in self.expr_array:
            term = i[0]
            for j in range(len(i[1])):
                term *= inputval[j] ** i[1][j]
            result += term
        return result
