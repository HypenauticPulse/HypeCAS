from polynomials.Equality import Equality
from polynomials.Polynomial import Polynomial
from polynomials.Expression import Expression

# sys.stdout = TracePrints()

a = " - x^2 + y^2 - 15xy"
avars = ["x", "y"]

coeffpower = []
expr = a.split()
print(expr)
expr1 = []
expr2 = []
expr12 = []

for i in range(len(expr)):
    if avars[0] in expr[i] and avars[1] in expr[i]:
        expr12.append(expr[i - 1])
        expr12.append(expr[i])
    elif avars[0] in expr[i]:
        expr1.append(expr[i-1])
        expr1.append(expr[i])
    elif avars[1] in expr[i]:
        expr2.append(expr[i - 1])
        expr2.append(expr[i])

b = Polynomial(" ".join(expr1), avars[0])
c = Polynomial(" ".join(expr2), avars[1])
d = Polynomial(" ".join(expr12), avars[0]+avars[1])
print(b.exprArray)
print(c.exprArray)
print(d.exprArray)


# for i in range(x, len(expr), 2):
#     temp = expr[i].split(.var)
#     if temp[0] == '':
#         temp[0] = '1'
#     if not x and i == x:
#         if len(temp) == 1:
#             coeffpower.append([float(temp[0]), int(0)])
#         elif temp[1] == '':
#             coeffpower.append([float(temp[0]), int(1)])
#         else:
#             coeffpower.append([float(temp[0]), int(temp[1].split('^')[1])])
#     else:
#         if len(temp) == 1:
#             coeffpower.append([float(expr[i - 1] + temp[0]), int(0)])
#         elif temp[1] == '':
#             coeffpower.append([float(expr[i - 1] + temp[0]), int(1)])
#         else:
#             coeffpower.append([float(expr[i - 1] + temp[0]), int(temp[1].split('^')[1])])
