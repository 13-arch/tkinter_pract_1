import datetime
from tkinter import *
from tkinter import ttk
from datetime import datetime as dt

if __name__ == '__main__':
    root = Tk()
    root.title("pupupu")
    root.geometry('500x500')

    root.tk.call("source", "breeze-dark/breeze-dark.tcl")
    ttk.Style().theme_use("breeze-dark")

    lbl = Label(root, text="Привет!", foreground="blue", font=("bold", 13, "italic"))
    lbl.pack(pady=20)

    e1 = Entry(root, width=20)
    e1.pack(pady=10)

    def insert_time():
        dt_now = dt.now().strftime("%d-%m-%Y %H:%M:%S")
        e1.delete(0, END)
        e1.insert(0, dt_now)

    btn = Button(root, text="Показать время", command=insert_time)
    btn.pack(pady=10)


    
    root.mainloop()
