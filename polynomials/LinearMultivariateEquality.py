from polynomials.MultivariateEquality import MultivariateEquality


class LinearMultivariateEquality(MultivariateEquality):
    def __init__(self, expr_string, variables):
        super().__init__(expr_string, variables)
        self.is_linear = self.check_linearity()

    def check_linearity(self):
        if self.degree != 1:
            raise TypeError("The entered polynomial is not linear")
        else:
            return True
