from polynomials.Expression import Expression
import polyutils.polyoperations as polyop


class MultivariateEquality(Expression):
    def __init__(self, expr_string, variables):
        super().__init__(expr_string, variables)
        self.is_equality = self.check_equality()
        self.lhs_string, self.rhs_string = self.split_equality()
        self.lhs_array, self.rhs_array = self.gen_array()
        self.degree = max(polyop.poly_degree(self.lhs_array), polyop.poly_degree(self.rhs_array))
        self.num_vars = len(self.variables)

    def check_equality(self):
        if '=' not in self.expr_string:
            raise TypeError('The entered string does not represent an equality')
        else:
            return True

    def split_equality(self):
        if self.is_equality:
            lhs, rhs = self.expr_string.split(' = ')
            return lhs, rhs
        else:
            raise TypeError('The entered string does not represent an equality')

    def gen_array(self):
        if self.is_equality:
            lhs = self.parse_expr(self.lhs_string, self.variables)
            rhs = self.parse_expr(self.rhs_string, self.variables)
            return lhs, rhs
        else:
            raise TypeError('The entered string does not represent an equality')