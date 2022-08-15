
# Written by Aakash Nadupalli

# 29.Write a Python program to display the contents of a file to screen starting with
# the location that is specified on the command-line.

import sys
import os

Location = sys.argv[1]
lst_loc = Location.split('\\')
path = ''.join(lst_loc[:-1]+["\\"])

os.chdir(path)
print("\nLocation = ",os.getcwd())


if lst_loc[-1] in os.listdir():
    with open(lst_loc[-1],'r') as f:
        print(f.read())
else:
    print("File Not Present in the mentioned directory")


## In Command Line just type like python Program_29.py  here mention the path where file exists  (No inverted commas )
# eg.   python Program_29.py G:\File.txt    (mention the file name also)

# In pycharm click on dropdown list which is exactly left to run toggle button  (symbol present right corner 2nd row)
# After that click on Edit Configuration  then a dialog box will be appeared see the parameter option
# In Parameters specify just parameters that you want to pass like  G:\File.txt no need of python Program_29.py