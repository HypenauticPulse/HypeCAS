def poly_conversion_array(eq, var):
    poly = eq.split()
    coeffPower = []

    i = 1
    while i < len(poly):
        poly.insert(i, poly[i] + poly[i + 1])
        poly.pop(i + 1)
        poly.pop(i + 1)
        i += 1

    for j in poly:
        cp = j.split(var)
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
                    for k in range(len(cp)):
                        cp[k] = float(cp[k])
                    coeffPower.append(cp)
            elif cp[1] == '':
                if cp[0] == '':
                    coeffPower.append([float(1), float(1)])
                else:
                    cp.pop(1)
                    cp.append(1)
                    for k in range(len(cp)):
                        cp[k] = float(cp[k])
                    coeffPower.append(cp)

    return coeffPower


def poly_conversion_string(polyarray):
    polyString = ''
    for i in polyarray:
        if i[1] == polyarray[0][1]:
            if i[1] == 0:
                if i[0] > 0:
                    Tempstring = "{}".format(str(i[0]))
                    polyString += Tempstring + " "
                elif i[0] < 0:
                    Tempstring = "- {}".format(str(abs(i[0])))
                    polyString += Tempstring + " "
            elif i[1] == 1.0:
                if i[0] == 1.0:
                    Tempstring = "x"
                    polyString += Tempstring + " "
                elif i[0] > 1.0:
                    Tempstring = "{}x".format(str(i[0]))
                    polyString += Tempstring + " "
                elif i[0] == -1.0:
                    Tempstring = "- x"
                    polyString += Tempstring + " "
                elif i[0] < -1.0:
                    Tempstring = "- {}x".format(str(abs(i[0])))
                    polyString += Tempstring + " "
            else:
                if i[0] == 1.0:
                    Tempstring = "x^{}".format(str(i[1]))
                    polyString += Tempstring + " "
                elif i[0] > 1.00:
                    Tempstring = "{}x^{}".format(str(i[0]), str(i[1]))
                    polyString += Tempstring + " "
                elif i[0] == -1.0:
                    Tempstring = "- x^{}".format(str(i[1]))
                    polyString += Tempstring + " "
                elif i[0] < -1.0:
                    Tempstring = "- {}x^{}".format(str(abs(i[0])), str(i[1]))
                    polyString += Tempstring + " "
        else:
            if i[1] == 0:
                if i[0] > 0:
                    Tempstring = "+ {}".format(str(i[0]))
                    polyString += Tempstring + " "
                elif i[0] < 0:
                    Tempstring = "- {}".format(str(abs(i[0])))
                    polyString += Tempstring + " "
            elif i[1] == 1.0:
                if i[0] == 1.0:
                    Tempstring = "+ x"
                    polyString += Tempstring + " "
                if i[0] > 1.0:
                    Tempstring = "+ {}x".format(str(i[0]))
                    polyString += Tempstring + " "
                elif i[0] == -1.0:
                    Tempstring = "- x"
                    polyString += Tempstring + " "
                elif i[0] < -1.0:
                    Tempstring = "- {}x".format(str(abs(i[0])))
                    polyString += Tempstring + " "
            else:
                if i[0] == 1.0:
                    Tempstring = "+ x^{}".format(str(i[1]))
                    polyString += Tempstring + " "
                elif i[0] > 1.0:
                    Tempstring = "+ {}x^{}".format(str(i[0]), str(i[1]))
                    polyString += Tempstring + " "
                elif i[0] == -1.0:
                    Tempstring = "- x^{}".format(str(i[1]))
                    polyString += Tempstring + " "
                elif i[0] < -1.0:
                    Tempstring = "- {}x^{}".format(str(abs(i[0])), str(i[1]))
                    polyString += Tempstring + " "
    return polyString
