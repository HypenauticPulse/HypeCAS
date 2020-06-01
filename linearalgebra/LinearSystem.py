from polynomials.LinearMultivariateEquality import LinearMultivariateEquality as LMvE
from polyutils import polyoperations as polyop
from linearalgebra import matrixoperations as matop


class LinearSystem:
    def __init__(self, variables, *args):
        self.variables = variables
        self.lhs, self.rhs = self.gen_arrays(args)
        self.augmented_matrix = self.gen_augmented_matrix()

    def gen_arrays(self, args):
        lhs_list = []
        rhs_list = []
        for i in args:
            print(i)
            temp = LMvE(i, self.variables)
            lhs = temp.lhs_array
            rhs = temp.rhs_array
            j = 0
            while j < len(rhs):
                k = 0
                trigger = 0
                while k < len(rhs[j][1]) and not trigger:
                    if rhs[j][1][k] != 0:
                        trigger = 1
                    k += 1
                if trigger:
                    lhs = polyop.poly_subtraction(lhs, [rhs[j]])
                    rhs = polyop.poly_subtraction(rhs, [rhs[j]])
                else:
                    j += 1
            lhs_list.append(lhs)
            rhs_list.append(rhs)
        self.insert_zeros(lhs_list)
        return lhs_list, rhs_list

    def gen_augmented_matrix(self):
        aug_mat = []
        for i in range(len(self.lhs)):
            temp = []
            for j in range(len(self.lhs[i])):
                temp.append(self.lhs[i][j][0])
            temp.append(self.rhs[i][0][0])
            aug_mat.append(temp)
        return aug_mat

    def insert_zeros(self, lhs_array):
        for i in lhs_array:
            j = len(i)
            while j != len(self.variables):
                for k in range(len(self.variables)):
                    power = []
                    for m in range(len(self.variables)):
                        if k == m:
                            power.append(1.0)
                        else:
                            power.append(0.0)
                    coeff = polyop.poly_find_coefficient(i, power)

                    if coeff == 0:
                        i.insert(k, [0.0, power])
                    j = len(i)

