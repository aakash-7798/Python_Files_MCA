# 2. Develop a Python GUI program that receives an integer in one text field, and computes
# its factorial Value and fills it in another text field, when the button named “Compute” is
# clicked.


from tkinter import *

main_window = Tk()

main_window.title("Factorial Calculator")

main_window.geometry('1000x200')

def fact(n):
    if n <= 1:
        return 1
    else:
        return n*fact(n-1)

def show_output():
    inpt = input_txt.get("1.0","end-1c")
    if inpt.isnumeric():
        output_txt.delete('1.0',END)
        output_txt.insert(END,fact(int(inpt)))
        output_txt.pack()
        # output_txt.configure(bg="green",font=("Times Roman",13),fg="white")
    else:
        output_txt.delete('1.0',END)
        output_txt.insert(END,'invalid literal for int() with base 10...  Enter Only Integers...')
        output_txt.pack()


Label(main_window,text="Enter Number ",font=20).pack()
input_txt = Text(main_window,height=3,width=100)
bt = Button(main_window,text="Compute",font=20,command=show_output)
output_txt = Text(main_window,height=3,width=100)
input_txt.pack()
bt.pack(pady=10)
# output_txt.pack()
main_window.mainloop()