import tkinter as tk

# create a window
window = tk.Tk()
window.title("Window and widgets")
window.geometry("800x500")

# create widgets
tk.Text(master=window).pack()
# run
window.mainloop()