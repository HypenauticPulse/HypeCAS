import polyinput as polyin
import polyconvert as polycon
import polyoperations as polyop

[eq1, eq2, var] = polyin.get_input_dual()
poly1 = polycon.poly_conversion_array(eq1, var)
poly2 = polycon.poly_conversion_array(eq2, var)

for i in range(len(poly2)):
    poly2[i][0] = - poly2[i][0]
result = polyop.poly_sort(polyop.poly_consolidate(poly1 + poly2))
print("Result 1:", result)

result = polyop.poly_subtraction(poly1, poly2)
print("Result 2:", result)
