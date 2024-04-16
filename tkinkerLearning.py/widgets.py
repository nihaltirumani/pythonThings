import tkinter as tk
from tkinter import ttk

def button_func():
    print("Button was pressed!!")

def print_hello():
    print("Hello")

# create a window
window = tk.Tk()
window.title("Window and widgets")
window.geometry("800x500")

# ttk label
label = ttk.Label(master=window, text="This is text")
label.pack()

# tk text
text = tk.Text(master=window)
text.pack()

# ttk entry
entry = ttk.Entry(master=window)
entry.pack()

# my label
my_label = ttk.Label(master=window, text="My label")
my_label.pack()

# ttk button
button = ttk.Button(master=window, text="Click me!", command=button_func)
button.pack()

# Button that prints "Hello"
button_1 = ttk.Button(master=window, text="print", command=print_hello)
button_1.pack()

# run 
window.mainloop()