from linearalgebra.LinearMultivariateEquality import LinearMultivariateEquality as LME


class LinearSystem:
    def __init__(self, variables, *args):
        self.leftequations = []
        self.rightequations = []
        self.variables = variables
        for i in args:
            temp = LME(i, self.variables)
            self.leftequations.append(temp.lhsArray)
            self.rightequations.append(temp.rhsArray)
    # TODO: Finish linear systems of equations implementation
