import polyoperations as polyop

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
                coeffPower.append([float(Temp[0]), int(0)])
            elif Temp[1] == '':
                coeffPower.append([float(Temp[0]), int(1)])
            else:
                coeffPower.append([float(Temp[0]), int(Temp[1].split('^')[1])])
        else:
            if len(Temp) == 1:
                coeffPower.append([float(poly[i - 1] + Temp[0]), int(0)])
            elif Temp[1] == '':
                coeffPower.append([float(poly[i - 1] + Temp[0]), int(1)])
            else:
                coeffPower.append([float(poly[i - 1] + Temp[0]), int(Temp[1].split('^')[1])])

    return polyop.poly_sort(polyop.poly_consolidate(coeffPower))


def poly_conversion_string(polyarray):
    polyString = ''
    count = 0
    for i in polyarray:
        if i == [0, 0]:
            count += 1
    if count == len(polyarray):
        polyString = '0'
    else:
        for j in polyarray:
            if j[1] == polyarray[0][1]:
                if j[1] == 0:
                    if j[0] > 0:
                        Tempstring = "{}".format(str(j[0]))
                        polyString += Tempstring + " "
                    elif j[0] < 0:
                        Tempstring = "- {}".format(str(abs(j[0])))
                        polyString += Tempstring + " "
                elif j[1] == 1.0:
                    if j[0] == 1.0:
                        Tempstring = "x"
                        polyString += Tempstring + " "
                    elif j[0] > 1.0:
                        Tempstring = "{}x".format(str(j[0]))
                        polyString += Tempstring + " "
                    elif j[0] == -1.0:
                        Tempstring = "- x"
                        polyString += Tempstring + " "
                    elif j[0] < -1.0:
                        Tempstring = "- {}x".format(str(abs(j[0])))
                        polyString += Tempstring + " "
                else:
                    if j[0] == 1.0:
                        Tempstring = "x^{}".format(str(j[1]))
                        polyString += Tempstring + " "
                    elif j[0] > 1.00:
                        Tempstring = "{}x^{}".format(str(j[0]), str(j[1]))
                        polyString += Tempstring + " "
                    elif j[0] == -1.0:
                        Tempstring = "- x^{}".format(str(j[1]))
                        polyString += Tempstring + " "
                    elif j[0] < -1.0:
                        Tempstring = "- {}x^{}".format(str(abs(j[0])), str(j[1]))
                        polyString += Tempstring + " "
            else:
                if j[1] == 0:
                    if j[0] > 0:
                        Tempstring = "+ {}".format(str(j[0]))
                        polyString += Tempstring + " "
                    elif j[0] < 0:
                        Tempstring = "- {}".format(str(abs(j[0])))
                        polyString += Tempstring + " "
                elif j[1] == 1.0:
                    if j[0] == 1.0:
                        Tempstring = "+ x"
                        polyString += Tempstring + " "
                    if j[0] > 1.0:
                        Tempstring = "+ {}x".format(str(j[0]))
                        polyString += Tempstring + " "
                    elif j[0] == -1.0:
                        Tempstring = "- x"
                        polyString += Tempstring + " "
                    elif j[0] < -1.0:
                        Tempstring = "- {}x".format(str(abs(j[0])))
                        polyString += Tempstring + " "
                else:
                    if j[0] == 1.0:
                        Tempstring = "+ x^{}".format(str(j[1]))
                        polyString += Tempstring + " "
                    elif j[0] > 1.0:
                        Tempstring = "+ {}x^{}".format(str(j[0]), str(j[1]))
                        polyString += Tempstring + " "
                    elif j[0] == -1.0:
                        Tempstring = "- x^{}".format(str(j[1]))
                        polyString += Tempstring + " "
                    elif j[0] < -1.0:
                        Tempstring = "- {}x^{}".format(str(abs(j[0])), str(j[1]))
                        polyString += Tempstring + " "
    return polyString
