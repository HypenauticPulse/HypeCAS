import polyinput as polyin
import polyconvert as polycon
import polyoperations as polyop


print("Valid operations\n(1) Polynomial Addition\n(2) Polynomial Subtraction\n(3) Polynomial Multiplication\n(4) "
      "Polynomial division\n(5) Polynomial Conversion")

while True:
    choice = int(input("Enter the desired operation: "))
    if not 1 <= choice <= 5:
        print("Invalid selection, please try again.\n")
    else:
        break

if choice == 1:
    sum = polyop.poly_addition()
    print("Result:", sum)
elif choice == 2:
    pass
elif choice == 3:
    pass
elif choice == 4:
    pass
else:
    [eq, var] = polyin.get_input()

    coeffPower = polycon.poly_conversion_array(eq, var)
    coeffPower = polyop.poly_consolidate(coeffPower)

    print("Converted Polynomial:", coeffPower)
    polyString = polycon.poly_conversion_string(coeffPower)
    print("Polynomial string:", polyString)
