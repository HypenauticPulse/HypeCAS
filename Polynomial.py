from Expression import Expression
from polyutil import polyoperations as polyop, polyconvert as polycon


class Polynomial(Expression):
    def __init__(self, expr, var):
        super().__init__(expr, var)
        self.isequality = self.check_usage()
        self.exprArray = self.gen_array()
        self.degree = self.get_degree()

    def check_usage(self):
        if self.isequality:
            raise TypeError("Equalities should not be defined as polynomials")
        else:
            return self.isequality

    def gen_array(self):
        return self.array_from_expr(self.exprString)

    def __add__(self, other):
        if isinstance(other, Polynomial):
            return polyop.poly_addition(self.exprArray, other.exprArray)
        else:
            raise TypeError("The Addend is not a Polynomial")

    def __sub__(self, other):
        if isinstance(other, Polynomial):
            return polyop.poly_subtraction(self.exprArray, other.exprArray)
        else:
            raise TypeError("The Subtrahend is not a Polynomial")

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            return polyop.poly_poly_multiplication(self.exprArray, other.exprArray)
        elif isinstance(other, int):
            return polyop.poly_scalar_multiplication(self.exprArray, other)
        else:
            raise TypeError("The Multiplier is not a Polynomial or Integer")

    def __pow__(self, power, modulo=None):
        if isinstance(power, int):
            if power > 0:
                temp = self.exprArray
                for i in range(power - 1):
                    temp = polyop.poly_poly_multiplication(temp, self.exprArray)
                return temp
            elif power == 0:
                return 0
            else:
                raise TypeError("Only positive integer powers are allowed")
        else:
            raise TypeError("Only positive integer powers are allowed")

    def get_degree(self):
        return polyop.poly_degree(self.exprArray)

    def zeros(self):
        if self.degree == 2:
            return polyop.poly_quadratic_zeros(self.exprArray)
        elif self.degree == 1:
            return - self.exprArray[1][0] / self.exprArray[0][0], None
        elif self.degree == 0:
            print("Constants do not have zeros")
            return None
        else:
            print("Unable to find zeros for a Polynomial with greater than degree two at this time")
            return None

    def evaluate(self, input):
        output = 0
        for i in self.exprArray:
            output += i[0] * input ** i[1]
        return output

    def zeros_new(self):
        start = -25
        end = 25
        zerocount = 0
        zeros = []
        guesses = []
        trigger = 0
        while not trigger:
            out = []
            zerocount = 0
            for i in range(start, end):
                out.append(self.evaluate(i))
            for j in range(len(out) - 1):
                if out[j] == 0.0:
                    zeros.append(j + start)
                    zerocount += 1
                elif out[j] > 0 and out[j + 1] < 0 or out[j] < 0 and out[j + 1] > 0:
                    guesses.append(j + start + 1 / 2)
                    zerocount += 1
            if zerocount == self.degree:
                trigger = 1
            else:
                zerocount = 0
                start *= 10
                end *= 10

        fderiv = Polynomial(polycon.poly_conversion_string(polyop.derivative_powrule(self.exprArray)), self.var)
        for k in guesses:
            temp = k
            while abs(self.evaluate(temp)) > (1 * (10 ** (-10))):
                temp = temp - self.evaluate(temp) / fderiv.evaluate(temp)
            if len(zeros) != 0:
                existtrigger = 0
                for m in zeros:
                    if round(temp, 7) == round(m, 7):
                        existtrigger = 1
                if not existtrigger:
                    zeros.append(temp)
            else:
                zeros.append(temp)
        return guesses, zeros
