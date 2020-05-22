def poly_conversion_string(polyarray, var):
    polystring = ''
    powers = []
    for _ in polyarray[0][1]:
        powers.append(0.0)

    count = 0
    for i in polyarray:
        if i == [0.0, powers]:
            count += 1

    if count == len(polyarray):
        polystring = '0.0'
    else:
        for i in polyarray:
            tempstring = ''
            if i == polyarray[0]:
                if i[0] > 0:
                    tempstring += "{}".format(i[0])
                else:
                    tempstring += "- {}".format(abs(i[0]))
                for j in range(len(i[1])):
                    if i[1][j] != 0.0:
                        if i[1][j] == 1.0:
                            tempstring += "{}".format(var[j])
                        else:
                            tempstring += "{}^{}".format(var[j], i[1][j])
            else:
                if i[0] > 0:
                    tempstring += "+ {}".format(i[0])
                else:
                    tempstring += "- {}".format(abs(i[0]))
                for j in range(len(i[1])):
                    if i[1][j] != 0.0:
                        if i[1][j] == 1.0:
                            tempstring += "{}".format(var[j])
                        else:
                            tempstring += "{}^{}".format(var[j], i[1][j])
            if i != polyarray[-1]:
                polystring += tempstring + " "
            else:
                polystring += tempstring
    return polystring


def equality_conversion_string(lhs, rhs, var):
    return poly_conversion_string(lhs, var) + ' = ' + poly_conversion_string(rhs, var)