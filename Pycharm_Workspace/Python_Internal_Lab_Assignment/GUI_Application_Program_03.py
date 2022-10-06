# 3. Write a Python program that creates a user interface to perform integer divisions. The user
# enters two numbers in the text fields, Num1 and Num2. The division of Num1 and
# Num2 is displayed in the Result field when the Divide button is clicked. If Num1 or Num2
# were not an integer or Num2 is Zero, the program should display an appropriate message
# in the result field in Red color.

from tkinter import *

main_window = Tk()

main_window.title('Division Calculator')

main_window.geometry('750x300')

def calculate():
    inpt1 = input_txt1.get('1.0','end-1c')
    inpt2 = input_txt2.get('1.0','end-1c')
    if not inpt1.isalpha() and not inpt2.isalpha():
        if float(inpt2) != 0.0:
            output_txt.delete('1.0', END)
            output_txt.insert(END,float(inpt1)/float(inpt2))
            output_txt.configure(bg='white')
        elif float(inpt2) == 0.0:
            output_txt.delete('1.0', END)
            output_txt.insert(END, 'ZeroDivisionError: division by zero')
            output_txt.configure(bg="red")
        output_txt.grid(row=8, column=0, columnspan=6, padx=80, pady=20)
    else:
        output_txt.delete('1.0', END)
        output_txt.insert(END, 'invalid literal for int() with base 10...  Enter Only Integers...')
        output_txt.grid(row=8, column=0, columnspan=6, padx=80, pady=20)
        output_txt.configure(bg="red")


lb1 = Label(main_window,text="Num1 :")

lb2 = Label(main_window,text="Num2 :")

input_txt1 = Text(main_window,height=2,width=30)

input_txt2 = Text(main_window,height=2,width=30)

output_txt = Text(main_window,height=2,width=70)

btn = Button(main_window,text="Divide",font=20,command=calculate)

lb1.grid(row=1,column=0,padx=50)

input_txt1.grid(row=1,column=1,pady=20)

lb2.grid(row=4,column=0,padx=50)

input_txt2.grid(row=4,column=1,pady=20)

btn.grid(row=6,column=1,pady=20)

main_window.mainloop()