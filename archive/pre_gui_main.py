from polyutil import polyconvert as polycon, polyoperations as polyop, polyinput as polyin

print("Valid operations\n"
      "(1) Polynomial Addition\n"
      "(2) Polynomial Subtraction\n"
      "(3) Polynomial Multiplication\n"
      "(4) Polynomial division\n"
      "(5) Polynomial Conversion")

while True:
    choice = int(input("Enter the desired operation: "))
    if not 1 <= choice <= 5:
        print("Invalid selection, please try again.\n")
    else:
        break

if choice == 1:
    [eq1, eq2, var] = polyin.get_input_dual()
    coeffPower1 = polycon.poly_conversion_array(eq1, var)
    coeffPower2 = polycon.poly_conversion_array(eq2, var)

    result = polyop.poly_addition(coeffPower1, coeffPower2)
    print("Result:", polycon.poly_conversion_string(result))

elif choice == 2:
    [eq1, eq2, var] = polyin.get_input_dual()
    coeffPower1 = polycon.poly_conversion_array(eq1, var)
    coeffPower2 = polycon.poly_conversion_array(eq2, var)

    result = polyop.poly_subtraction(coeffPower1, coeffPower2)
    print("Result:", polycon.poly_conversion_string(result))

elif choice == 3:
    [eq1, eq2, var] = polyin.get_input_dual()
    coeffPower1 = polycon.poly_conversion_array(eq1, var)
    coeffPower2 = polycon.poly_conversion_array(eq2, var)

    result = polyop.poly_poly_multiplication(coeffPower1, coeffPower2)
    print("Result:", polycon.poly_conversion_string(result))
elif choice == 4:
    [eq1, eq2, var] = polyin.get_input_dual()
    coeffPower1 = polycon.poly_conversion_array(eq1, var)
    coeffPower2 = polycon.poly_conversion_array(eq2, var)

    [quotient, remainder] = polyop.poly_poly_division(coeffPower1, coeffPower2)
    if quotient == -1 and remainder == -1:
        print("Error, divisor is zero")
    else:
        print("Quotient:", polycon.poly_conversion_string(quotient))
        print("Remainder:", polycon.poly_conversion_string(remainder))
else:
    [eq, var] = polyin.get_input()

    coeffPower = polyop.poly_sort(polycon.poly_conversion_array(eq, var))

    print("Converted Polynomial:", coeffPower)
    polyString = polycon.poly_conversion_string(coeffPower)
    print("Polynomial string:", polyString)
