import tkinter as tk
from tkinter import ttk

def button_func(entry_string):
    print("A button was pressed.")
    print(entry_string.get())

def outer_func(parameter):
    def inner_func():
        print("A button pressed.")
        print(parameter.get())
    return inner_func

# setup
window = tk.Tk()
window.title("buttons, functions and arguments.")
window.geometry("500x300")

# widget
entry_string = tk.StringVar(value="test")
entry = ttk.Entry(window, textvariable=entry_string)
entry.pack()

button = ttk.Button(window, text="Button", command=lambda: button_func(entry_string))
button.pack()
# run
window.mainloop() 