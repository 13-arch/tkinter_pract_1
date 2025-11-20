import csv
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

window = tk.Tk()
window.title('Авторизация')
import tkinter as tk

window.tk.call("source", "breeze-dark/breeze-dark.tcl")
ttk.Style().theme_use("breeze-dark")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
desired_width_percentage = 0.25
window_width = int(screen_width * desired_width_percentage)
aspect_ratio = 10 / 8
window_height = int(window_width * aspect_ratio)

if window_height > screen_height:
    window_height = screen_height

window.geometry(f"{window_width}x{window_height}")
window.bind("<Escape>", lambda e: window.destroy())

window.resizable(False, False)
window.overrideredirect(True)
font_header = ('Arial', 15)
font_entry = ('Arial', 12)
label_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}

main_label = tk.Label(window, text='плеер', font=font_header, justify=tk.CENTER, **header_padding)




window.mainloop()
