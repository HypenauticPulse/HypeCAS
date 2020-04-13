import input

[eq, var] = input.get_input()

poly = eq.split(var)
coeffPower = []
# print("Test 1:", poly)

i = 0
while i < len(poly):
    # print("Poly: ", poly)
    if poly[i] != '':
        Temp = poly[i].split()
        # print(Temp)
        if len(Temp) == 1:
            if poly[i - 1] == '':
                poly.pop(i - 1)
                i += 1
            else:
                i += 1
        elif len(Temp) == 2:
            poly.pop(i)
            poly.insert(i + 1, Temp[0] + Temp[1])
            i += 2
        elif poly[i - 1] == '':
            poly.pop(i)
            poly.insert(i, Temp[0])
            poly.insert(i + 1, Temp[1] + Temp[2])
            i += 2

        else:
            poly.pop(i)
            poly.insert(i, Temp[0])
            poly.insert(i + 1, Temp[1] + Temp[2])
            i += 2
    else:
        i += 1

print("Test 2:", poly)
i = 0
while i < len(poly):
    print("List:", coeffPower)
    print("i =", i)
    print(poly[i])
    print(poly[i].split())
    if len(poly) == 1:
        # print("alpha")
        coeffPower.append([float(1), float(poly[i].split("^")[1])])
        i += 1
    else:
        if poly[i] != '':
            if len(poly[i].split()) != 1 and len(poly[i].split()) != 0:
                Temp = poly[i].split()
                # print(Temp)
                # print("beta")
                coeffPower.append([float(Temp[0] + Temp[1]), float(0)])
                i += 1
            else:
                # try:
                #     print("a", poly[i])
                #     print("b", poly[i + 1])
                #     print("c", poly[i + 1].split())
                # except IndexError:
                #     pass
                if i + 1 == len(poly):
                    # print("gamma")
                    coeffPower.append([float(poly[i]), float(1)])
                    i += 1
                else:
                    if poly[i - 1] == '':
                        # print("delta")
                        coeffPower.append([float(1), float(poly[i].split("^")[1])])
                        i += 1
                    elif len(poly[i + 1].split("^")) == 1 and (len(poly[i].split()) == 1 or len(poly[i].split()) == 0 or len(poly[i].split()) == 2):
                        # print("epsilon")
                        coeffPower.append([float(poly[i]), float(1)])
                        i += 1
                    else:
                        # print("theta")
                        coeffPower.append([float(poly[i]), float(poly[i + 1].split("^")[1])])
                        i += 2
        else:
            i += 1

print("Converted Polynomial:", coeffPower)
