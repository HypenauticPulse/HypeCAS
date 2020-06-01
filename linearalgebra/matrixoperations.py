def swap_rows(row_a, row_b, aug_mat):
    temp = aug_mat[row_b]
    aug_mat[row_b] = aug_mat[row_a]
    aug_mat[row_a] = temp


def multiply_scalar(row, scalar, aug_mat):
    for i in range(len(aug_mat[row])):
        aug_mat[row][i] *= scalar


def multiply_add_row(row_a, row_b, scalar, aug_mat):
    for i in range(len(aug_mat[row_a])):
        aug_mat[row_b][i] += scalar * aug_mat[row_a][i]


def rref(aug_mat):
    temp = []
    for i in aug_mat:
        temp.append(i)

    for i in range(len(temp)):
        if temp[i][i] == 0:
            trigger = 0
            j = i + 1
            while j < len(temp) and not trigger:
                if temp[j][i] != 0:
                    trigger = 1
                else:
                    j += 1
            if trigger:
                swap_rows(i, j, temp)

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
                multiply_scalar(i, 1.0 / temp[i][pivot], temp)
            for j in range(i + 1, len(temp)):
                if temp[j][pivot] != 0:
                    multiply_add_row(i, j, - temp[j][pivot], temp)

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
                multiply_scalar(i, 1.0 / temp[i][pivot], temp)
            if temp[i][pivot] == 1:
                for j in reversed(range(i)):
                    if temp[j][pivot] != 0:
                        multiply_add_row(i, j, - temp[j][pivot], temp)

    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if temp[i][j] == -0.0:
                temp[i][j] = 0.0

    return temp


def print_matrix(matrix):
    print('\n'.join([''.join(['{:7}'.format(round(item, 2)) for item in row])
                     for row in matrix]))
