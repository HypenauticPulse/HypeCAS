import tkinter as tk
from polynomials.Polynomial import Polynomial
from polyutil import polyconvert as polycon, polyoperations as polyop


class GenOperationWindow:
    def __init__(self, title, sign):
        self.title = title
        self.sign = sign

    def gen_window(self):
        def win_execute():
            poly1 = Polynomial(ent_first.get(), "x")
            poly2 = Polynomial(ent_second.get(), "x")
            if self.sign == "+":
                result = poly1 + poly2
            elif self.sign == "-":
                result = poly1 - poly2
            elif self.sign == "x":
                result = poly1 * poly2
            lbl_result["text"] = polycon.poly_conversion_string(result)

        window = tk.Tk()

        window.rowconfigure([0, 1], minsize=50, weight=1)
        window.columnconfigure([0], minsize=50, weight=1)

        frm_win_title = tk.Frame(master=window)
        frm_win_title.grid(row=0, column=0)

        lbl_win_title = tk.Label(master=frm_win_title, text=self.title)
        lbl_win_title.grid(row=0, column=0)

        frm_win_main = tk.Frame(master=window)
        frm_win_main.grid(row=1, column=0)

        frm_win_main.rowconfigure([0, 1, 2, 3], minsize=50, weight=1)
        frm_win_main.columnconfigure([0, 1, 2, 3, 4], minsize=50, weight=1)

        lbl_first = tk.Label(master=frm_win_main, text="First polynomials:")
        lbl_first.grid(row=1, column=0)

        lbl_second = tk.Label(master=frm_win_main, text="Second polynomials:")
        lbl_second.grid(row=1, column=2)

        ent_first = tk.Entry(master=frm_win_main)
        ent_first.grid(row=2, column=0)

        ent_second = tk.Entry(master=frm_win_main)
        ent_second.grid(row=2, column=2)

        lbl_sign = tk.Label(master=frm_win_main, text=self.sign)
        lbl_sign.grid(row=2, column=1)

        lbl_equals = tk.Label(master=frm_win_main, text="=")
        lbl_equals.grid(row=2, column=3)

        lbl_result = tk.Label(master=frm_win_main, text="")
        lbl_result.grid(row=2, column=4)

        btn_submit = tk.Button(master=frm_win_main, text="Submit", command=win_execute)
        btn_submit.grid(row=3, column=1)

    def gendivwindow(self):
        def win_execute():
            poly1 = Polynomial(ent_first.get(), 'x')
            poly2 = Polynomial(ent_second.get(), 'x')
            [quotient, remainder] = polyop.poly_poly_division(poly1.exprArray, poly2.exprArray)
            if quotient == -1 and remainder == -1:
                lbl_res_quotient["text"] = "Error, divisor is zero"
                lbl_res_remainder["text"] = ""
            else:
                lbl_res_quotient["text"] = polycon.poly_conversion_string(quotient)
                lbl_res_remainder["text"] = polycon.poly_conversion_string(remainder)

        window = tk.Tk()

        window.rowconfigure([0, 1], minsize=50, weight=1)
        window.columnconfigure([0], minsize=50, weight=1)

        frm_win_title = tk.Frame(master=window)
        frm_win_title.grid(row=0, column=0)

        lbl_win_title = tk.Label(master=frm_win_title, text=self.title)
        lbl_win_title.grid(row=0, column=0)

        frm_win_main = tk.Frame(master=window)
        frm_win_main.grid(row=1, column=0)

        frm_win_main.rowconfigure([0, 1, 2, 3], minsize=50, weight=1)
        frm_win_main.columnconfigure([0, 1, 2, 3, 4], minsize=50, weight=1)

        lbl_first = tk.Label(master=frm_win_main, text="First polynomials:")
        lbl_first.grid(row=1, column=0)

        lbl_second = tk.Label(master=frm_win_main, text="Second polynomials:")
        lbl_second.grid(row=1, column=2)

        ent_first = tk.Entry(master=frm_win_main)
        ent_first.grid(row=2, column=0)

        ent_second = tk.Entry(master=frm_win_main)
        ent_second.grid(row=2, column=2)

        lbl_sign = tk.Label(master=frm_win_main, text=self.sign)
        lbl_sign.grid(row=2, column=1)

        lbl_equals = tk.Label(master=frm_win_main, text="->")
        lbl_equals.grid(row=2, column=3)

        btn_submit = tk.Button(master=frm_win_main, text="Submit", command=win_execute)
        btn_submit.grid(row=3, column=1)

        frm_win_result = tk.Frame(master=frm_win_main)
        frm_win_result.grid(row=2, column=4)

        frm_win_result.rowconfigure([0, 1], minsize=50, weight=1)
        frm_win_result.columnconfigure([0, 2], minsize=50, weight=1)

        lbl_quotient = tk.Label(master=frm_win_result, text="Quotient:")
        lbl_quotient.grid(row=0, column=0)

        lbl_remainder = tk.Label(master=frm_win_result, text="Remainder:")
        lbl_remainder.grid(row=1, column=0)

        lbl_res_quotient = tk.Label(master=frm_win_result, text="")
        lbl_res_quotient.grid(row=0, column=1)

        lbl_res_remainder = tk.Label(master=frm_win_result, text="")
        lbl_res_remainder.grid(row=1, column=1)

    def genrootswindow(self):
        def win_execute():
            poly = Polynomial(ent_first.get(), 'x')
            [zero1, zero2] = poly.zeros()
            if zero1 == 'C' and zero2 == 'C':
                lbl_res_zero1["text"] = "Roots are complex"
                lbl_res_zero2["text"] = ""
            elif zero1 == 'NaN' and zero2 == 'NaN':
                lbl_res_zero1["text"] = "Error: Polynomial is not quadratic"
                lbl_res_zero2["text"] = ""
            else:
                lbl_res_zero1["text"] = zero1
                lbl_res_zero2["text"] = zero2

        window = tk.Tk()

        window.rowconfigure([0, 1], minsize=50, weight=1)
        window.columnconfigure([0], minsize=50, weight=1)

        frm_win_title = tk.Frame(master=window)
        frm_win_title.grid(row=0, column=0)

        lbl_win_title = tk.Label(master=frm_win_title, text=self.title)
        lbl_win_title.grid(row=0, column=0)

        frm_win_main = tk.Frame(master=window)
        frm_win_main.grid(row=1, column=0)

        frm_win_main.rowconfigure([0, 1, 2, 3], minsize=50, weight=1)
        frm_win_main.columnconfigure([0, 1, 2, ], minsize=50, weight=1)

        lbl_first = tk.Label(master=frm_win_main, text="Polynomial to find roots of:")
        lbl_first.grid(row=1, column=0)

        ent_first = tk.Entry(master=frm_win_main)
        ent_first.grid(row=2, column=0)

        lbl_sign = tk.Label(master=frm_win_main, text=self.sign)
        lbl_sign.grid(row=2, column=1)

        lbl_equals = tk.Label(master=frm_win_main, text="->")
        lbl_equals.grid(row=2, column=3)

        btn_submit = tk.Button(master=frm_win_main, text="Submit", command=win_execute)
        btn_submit.grid(row=3, column=1)

        frm_win_result = tk.Frame(master=frm_win_main)
        frm_win_result.grid(row=2, column=4)

        frm_win_result.rowconfigure([0, 1], minsize=50, weight=1)
        frm_win_result.columnconfigure([0, 2], minsize=50, weight=1)

        lbl_zero1 = tk.Label(master=frm_win_result, text="First Zero:")
        lbl_zero1.grid(row=0, column=0)

        lbl_zero2 = tk.Label(master=frm_win_result, text="Second Zero:")
        lbl_zero2.grid(row=1, column=0)

        lbl_res_zero1 = tk.Label(master=frm_win_result, text="")
        lbl_res_zero1.grid(row=0, column=1)

        lbl_res_zero2 = tk.Label(master=frm_win_result, text="")
        lbl_res_zero2.grid(row=1, column=1)
