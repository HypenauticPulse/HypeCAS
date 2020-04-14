import polyinput
import polyconvert


def poly_consolidate(poly):
    powers = {}
    for coeff, power in poly:
        powers[power] = powers.get(power, 0) + coeff

    conspoly = [[coeff, power] for power, coeff in powers.items()]

    return conspoly


def poly_addition():
    [eq1, eq2, var] = polyinput.get_input_dual()

    coeffPower1 = polyconvert.poly_conversion_array(eq1, var)
    coeffPower2 = polyconvert.poly_conversion_array(eq2, var)

    coeffPower1 = poly_consolidate(coeffPower1)
    coeffPower2 = poly_consolidate(coeffPower2)

    result = poly_consolidate(coeffPower1 + coeffPower2)

    return polyconvert.poly_conversion_string(result)
