from tkinter import *
import math
import base64

#* COLORS
c1 = '#defcf9'; c2 = '#cadefc'
c3 = '#c3bef0'; c4 = '#cca8e9'

#* FUNCTIONS
def button_add(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))

def clear():
    e.delete(0, END)

def operacion(signo):
    first_num = e.get()
    global f_num
    f_num = float(first_num)
    global operand; operand = signo
    clear()

def igual():
    sencond_num = e.get()
    s_num = float(sencond_num)
    e.delete(0, END)
    if operand == '+':
        result = f_num + s_num
    elif operand == '-':
        result = f_num - s_num
    elif operand == '/':
        result = f_num / s_num
    elif operand == '*':
        result = f_num * s_num
    elif operand == '**':
        result = f_num ** s_num

    e.insert(0, "{:.2f}".format(result))

def raiz():
    num = e.get()
    sqr = "{:.2f}".format(math.sqrt(float(num)))
    e.delete(0, END)
    e.insert(0, float(sqr))

#* WINDOW
win = Tk()
win.iconbitmap('./calc-icon.ico')
win.configure(bg=c1)
win.title('Calculator')
win.resizable(width=False,height=False)
e = Entry(win,  borderwidth=5, font=('Varela Round Regular', 17), bd=0)
#e.grid(row=0, column=0, ipadx=100, columnspan=6, padx=10, pady=10)
e.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

w=0;h=0;f=25;bd=0

button_1 = Button(win, border=2, font=('Varela Round Regular', f), relief=GROOVE, borderwidth=bd, activebackground=c3, bg=c1, text='1', width=w, height=h, command=lambda: button_add(1))
button_2 = Button(win, border=2, font=('Varela Round Regular', f), relief=GROOVE, borderwidth=bd, activebackground=c3, bg=c1, text='2', width=w, height=h, command=lambda: button_add(2))
button_3 = Button(win, border=2, font=('Varela Round Regular', f), relief=GROOVE, borderwidth=bd, activebackground=c3, bg=c1, text='3', width=w, height=h, command=lambda: button_add(3))
button_4 = Button(win, border=2, font=('Varela Round Regular', f), relief=GROOVE, borderwidth=bd, activebackground=c3, bg=c1, text='4', width=w, height=h, command=lambda: button_add(4))
button_5 = Button(win, border=2, font=('Varela Round Regular', f), relief=GROOVE, borderwidth=bd, activebackground=c3, bg=c1, text='5', width=w, height=h, command=lambda: button_add(5))
button_6 = Button(win, border=2, font=('Varela Round Regular', f), relief=GROOVE, borderwidth=bd, activebackground=c3, bg=c1, text='6', width=w, height=h, command=lambda: button_add(6))
button_7 = Button(win, border=2, font=('Varela Round Regular', f), relief=GROOVE, borderwidth=bd, activebackground=c3, bg=c1, text='7', width=w, height=h, command=lambda: button_add(7))
button_8 = Button(win, border=2, font=('Varela Round Regular', f), relief=GROOVE, borderwidth=bd, activebackground=c3, bg=c1, text='8', width=w, height=h, command=lambda: button_add(8))
button_9 = Button(win, border=2, font=('Varela Round Regular', f), relief=GROOVE, borderwidth=bd, activebackground=c3, bg=c1, text='9', width=w, height=h, command=lambda: button_add(9))
button_0 = Button(win, border=2, font=('Varela Round Regular', f), relief=GROOVE, borderwidth=bd, activebackground=c3, bg=c1, text='0', width=w, height=h, command=lambda: button_add(0))

button_punto  = Button(win, border=2, font=('Varela Round Regular', f), relief=GROOVE, borderwidth=bd, activebackground=c3, bg=c1, text=',', width=w, height=h, command=lambda: button_add('.'))
button_mas    = Button(win, border=2, font=('Varela Round Regular', f), relief=GROOVE, borderwidth=bd, activebackground=c3, bg=c1, text='+', width=w, height=h, command=lambda: operacion('+'))
button_igual  = Button(win, border=2, font=('Varela Round Regular', f), relief=GROOVE, borderwidth=bd, activebackground=c3, bg=c1, text='=', width=w, height=h, command=lambda: igual())
button_clear  = Button(win, border=2, font=('Varela Round Regular', f), relief=GROOVE, borderwidth=bd, activebackground=c3, bg=c1, text='c', width=w, height=h, command=lambda: clear())
button_menos  = Button(win, border=2, font=('Varela Round Regular', f), relief=GROOVE, borderwidth=bd, activebackground=c3, bg=c1, text='-', width=w, height=h, command=lambda: operacion('-'))
button_x      = Button(win, border=2, font=('Varela Round Regular', f), relief=GROOVE, borderwidth=bd, activebackground=c3, bg=c1, text='x', width=w, height=h, command=lambda: operacion('*'))
button_divide = Button(win, border=2, font=('Varela Round Regular', f), relief=GROOVE, borderwidth=bd, activebackground=c3, bg=c1, text='/', width=w, height=h, command=lambda: operacion('/'))
button_pow    = Button(win, border=2, font=('Varela Round Regular', f), relief=GROOVE, borderwidth=bd, activebackground=c3, bg=c1, text='^', width=w, height=h, command=lambda: operacion('**'))
button_raiz   = Button(win, border=2, font=('Varela Round Regular', f), relief=GROOVE, borderwidth=bd, activebackground=c3, bg=c1, text='√', width=w, height=h, command=lambda: raiz())

#? GRID BUTTONS

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_punto.grid(row=4,column=1)

button_clear.grid(row=1,column=5)
button_mas.grid(row=4,column=4)
button_igual.grid(row=4,column=5)
button_menos.grid(row=3,column=4)
button_x.grid(row=2,column=4)
button_divide.grid(row=1,column=4)
button_pow.grid(row=3,column=5)
button_raiz.grid(row=2,column=5)

win.mainloop()
