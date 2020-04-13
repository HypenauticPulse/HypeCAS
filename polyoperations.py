from polyinput import get_input_dual
from polyconvert import *

def poly_addition():
    [eq1, eq2, var] = get_input_dual()
    coeffPower1 = poly_conversion_array(eq1, var)
    coeffPower2 = poly_conversion_array(eq2, var)
    result = []

    for i in coeffPower1:
        found = 0
        for j in coeffPower2:
            if i[1] == j[1]:
                result.append([i[0] + j[0], i[1]])
                found = 1
        if found == 0:
            result.append(i)

    return poly_conversion_string(result)
