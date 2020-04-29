import re

import polyoperations as polyop


def poly_conversion_array(poly, var):
    coeffpower = []
    poly = poly.split()

    if len(poly) % 2 == 0:
        x = 1
    else:
        x = 0

    for i in range(x, len(poly), 2):
        temp = poly[i].split(var)
        if temp[0] == '':
            temp[0] = '1'
        if not x and i == x:
            if len(temp) == 1:
                coeffpower.append([float(temp[0]), int(0)])
            elif temp[1] == '':
                coeffpower.append([float(temp[0]), int(1)])
            else:
                coeffpower.append([float(temp[0]), int(temp[1].split('^')[1])])
        else:
            if len(temp) == 1:
                coeffpower.append([float(poly[i - 1] + temp[0]), int(0)])
            elif temp[1] == '':
                coeffpower.append([float(poly[i - 1] + temp[0]), int(1)])
            else:
                coeffpower.append([float(poly[i - 1] + temp[0]), int(temp[1].split('^')[1])])

    return polyop.poly_sort(polyop.poly_consolidate(coeffpower))


def poly_conversion_string(polyarray):
    polystring = ''
    count = 0
    for i in polyarray:
        if i == [0, 0]:
            count += 1
    if count == len(polyarray):
        polystring = '0'
    else:
        for j in polyarray:
            if j[1] == polyarray[0][1]:
                if j[1] == 0:
                    if j[0] > 0:
                        tempstring = "{}".format(str(int(j[0])))
                        polystring += tempstring + " "
                    elif j[0] < 0:
                        tempstring = "- {}".format(str(int(abs(j[0]))))
                        polystring += tempstring + " "
                elif j[1] == 1.0:
                    if j[0] == 1.0:
                        tempstring = "x"
                        polystring += tempstring + " "
                    elif j[0] > 0.0:
                        tempstring = "{}x".format(str(int(j[0])))
                        polystring += tempstring + " "
                    elif j[0] == -1.0:
                        tempstring = "- x"
                        polystring += tempstring + " "
                    elif j[0] < 0.0:
                        tempstring = "- {}x".format(str(int(abs(j[0]))))
                        polystring += tempstring + " "
                else:
                    if j[0] == 1.0:
                        tempstring = "x^{}".format(str(int(j[1])))
                        polystring += tempstring + " "
                    elif j[0] > 0.0:
                        tempstring = "{}x^{}".format(str(int(j[0])), str(int(j[1])))
                        polystring += tempstring + " "
                    elif j[0] == -1.0:
                        tempstring = "- x^{}".format(str(int(j[1])))
                        polystring += tempstring + " "
                    elif j[0] < 0.0:
                        tempstring = "- {}x^{}".format(str(int(abs(j[0]))), str(int(j[1])))
                        polystring += tempstring + " "
            else:
                if j[1] == 0:
                    if j[0] > 0:
                        tempstring = "+ {}".format(str(int(j[0])))
                        polystring += tempstring + " "
                    elif j[0] < 0:
                        tempstring = "- {}".format(str(int(abs(j[0]))))
                        polystring += tempstring + " "
                elif j[1] == 1.0:
                    if j[0] == 1.0:
                        tempstring = "+ x"
                        polystring += tempstring + " "
                    if j[0] > 1.0:
                        tempstring = "+ {}x".format(str(int(j[0])))
                        polystring += tempstring + " "
                    elif j[0] == -1.0:
                        tempstring = "- x"
                        polystring += tempstring + " "
                    elif j[0] < -1.0:
                        tempstring = "- {}x".format(str(int(abs(j[0]))))
                        polystring += tempstring + " "
                else:
                    if j[0] == 1.0:
                        tempstring = "+ x^{}".format(str(int(j[1])))
                        polystring += tempstring + " "
                    elif j[0] > 1.0:
                        tempstring = "+ {}x^{}".format(str(int(j[0])), str(int(j[1])))
                        polystring += tempstring + " "
                    elif j[0] == -1.0:
                        tempstring = "- x^{}".format(str(int(j[1])))
                        polystring += tempstring + " "
                    elif j[0] < -1.0:
                        tempstring = "- {}x^{}".format(str(int(abs(j[0]))), str(int(j[1])))
                        polystring += tempstring + " "
    return polystring


def poly_format(poly, var):
    if '(' in poly:
        coeffpower = []
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
                coeffpower.append(poly_conversion_array(k, var))
            elif '(' in k and ')' in k:
                k = re.split('\(|\)', k)
                temp = polyop.poly_poly_multiplication(poly_conversion_array(k[1], var),
                                                       poly_conversion_array(k[2], var))
                if k[0] != '':
                    if k[0] == '-':
                        temp = polyop.poly_scalar_multiplication(temp, -1)
                    elif k[0] != '+':
                        temp = polyop.poly_scalar_multiplication(temp, float(k[0]))

                coeffpower.append(temp)

        for m in range(len(coeffpower)):
            for n in range(len(coeffpower[m])):
                final.append(coeffpower[m][n])
    else:
        final = poly_conversion_array(poly, var)

    return polyop.poly_sort(polyop.poly_consolidate(final))
