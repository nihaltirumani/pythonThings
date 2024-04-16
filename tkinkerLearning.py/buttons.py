import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Buttons")
window.geometry("600x400")

# button
def button_func():
    print("A basic button pressed.")
    print(radio_var.get( ))

button_string = tk.StringVar(value="A button with string var")
button = ttk.Button(window, text="A simple button", command=button_func, textvariable=button_string)
button.pack()

# checkbutton
check_var = tk.IntVar(value=10)
check1 = ttk.Checkbutton(
    window,
    text="Checkbutton 1",
    command=lambda: print(check_var.get()),
    variable=check_var,
    onvalue=10,
    offvalue=5)
check1.pack()

check2 = ttk.Checkbutton(
    window,
    text="Checkbutton 2",
    command=lambda: check_var.set(5))
check2.pack()

# radiobutton
radio_var = tk.StringVar()
radiobutton1 = ttk.Radiobutton(
    window,
    text="Radiobutton1",
    value=1,
    variable=radio_var,
    command=lambda: print(radio_var.get())
)
radiobutton1.pack()

radiobutton2 = ttk.Radiobutton(window, text="Radiobutton2", value=2, variable=radio_var)
radiobutton2.pack()

# exercise checkbutton
exercise_checkvar = tk.BooleanVar(value=True)
exercise_check = ttk.Checkbutton(
    window,
    text="Exercise check box",
    variable=exercise_checkvar,
    onvalue=True,
    offvalue=False,
    command=lambda: print(exercise_radio_var.get())
)
exercise_check.pack()

# exercise radio button
def radio_func():
    print(exercise_checkvar.get())
    exercise_checkvar.set(False)

exercise_radio_var = tk.StringVar()
exercise_radiobutton1 = ttk.Radiobutton(
    window,
    text="Radiobutton1",
    value="A",
    variable=exercise_radio_var,
    command=radio_func
)
exercise_radiobutton1.pack()

exercise_radiobutton2 = ttk.Radiobutton(
    window,
    text="Radiobutton2",
    value="B",
    variable=exercise_radio_var,
    command=radio_func
)
exercise_radiobutton2.pack()

# run
window.mainloop()