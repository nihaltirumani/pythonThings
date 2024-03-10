import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

def add():
    error = None
    try:
        number1 = int(entry_int1.get())
        number2 = int(entry_int2.get())
        
        added_number = number1 + number2
        output_string.set(str(f"The result is : {added_number}"))
    except BaseException:
        output_string.set("Invalid Input")

    

# window
window = tk.Tk()
window.title("ADDER")
window.geometry("350x250")

# title
title_label = ttk.Label(master = window, text = "Please fill the following data", font = "Calibri 24 bold")
title_label.pack()

# input feild of num1
input_frame_num1 = ttk.Frame(master = window)

entry_int1 = tk.IntVar()
entry1 = ttk.Entry(master = input_frame_num1, textvariable = entry_int1)
num1_label = ttk.Label(master = input_frame_num1, text = "Number 1")

num1_label.pack(side = "left")
entry1.pack(side = "left")
input_frame_num1.pack(pady = 10)

# input feild of num2
input_frame_num2 = ttk.Frame(master = window)

entry_int2 = tk.IntVar()
entry2 = ttk.Entry(master = input_frame_num2, textvariable = entry_int2)
num2_label = ttk.Label(master = input_frame_num2, text = "Number 2")

num2_label.pack(side = "left")
entry2.pack(side = "left")
input_frame_num2.pack(pady = 10)

# Add button
button = ttk.Button(master = window, text = "Add", command = add)

button.pack(pady = 5)
 
# output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = "Output", font = "Calibri 24", textvariable = output_string)
output_label.pack(pady = 5)

# run
window.mainloop()