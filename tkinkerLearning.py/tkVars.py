import tkinter as tk
from tkinter import ttk

def button_func():
    print(stringVar.get())
    stringVar.set("Button pressed!")

# window
window = tk.Tk()
window.title("Tkinter variables")
window.geometry("500x300")

# tkinter variable
stringVar = tk.StringVar()

# widgets
label = ttk.Label(master=window, text="Label", textvariable=stringVar )
label.pack()

entry = ttk.Entry(master=window, textvariable=stringVar )
entry.pack()

button = ttk.Button(master=window, text="Button", command=button_func)
button.pack()

# exercise variable
exercise_stringVar = tk.StringVar(value = "test")
#exercise_stringVar.set("test")

# exercise widgets
exercise_label = ttk.Label(master=window, text="Exercise label", textvariable=exercise_stringVar)
exercise_label.pack()

exercise_entry1 = ttk.Entry(master=window, textvariable=exercise_stringVar)
exercise_entry1.pack()

exercise_entry2 = ttk.Entry(master=window, textvariable=exercise_stringVar)
exercise_entry2.pack()

# run
window.mainloop()