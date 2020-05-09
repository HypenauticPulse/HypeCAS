from polyutil_mv import polyoperations_mv as polyop


class LinearMultivariateExpression:
    def __init__(self, exprstring, variables):
        self.exprString = exprstring
        self.variables = variables
        self.islinear = self.checklinearity()

    def checklinearity(self):
        expr = self.exprString.split()
        i = 0
        count = 0
        while i < len(expr) and count <= 1:
            count = 0
            for j in self.variables:
                if j in expr[i]:
                    count += 1
            i += 1
        if count > 1:
            return False
        else:
            return True

    def array_no_paren(self, expr, var):
        coeffpower = []
        expr = expr.split()
        if len(expr) % 2 == 0:
            x = 1
        else:
            x = 0

        for i in range(x, len(expr), 2):
            temp = expr[i].split(var)
            if temp[0] == '':
                temp[0] = '1'
            if not x and i == x:
                if len(temp) == 1:
                    coeffpower.append([float(temp[0]), int(0), var])
                elif temp[1] == '':
                    coeffpower.append([float(temp[0]), int(1)])
                else:
                    coeffpower.append([float(temp[0]), int(temp[1].split('^')[1]), var])
            else:
                if len(temp) == 1:
                    coeffpower.append([float(expr[i - 1] + temp[0]), int(0), var])
                elif temp[1] == '':
                    coeffpower.append([float(expr[i - 1] + temp[0]), int(1), var])
                else:
                    coeffpower.append([float(expr[i - 1] + temp[0]), int(temp[1].split('^')[1]), var])
        return coeffpower

    def parse(self, expr):
        # TODO: Fix bug with non-negative leading variables
        coeffpower = []
        expr = expr.split()
        exprs = []
        for i in self.variables:
            exprs.append([])

        i = 0
        while i < len(expr):
            trigger = 0
            j = 0
            while j < len(self.variables) and not trigger:
                if self.variables[j] in expr[i]:
                    expr[i - 1] = expr[i - 1] + " " + expr[i]
                    trigger = 1
                    expr.pop(i)
                j += 1
            i += 1

        for i in expr:
            for j in range(len(self.variables)):
                if self.variables[j] in i:
                    exprs[j].append(i)

        for i in range(len(exprs)):
            for j in exprs[i]:
                coeffpower.append(self.array_no_paren(j, self.variables[i])[0])
        return polyop.poly_consolidate(coeffpower)
