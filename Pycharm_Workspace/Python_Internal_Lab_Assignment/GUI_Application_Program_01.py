# 1. Write a Python program that works as a simple calculator. Use a grid to arrange buttons
# for the digits and for the +, -,*, % operations. Add a text field to display the result.

from tkinter import *

main_window = Tk()

main_window.geometry('320x400')

txt = Text(main_window,height=2,width=35,border=2,font=30)
txt.grid(row=1,columnspan=5,column=0)

def button_click(number):
    txt.insert(END,number)

def button_add():
    global g_num
    global status
    status = 'Addition'
    g_num = txt.get('1.0', 'end-1c')
    button_clear()

def button_subtract():
    global g_num
    global status
    status = 'Subtraction'
    g_num = txt.get('1.0', 'end-1c')
    button_clear()

def button_multpily():
    global g_num
    global status
    status = 'Multiplication'
    g_num = txt.get('1.0', 'end-1c')
    button_clear()


def button_divide():
    global g_num
    global status
    status = "Division"
    g_num = txt.get('1.0', 'end-1c')
    button_clear()

def button_percentage():
    global g_num
    global status
    status = "Percentage"
    g_num = txt.get('1.0', 'end-1c')
    button_clear()

def button_equal():
    number2 = txt.get('1.0','end-1c')
    button_clear()
    if status == "Addition":
        txt.insert(END,eval(f'{g_num}+{number2}'))
    elif status == "Subtraction":
        txt.insert(END,eval(f'{g_num}-{number2}'))
    elif status == "Multiplication":
        txt.insert(END,eval(f'{g_num}*{number2}'))
    elif status == "Division":
        if number2 == '0':
            txt.insert(END, 'Zero Division Error')
        else:
            txt.insert(END,eval(f'{g_num}/{number2}'))
    elif status == "Percentage":
        print(number2)
        txt.insert(END, float(g_num)/100)

def button_clear():
    txt.delete('1.0',END)

Button(main_window,text='Clear',padx=50,pady=20,font=20,command=button_clear)  .grid(row=7,column=0,columnspan=2)

Button(main_window,text='=',padx=70,pady=20,font=20,command=button_equal)      .grid(row=7,column=2,columnspan=2)

Button(main_window,text=0,padx=29,pady=20,font=20,command=lambda :button_click(0))        .grid(row=6,column=0,columnspan=1)

Button(main_window,text='.',padx=29,pady=20,font=20,command=lambda :button_click('.'))      .grid(row=6,column=1,columnspan=1)

Button(main_window,text='%',padx=29,pady=20,font=20,command=button_percentage)      .grid(row=6,column=2,columnspan=1)

Button(main_window,text='/',padx=29,pady=20,font=20,command=button_divide)      .grid(row=6,column=3,columnspan=1)

Button(main_window,text=1,padx=29,pady=20,font=20,command=lambda :button_click(1))        .grid( row=5,column=0,columnspan=1)

Button(main_window,text=2,padx=29,pady=20,font=20,command=lambda :button_click(2))        .grid(row=5,column=1,columnspan=1)

Button(main_window,text=3,padx=29,pady=20,font=20,command=lambda :button_click(3))        .grid(row=5,column=2,columnspan=1)

Button(main_window,text='*',padx=29,pady=20,font=20,command=button_multpily)      .grid(row=5,column=3,columnspan=1)

Button(main_window,text=4,padx=29,pady=20,font=20,command=lambda :button_click(4))        .grid( row=4,column=0,columnspan=1)

Button(main_window,text=5,padx=29,pady=20,font=20,command=lambda :button_click(5))        .grid(row=4,column=1,columnspan=1)

Button(main_window,text=6,padx=29,pady=20,font=20,command=lambda :button_click(6))        .grid(row=4,column=2,columnspan=1)

Button(main_window,text='-',padx=29,pady=20,font=20,command=button_subtract)      .grid(row=4,column=3,columnspan=1)

Button(main_window,text=7,padx=29,pady=20,font=20,command=lambda :button_click(7))        .grid( row=3,column=0,columnspan=1)

Button(main_window,text=8,padx=29,pady=20,font=20,command=lambda :button_click(8))        .grid(row=3,column=1,columnspan=1)

Button(main_window,text=9,padx=29,pady=20,font=20,command=lambda :button_click(9))        .grid(row=3,column=2,columnspan=1)

Button(main_window,text='+',padx=29,pady=20,font=20,command=button_add)      .grid(row=3,column=3,columnspan=1)

main_window.mainloop()