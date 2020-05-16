from polyutil_mv import polyoperations_mv as polyop


class LinearMultivariateExpression:
    def __init__(self, exprstring, variables):
        self.exprString = exprstring
        self.variables = variables
        self.islinear = self.checklinearity()
        self.length = len(self.exprString)
        self.isequality = self.check_equality()

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

    def check_equality(self):
        for i in range(self.length):
            if '=' in self.exprString[i]:
                return True
        return False

    @staticmethod
    def array_no_paren(expr, var):
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
        print("s", coeffpower)
        return coeffpower

    def parse(self, expr):
        # TODO: Fix bug with non-negative leading variables
        coeffpower = []
        expr = expr.split()
        exprs = []
        for i in self.variables:
            exprs.append([])
            if i in expr[0]:
                expr.insert(0, "+ ")
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
        print("t", expr)
        for i in expr:
            
            for j in range(len(self.variables)):
                if self.variables[j] in i:
                    exprs[j].append(i)
        for i in range(len(exprs)):
            for j in exprs[i]:
                coeffpower.append(self.array_no_paren(j, self.variables[i])[0])
        return polyop.poly_consolidate(coeffpower)

    def array_from_equ(self, lhs, rhs):
        if self.isequality:
            return self.parse(lhs), self.parse(rhs)
