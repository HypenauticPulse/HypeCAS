import tkinter as tk
import sys

sys.path.insert(0, '../')

import casgui.windowclass as wc
import polyoperations as polyop
import polyconvert as polycon

def gen_gui():
    add_window = wc.GenOperationWindow("Polynomial Addition", polyop.poly_addition, "+")
    sub_window = wc.GenOperationWindow("Polynomial Subtraction", polyop.poly_subtraction, "-")
    multi_window = wc.GenOperationWindow("Polynomial Multiplication", polyop.poly_poly_multiplication, "x")
    div_window = wc.GenOperationWindow("Polynomial Long Division", polyop.poly_poly_division, "/")

    root = tk.Tk()

    root.rowconfigure([0, 1], minsize=50, weight=1)
    root.columnconfigure([0], minsize=50, weight=1)

    frm_title = tk.Frame(master=root)
    frm_title.grid(row=0, column=0, sticky="n")

    lbl_title = tk.Label(master=frm_title, text="Choose your operation:")
    lbl_title.grid(row=0, column=1)

    frm_buttons = tk.Frame(master=root)
    frm_buttons.grid(row=1, column=0)

    frm_buttons.rowconfigure([0], minsize=50, weight=1)
    frm_buttons.columnconfigure([0, 1, 2, 3], minsize=50, weight=1)

    btn_addition = tk.Button(master=frm_buttons, text="Addition", command=add_window.genwindow)
    btn_addition.grid(row=0, column=0, sticky="nsew")

    btn_subtraction = tk.Button(master=frm_buttons, text="Subtraction", command=sub_window.genwindow)
    btn_subtraction.grid(row=0, column=1, sticky="nsew")

    btn_multiplication = tk.Button(master=frm_buttons, text="Multiplication", command=multi_window.genwindow)
    btn_multiplication.grid(row=0, column=2, sticky="nsew")

    btn_division = tk.Button(master=frm_buttons, text="Divison", command=div_window.gendivwindow)
    btn_division.grid(row=0, column=3, sticky="nsew")

    root.mainloop()

    return