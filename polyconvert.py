def poly_conversion(eq, var):
    poly = eq.split()

    print(poly)
    coeffPower = []
    i = 1

    while i < len(poly):
        print("i =", i)
        poly.insert(i, poly[i] + poly[i + 1])
        poly.pop(i + 1)
        poly.pop(i + 1)
        print(poly)
        i += 1

    for j in poly:
        cp = j.split(var)
        print(cp)
        if len(cp) == 1:
            cp.append(0)
            for k in range(len(cp)):
                cp[k] = float(cp[k])
            coeffPower.append(cp)
        else:
            if '^' in cp[1]:
                if cp[0] == '':
                    Temp = cp[1]
                    Temp.split('^')
                    cp.pop(1)
                    cp.append(Temp[1])
                    cp.pop(0)
                    cp.insert(0, 1)
                    for k in range(len(cp)):
                        cp[k] = float(cp[k])
                    coeffPower.append(cp)
                else:
                    Temp = cp[1]
                    Temp.split('^')
                    cp.pop(1)
                    cp.append(Temp[1])
                    # print("cp alpha:", cp)
                    for k in range(len(cp)):
                        cp[k] = float(cp[k])
                    coeffPower.append(cp)
            elif cp[1] == '':
                cp.pop(1)
                cp.append(1)
                for k in range(len(cp)):
                    cp[k] = float(cp[k])
                coeffPower.append(cp)

    return coeffPower
