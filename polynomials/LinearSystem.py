from polynomials.LinearMultivariatePolynomial import LinearMultivariatePolynomial as LMP

class LinearSystem:
    def __init__(self, variables, *args):
        self.equations = []
        self.variables = variables
        for i in args:
            self.equations.append(LMP(i, self.variables).exprArray)
    #TODO: Finish linear systems of equations implementation