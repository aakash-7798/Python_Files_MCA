# 4. Write a Python program that simulates a traffic light. The program lets the user select one of
# three lights: red, yellow, or green. When a radio button is selected, the light is turned on, and
# only one light can be on at a time. No light is on when the program starts.

from tkinter import *

main_window = Tk()

main_window.title('Traffic Lights')

main_window.geometry('600x300')


# Note Variable Declaration is very important because we want all radio buttons
# to be deselected so when we don't declare below variable
# The default for tristatevalue is the empty string, and the default value for a StringVar is the empty string.
# For your second set of radiobuttons both the variable value and the tristatevalue are the same
# so we are seeing the "tri-state mode"

v = StringVar(main_window,'ryg')

rbt_red = Radiobutton(main_window,text="Red",font=20,indicatoron=0,variable=v,value='red',selectcolor='red')
rbt_yellow = Radiobutton(main_window,text="Yellow",font=20,indicatoron=0,variable=v,value='yellow',selectcolor='yellow')
rbt_green = Radiobutton(main_window,text="Green",font=20,indicatoron=0,variable=v,value='green',selectcolor='green')


rbt_red.pack(side=TOP,ipadx=100,ipady=20,pady=15)
rbt_yellow.pack(side=TOP,ipadx=100,ipady=20,pady=15)
rbt_green.pack(side=TOP,ipadx=100,ipady=20,pady=15)


main_window.mainloop()