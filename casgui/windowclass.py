import tkinter as tk
import sys

sys.path.insert(0, '../')

import polyconvert as polycon


class GenOperationWindow:
    def __init__(self, title, operation, sign):
        self.title = title
        self.operation = operation
        self.sign = sign

    def genwindow(self):
        def win_execute():
            poly1 = polycon.poly_format(ent_first.get(), 'x')
            poly2 = polycon.poly_format(ent_second.get(), 'x')
            result = self.operation(poly1, poly2)
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

        lbl_first = tk.Label(master=frm_win_main, text="First polynomial:")
        lbl_first.grid(row=1, column=0)

        lbl_second = tk.Label(master=frm_win_main, text="Second polynomial:")
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
            poly1 = polycon.poly_format(ent_first.get(), 'x')
            poly2 = polycon.poly_format(ent_second.get(), 'x')
            [quotient, remainder] = self.operation(poly1, poly2)
            if quotient == -1 and remainder == -1:
                lbl_res_quotient["text"] = "Error, divisor is zero"
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

        lbl_first = tk.Label(master=frm_win_main, text="First polynomial:")
        lbl_first.grid(row=1, column=0)

        lbl_second = tk.Label(master=frm_win_main, text="Second polynomial:")
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
