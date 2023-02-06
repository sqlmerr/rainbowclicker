from tkinter import *
from random import choice

# переменные
gray = '#696969'
num = 0
app = Tk()
app.title('Rainbow clicker')
app.geometry('640x450')
app.resizable(False, False)
colors = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
fn = "Arial Bold"
fnR = 50

app.configure(bg=gray)

# функция при нажатии кнопки
def click():
    global num
    num += 1
    btn.configure(text=num)
    color = '#'
    for i in range(6):
        color += choice(colors)
    btn.configure(bg=color, activebackground=color)


# функция изменения цвета фона
def color_change():
    color = '#'
    for i in range(6):
        color += choice(colors)
    app.configure(bg=color)
    lbl.configure(bg=color)


lbl = Label(app, text='click!', font=(fn, fnR), bg=gray, fg='white')
lbl.place(x=110, y=50, height=100, width=400)

btn = Button(app, text=num, bg='#ffffff', fg='black', font=(fn, fnR), command=click)
btn.place(x=180, y=180, height=100, width=250)

clrchange = Button(app, text='изменить цвет фона', bg='black', fg='white', font=(fn, 30), command=color_change)
clrchange.place(x=110, y=350, height=60, width=400)

#txt = Entry(app, font=(fn, fnR))
#txt.place(x = 110, y = 300, height=100, width=400)

app.mainloop()