import csv
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('Авторизация')
window.geometry('450x230')
window.resizable(True, True)

font_header = ('Arial', 15)
font_entry = ('Arial', 12)
label_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}

def load_users(filename="users.csv"):
    users = {}
    with open(filename, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            users[row["name"]] = row["password"]
    return users

users = load_users("users.csv")

def create_many_windows(num_windows):
    for i in range(num_windows):
        new_window = tk.Toplevel(window) 
        new_window.title(f"Ошибка {i+1}")
        new_window.geometry("250x120")  
        error_label = tk.Label(new_window, text="Неверное имя пользователя или пароль!", 
                               fg="red", font=('Arial', 10))
        error_label.pack(expand=True)

num_windows_to_create = 5

def clear_and_add_widgets(username):
    for widget in window.winfo_children():
        widget.destroy()
    label = tk.Label(window, text=f"Добро пожаловать, {username}!", font=('Arial', 16), fg="green")
    label.pack(expand=True)

def clicked():
    username = username_entry.get()
    password = password_entry.get()
    if username in users and users[username] == password:
        clear_and_add_widgets(username)
    else:
        create_many_windows(num_windows_to_create)

main_label = tk.Label(window, text='Авторизация', font=font_header, justify=tk.CENTER, **header_padding)
main_label.pack()

username_label = tk.Label(window, text='Имя пользователя', font=label_font, **base_padding)
username_label.pack()

username_entry = tk.Entry(window, bg='#fff', fg='#444', font=font_entry)
username_entry.pack()

password_label = tk.Label(window, text='Пароль', font=label_font, **base_padding)
password_label.pack()

password_entry = tk.Entry(window, bg='#fff', fg='#444', font=font_entry, show="*")
password_entry.pack()

send_btn = tk.Button(window, text='Войти', command=clicked)
send_btn.pack(**base_padding)

window.mainloop()
