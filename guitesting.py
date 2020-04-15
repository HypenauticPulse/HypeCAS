import tkinter as tk


def create_window():
    window = tk.Toplevel(root)


root = tk.Tk()

root.rowconfigure([0, 1], minsize=50, weight=1)
root.columnconfigure([0], minsize=50, weight=1)

b = tk.Button(root, text="Create new window", command=create_window)
b.grid(row=0, column=0)

root.mainloop()
