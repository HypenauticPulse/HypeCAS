import re

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


def poly_format(poly, var):
    coeffPower = []
    final = []
    poly = poly.split()
    i = 0
    end = 0
    while i < len(poly):
        if '(' in poly[i]:
            for j in range(i, len(poly) - i):
                if ')' in poly[i + j]:
                    end = i + j
        if end != 0:
            k = i
            while k < end:
                poly[k] = poly[k] + ' ' + poly[k + 1]
                poly.pop(k + 1)
                end -= 1
        # if '(' in poly[i] and ')' in poly[i + 2]:
        #     poly[i] = poly[i] + ' ' + poly[i + 1] + ' ' + poly[i + 2]
        #     poly.pop(i + 1)
        #     poly.pop(i + 1)
        i += 1

    j = 0

    while j < len(poly):
        if ('-' in poly[j] or '+' in poly[j]) and var not in poly[j]:
            poly[j] = poly[j] + poly[j + 1]
            poly.pop(j + 1)
        j += 1

    # for i in range(len(poly)):
    #     poly[i] = re.split('\(|\)', poly[i])

    for k in poly:
        if '(' not in k and ')' not in k:
            coeffPower.append(poly_conversion_array(k, var))
        elif '(' in k and ')' in k:
            k = re.split('\(|\)', k)
            temp = polyop.poly_poly_multiplication(poly_conversion_array(k[1], var), poly_conversion_array(k[2], var))
            if k[0] != '':
                if k[0] == '-':
                    temp = polyop.poly_scalar_multiplication(temp, -1)
                elif k[0] != '+':
                    temp = polyop.poly_scalar_multiplication(temp, float(k[0]))

            coeffPower.append(temp)

    for m in range(len(coeffPower)):
        for n in range(len(coeffPower[m])):
            final.append(coeffPower[m][n])

    return polyop.poly_sort(polyop.poly_consolidate(final))
