from polynomials.MultivariateEquality import MultivariateEquality


class UnivariateEquality(MultivariateEquality):
    def __init__(self, expr_string, variables):
        super().__init__(expr_string, variables)
        self.is_univariate = self.check_univariate()

    def check_univariate(self):
        if self.num_vars != 1:
            raise TypeError("The entered polynomial is not univariate")
        else:
            return True
