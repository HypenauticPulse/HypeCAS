def ero_swap_rows(row_a, row_b, aug_mat):
    temp = aug_mat[row_b]
    aug_mat[row_b] = aug_mat[row_a]
    aug_mat[row_a] = temp


def ero_multiply_scalar(row, scalar, aug_mat):
    for i in range(len(aug_mat[row])):
        aug_mat[row][i] *= scalar


def ero_multiply_add_row(row_a, row_b, scalar, aug_mat):
    for i in range(len(aug_mat[row_a])):
        aug_mat[row_b][i] += scalar * aug_mat[row_a][i]


def rref(aug_mat):
    temp = []
    for i in aug_mat:
        temp_row = []
        for j in range(len(i)):
            temp_row.append(i[j])
        temp.append(temp_row)

    temp = swap_zero_pivots(temp)

    for i in range(len(temp)):
        j = i
        trigger = 0
        pivot = -1
        while j < len(temp[i]) and not trigger:
            if temp[i][j] != 0.0:
                trigger = 1
                pivot = j
            j += 1
        if pivot != -1:
            if temp[i][pivot] != 1 and temp[i][pivot] != 0:
                ero_multiply_scalar(i, 1.0 / temp[i][pivot], temp)
            for j in range(i + 1, len(temp)):
                if temp[j][pivot] != 0:
                    ero_multiply_add_row(i, j, - temp[j][pivot], temp)

    for i in reversed(range(len(temp))):
        j = i
        trigger = 0
        pivot = -1
        while j < len(temp[i]) and not trigger:
            if temp[i][j] != 0.0:
                trigger = 1
                pivot = j
            j += 1
        if pivot != -1:
            if temp[i][pivot] != 1 and temp[i][pivot] != 0:
                ero_multiply_scalar(i, 1.0 / temp[i][pivot], temp)
            if temp[i][pivot] == 1:
                for j in reversed(range(i)):
                    if temp[j][pivot] != 0:
                        ero_multiply_add_row(i, j, - temp[j][pivot], temp)

    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if temp[i][j] == -0.0:
                temp[i][j] = 0.0

    return temp


def echelon_form(aug_mat):
    temp = []
    for i in aug_mat:
        temp_row = []
        for j in range(len(i)):
            temp_row.append(i[j])
        temp.append(temp_row)

    temp = swap_zero_pivots(temp)

    for i in range(len(temp)):
        j = i
        trigger = 0
        pivot = -1
        while j < len(temp[i]) and not trigger:
            if temp[i][j] != 0.0:
                trigger = 1
                pivot = j
            j += 1
        if pivot != -1:
            if temp[i][pivot] != 1 and temp[i][pivot] != 0:
                ero_multiply_scalar(i, 1.0 / temp[i][pivot], temp)
            for j in range(i + 1, len(temp)):
                if temp[j][pivot] != 0:
                    ero_multiply_add_row(i, j, - temp[j][pivot], temp)

    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if temp[i][j] == -0.0:
                temp[i][j] = 0.0

    return temp


def print_matrix(matrix):
    print('\n'.join([''.join(['{:7}'.format(round(item, 2)) for item in row])
                     for row in matrix]))


def matrix_add(matrix_a, matrix_b):
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        raise ValueError(
            "Dimension mismatch for addition between {}x{} and {}x{} matrices.".format(len(matrix_a), len(matrix_a[0]),
                                                                                       len(matrix_b), len(matrix_b[0])))
    else:
        result = []
        for i in range(len(matrix_a)):
            row_result = []
            for j in range(len(matrix_a[0])):
                row_result.append(matrix_a[i][j] + matrix_b[i][j])
            result.append(row_result)
    return result


def matrix_sub(matrix_a, matrix_b):
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        raise ValueError(
            "Dimension mismatch for subtraction between {}x{} and {}x{} matrices.".format(len(matrix_a),
                                                                                          len(matrix_a[0]),
                                                                                          len(matrix_b),
                                                                                          len(matrix_b[0])))
    else:
        temp = []
        for i in range(len(matrix_a)):
            row_temp = []
            for j in range(len(matrix_a[0])):
                row_temp.append(- matrix_b[i][j])
            temp.append(row_temp)
    return matrix_add(matrix_a, temp)


def matrix_scalar_multiply(matrix, scalar):
    result = []
    for i in range(len(matrix)):
        row_result = []
        for j in range(len(matrix[0])):
            row_result.append(scalar * matrix[i][j])
        result.append(row_result)

    return result


def matrix_multiplication(matrix_a, matrix_b):
    if len(matrix_a) != len(matrix_b[0]) or len(matrix_a[0]) != len(matrix_b):
        raise ValueError(
            "Dimension mismatch for multiplication between {}x{} and {}x{} matrices.".format(len(matrix_a),
                                                                                             len(matrix_a[0]),
                                                                                             len(matrix_b),
                                                                                             len(matrix_b[0])))
    else:
        result = []
        for i in range(len(matrix_a)):
            row_result = []
            for j in range(len(matrix_b[0])):
                term_result = 0
                for k in range(len(matrix_b)):
                    term_result += matrix_a[i][k] * matrix_b[k][j]
                row_result.append(term_result)
            result.append(row_result)

    return result


def create_minor(matrix, r_row, r_col):
    if not r_row <= len(matrix) or not r_col <= len(matrix[0]):
        raise ValueError(
            "Invalid row, {}, or column, {}, to remove from an {}x{} matrix".format(r_row, r_col, len(matrix),
                                                                                    len(matrix[0])))
    else:
        temp = []
        for i in range(len(matrix)):
            if i != r_row - 1:
                row_temp = []
                for j in range(len(matrix[0])):
                    if j != r_col - 1:
                        row_temp.append(matrix[i][j])
                temp.append(row_temp)

    return temp


def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Determinants can only be found for square matrices.")
    else:
        temp = lu_decomposition_upper(matrix)
        det = 1
        for i in range(len(matrix)):
            det *= temp[i][i]

    return det


def swap_zero_pivots(matrix):
    temp = []
    for i in matrix:
        temp_row = []
        for j in range(len(i)):
            temp_row.append(i[j])
        temp.append(temp_row)

    for i in range(len(temp)):
        if temp[i][i] == 0:
            trigger = 0
            j = 0
            while j < len(temp) and not trigger:
                if temp[j][i] != 0:
                    trigger = 1
                else:
                    j += 1
            if trigger:
                ero_swap_rows(i, j, temp)

    return temp


def lu_decomposition_upper(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Only square matrices can undergo LU decomposition.")
    else:
        temp = []
        for i in matrix:
            temp_row = []
            for j in range(len(i)):
                temp_row.append(i[j])
            temp.append(temp_row)
        for i in range(len(temp)):
            j = i
            trigger = 0
            pivot = -1
            while j < len(temp[i]) and not trigger:
                if temp[i][j] != 0.0:
                    trigger = 1
                    pivot = j
                j += 1
            if pivot != -1:
                for j in range(i + 1, len(temp)):
                    if temp[j][pivot] != 0:
                        ero_multiply_add_row(i, j, - temp[j][pivot] / temp[i][pivot], temp)
        for i in range(len(temp)):
            for j in range(len(temp[i])):
                if temp[i][j] == -0.0:
                    temp[i][j] = 0.0
    return temp


def invert(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Only square matrices can be inverted")
    else:
        det = determinant(matrix)
        if det == 0:
            raise ValueError("This matrix is singular since the determinant is zero")
        else:
            temp = []
            for i in range(len(matrix)):
                temp_row = []
                for j in range(len(matrix[i])):
                    temp_row.insert(j, matrix[i][j])
                    if i == j:
                        temp_row.append(1)
                    else:
                        temp_row.append(0)
                temp.append(temp_row)

            temp_rref = rref(temp)
            inverse = []
            for i in range(len(matrix)):
                inverse_row = []
                for j in range(len(matrix[i])):
                    inverse_row.append(temp_rref[i][j + len(matrix[0])])
                inverse.append(inverse_row)

            return inverse


def transpose(matrix):
    temp = []
    for i in range(len(matrix)):
        temp_row = []
        for j in range(len(matrix[i])):
            temp_row.append(matrix[j][i])
        temp.append(temp_row)
    return temp


def anti_transpose(matrix):
    temp = []
    for i in range(len(matrix)):
        temp_row = []
        for j in range(len(matrix[i])):
            temp_row.append(matrix[len(matrix) - j - 1][len(matrix) - i - 1])
        temp.append(temp_row)
    return temp