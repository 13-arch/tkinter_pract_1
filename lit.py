from tkinter import *       # стандарт
from tkinter.ttk import *   # более свежее оформление
import TKinterModernThemes

def clicked():
    from tkinter import messagebox

    messagebox.showinfo('Кнопка нажата', 'Клик') # сообщение в отдельном месседжбоксе
    print('Клик')


if __name__ == '__main__':
    root = Tk() # инициализация окна
    root.title("Имя окна") # имя окна
    root.geometry('400x400') # размер окна
    style = Style() # инициируем использование стилей
    style.theme_use('TKinterModernThemes') # выбираем тему
    root.option_add("*tearOff", FALSE) # выключаем ненужные штрихи во всех меню сразу

    # наваливаем фактуры
    label = Label(root, text='Это метка') # добавлям метку
    # label.grid(column=0, row=0)           # местоположение метки по сетке
    label.place(x=200,y=10)              # местоположение метки по пикселям

    button = Button(root, text='Клик', command=clicked) # добавлям кнопку
    button.place(x=100,y=100)

    entry = Entry(root) # добавлям поле ввода
    entry.place(x=200,y=100)

    # text = Text(root, wrap='word') # добавлям текст, И ЗАМЕНЯЕМ ПОЛЕ ВВОДА
    # entry.place(x=100,y=200)

    languages = ["Python", "JavaScript", "C#", "Java"]
    languages_var = Variable(value=languages)
    listbox = Listbox(listvariable=languages_var) # добавлям список
    listbox.place(x=200, y=200)

    checkbutton = Checkbutton(text='чекбокс') # добавлям чекбокс
    checkbutton.place(x=100, y=200)

    radiobutton1 = Radiobutton(text='радиокнопка 1', value="Value 1", variable="Value 1") # добавлям радиокнопки
    radiobutton2 = Radiobutton(text='радиокнопка 2', value="Value 2", variable="Value 1") # их должно быть хотя бы две - одна из них будет заполнена по умолчанию
    radiobutton1.place(x=50, y=230)
    radiobutton2.place(x=50, y=250)

    verticalScale = Scale(orient=VERTICAL, length=200, from_=1.0, to=100.0) # добавлям вертикальный ползунок
    verticalScale.place(x=10, y=100)
    
    horizontalScale = Scale(orient=HORIZONTAL, length=150, from_=1.0, to=100.0) # добавлям горизонтальный ползунок
    horizontalScale.place(x=30, y=350)

    file_menu = Menu() # добавлям вложенное меню
    file_menu.add_cascade(label="Save") # добавляем пункты меню
    file_menu.add_cascade(label="Save as")
    file_menu.add_cascade(label="Open")
    file_menu.add_cascade(label="Click", command=clicked)
    main_menu = Menu() # добавлям основное меню
    main_menu.add_cascade(label="File", menu=file_menu)
    main_menu.add_cascade(label="Edit")
    main_menu.add_cascade(label="View")
    
    root.config(menu=main_menu) # отображаем меню в окне
    root.mainloop() # отображение окна