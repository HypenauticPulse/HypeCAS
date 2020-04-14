def poly_conversion_array(poly, var):
    coeffPower = []
    poly = poly.split()

    if len(poly) % 2 == 0:
        x = 1
    else:
        x = 0

    for i in range(x, len(poly), 2):
        Temp = poly[i].split(var)
        if Temp[0] == '':
            Temp[0] = '1'
        if not x and i == x:
            if len(Temp) == 1:
                coeffPower.append([float(Temp[0]), float(0)])
            elif Temp[1] == '':
                coeffPower.append([float(Temp[0]), float(1)])
            else:
                coeffPower.append([float(Temp[0]), float(Temp[1].split('^')[1])])
        else:
            if len(Temp) == 1:
                coeffPower.append([float(poly[i - 1] + Temp[0]), float(0)])
            elif Temp[1] == '':
                coeffPower.append([float(poly[i - 1] + Temp[0]), float(1)])
            else:
                coeffPower.append([float(poly[i - 1] + Temp[0]), float(Temp[1].split('^')[1])])

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
