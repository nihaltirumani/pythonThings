import tkinter as tk
from tkinter import ttk

# Create the main application window
root = tk.Tk()
root.title("Modern Yellow Menu")
root.geometry("600x400")
root.config(bg="#FFEB3B")  # Yellow background

# Styling
button_bg = "#FFD600"  # Darker yellow
button_fg = "black"
button_hover = "#FFC107"  # Slightly orange shade

# Sidebar frame
sidebar = tk.Frame(root, bg=button_bg, width=150, height=400)
sidebar.pack(side="left", fill="y")

# Main content area
content = tk.Frame(root, bg="white", width=450, height=400)
content.pack(side="right", fill="both", expand=True)

def on_hover(event):
    event.widget["background"] = button_hover

def on_leave(event):
    event.widget["background"] = button_bg

# Menu buttons
def create_menu_button(text, command):
    btn = tk.Button(sidebar, text=text, font=("Arial", 12), bg=button_bg, fg=button_fg, 
                    relief="flat", command=command, height=2, width=15)
    btn.pack(pady=5)
    btn.bind("<Enter>", on_hover)
    btn.bind("<Leave>", on_leave)
    return btn

def show_message(text):
    for widget in content.winfo_children():  # Clear previous content
        widget.destroy()
    label = tk.Label(content, text=text, font=("Arial", 18), bg="white")
    label.pack(expand=True)

# Creating buttons
btn_home = create_menu_button("Home", lambda: show_message("Welcome Home!"))
btn_settings = create_menu_button("Settings", lambda: show_message("Settings Page"))
btn_about = create_menu_button("About", lambda: show_message("About This App"))

root.mainloop()
