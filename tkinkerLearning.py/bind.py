import tkinter as tk
from tkinter import ttk

def get_pos(event):
    print(f"x: {event.x} y: {event.y}")
# window
window = tk.Tk()
window.geometry("600x500")
window.title("Event Binding")

# widget
text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text="A button")
button.pack()

button.bind("<Control-KeyPress-a>", lambda event: print(event))
window.bind("<Motion>", get_pos)
# run
window.mainloop()