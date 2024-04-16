import tkinter as tk
from tkinter import ttk

def button_func():
    # content of entry_text
    entry_text = entry.get()

    # updating the label
    # label.configure(text = entry_text) or
    label["text"] = entry_text
    entry["state"] = "disabled"

def reset_func():
    label["text"] = "Some text"
    entry["state"] = "enabled"
     
# window 
window = tk.Tk()
window.geometry("500x300")
window.title("Getting and setting widgets")

# label
label = ttk.Label(master=window, text="Some text")
label.pack()

# entry
entry = ttk.Entry(master=window)
entry.pack()

# button
button = ttk.Button(master=window, text="Click me!", command=button_func)
button.pack()

reset_button = ttk.Button(master=window, text="Reset", command=reset_func)
reset_button.pack()

# run
window.mainloop()