from linearalgebra.LinearSystem import LinearSystem as LinSys
from linearalgebra import matrixoperations as matop
from polynomials.LinearMultivariateEquality import LinearMultivariateEquality as LMvE
from polyutils import polyoperations as polyop, polyconversion as polycon

eq1 = 'x + 2y + 3z = 0'
eq2 = '4x + 5y + 6z = 0'
eq3 = '7x + 8y + 9z = 0'
var = ['x', 'y', 'z']

test = LinSys(var, eq1, eq2, eq3)
print(test.lhs)
print(test.rhs)
print('\n\n')
matop.print_matrix(test.augmented_matrix)
rref_mat = matop.rref(test.augmented_matrix)
print('\n\n')
matop.print_matrix(rref_mat)

valid_count = 0
for i in rref_mat:
    valid = 1
    coeff = i[0:len(var)]
    constant = i[len(var)]
    if not any(coeff) and constant != 0:
        valid = 0
    valid_count += valid

if valid_count == len(rref_mat):
    print("This system of equations has solutions")
    free_count = 0
    free_vars = []
    for i in range(len(rref_mat)):
        if not any(rref_mat[i]):
            free_count += 1
            free_vars.append(i)
    print(free_count, "variable(s) are free")
    print('Free variables are:')
    for idx in free_vars:
        print(var[idx])

else:
    print("This system of equations is inconsistent")