def get_input():
    equation = input("Enter the polynomials: ")
    variable = input("Enter the variable of the polynomials: ")
    return equation, variable


def get_input_dual():
    variable = input("Enter the variable of both polynomials: ")
    equation1 = input("Enter the first polynomials: ")
    equation2 = input("Enter the second polynomials: ")
    return equation1, equation2, variable
