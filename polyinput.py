def get_input():
    equation = input("Enter the polynomial: ")
    variable = input("Enter the variable of the polynomial: ")
    return equation, variable


def get_input_dual():
    variable = input("Enter the variable of both polynomials: ")
    equation1 = input("Enter the first polynomial: ")
    equation2 = input("Enter the second polynomial: ")
    return equation1, equation2, variable
