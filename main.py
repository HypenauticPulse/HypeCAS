import input
import polyconvert

[eq, var] = input.get_input()

coeffPower = polyconvert.poly_conversion(eq, var)

print("Converted Polynomial:", coeffPower)
