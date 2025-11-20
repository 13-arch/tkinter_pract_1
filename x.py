import csv
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.withdraw()

def create_many_windows(num_windows):
    for i in range(num_windows):
        new_window = tk.Toplevel(window) 
        new_window.title(f"Ошибка {i+1}")
        new_window.geometry("250x120")  
        error_label = tk.Label(
            new_window, 
            text=":) ХАХА :)", 
            fg="red", 
            font=('Arial', 10)
        )
        error_label.pack(expand=True)

num_windows_to_create = 10

create_many_windows(num_windows_to_create)

window.mainloop()
