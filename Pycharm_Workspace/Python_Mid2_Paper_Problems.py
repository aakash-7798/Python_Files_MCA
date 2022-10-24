from tkinter import *

# 1 a
window = Tk()
window.title("ListBox Sort")
window.geometry("500x500")
colors = ["RED","BLACK",'YELLOW','WHITE','GREY','BROWN','BLUE','GREEN','VIOLET']

lb = Label(window,text="Right click on the Mouse",font=50)
lb.pack(pady=50)

def add_ele():
    lstbx.delete(0, END)
    for i in colors:
        lstbx.insert(END, i)
    lstbx.pack(pady=30)

def srt():
    lstbx.delete(0, END)
    for i in sorted(colors):
        lstbx.insert(END,i)
    lstbx.pack(pady=30)

def my_popup(e):
    mn.tk_popup(e.x_root,e.y_root)

lstbx = Listbox(window,height=9,width=25)
mn = Menu(window,tearoff=False)
mn.add_command(label="Add Elements into ListBox",command=add_ele)
mn.add_command(label="Sort",command=srt)
window.bind("<Button-3>",my_popup)
window.mainloop()







## 1.b
root = Tk()
root.title("ListBox with Scroll Bar")
root.geometry("500x300")

frm = Frame(root)
frm.place(x=150,y=80)

Lstbx = Listbox(frm,height=5,width=30,selectmode=BROWSE)
Lstbx.pack(side=LEFT,fill=Y)

scrbr = Scrollbar(frm,orient="vertical",command=Lstbx.yview)
scrbr.pack(side=RIGHT,fill=Y)

Lstbx.configure(yscrollcommand=scrbr.set)

colors = ["RED","BLACK",'YELLOW','WHITE','GREY','BROWN','BLUE','GREEN','VIOLET']
for i in colors:
    Lstbx.insert(END,i)

root.mainloop()



# # 2 a.)  Simple Temperature Conversion Calculator

# F = 32 + (9C/5)
# C = ((5*F)-160)/9

main_window = Tk()
main_window.title("Temperature Calculator")
main_window.geometry("500x200")

def calculate_celsius():
    lb_celsius.configure(text=f"Celsius = {round((5*float(ety.get()))-160/9,2)} C")
    lb_celsius.grid(row=8,columnspan=5,column=5,padx=30,ipadx=20,ipady=12)

def calculate_fahrenheit():
    lb_fahrenheit.configure(text=f"Fahrenheit = {round(32 + ((9*(float(ety.get())))/5),2)} F")
    lb_fahrenheit.grid(row=8,columnspan=5,column=5 ,padx=30,ipadx=20,ipady=12)

lb = Label(main_window,text="Enter Value ",font=25)
lb.grid(row=2,padx=90,columnspan=5,column=2)

lb_celsius = Label(main_window,font=30)

lb_fahrenheit = Label(main_window,font=30)

ety = Entry(width=20,font=25)
ety.grid(row=2,column=5,padx=180,pady=20,ipady=5,ipadx=10,columnspan=5)

btn_celsius = Button(main_window,text="CELSIUS",font=25,command=calculate_celsius)
btn_celsius.grid(row=4,columnspan=5,column=3,padx=30,ipadx=20,ipady=12)

btn_fahrenheit = Button(main_window,text="FAHRENHEIT",font=25,command=calculate_fahrenheit)
btn_fahrenheit.grid(row=4,columnspan=5,column=6,padx=30,ipadx=20,ipady=12)

main_window.mainloop()

