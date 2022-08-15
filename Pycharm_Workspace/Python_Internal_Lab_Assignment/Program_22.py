
## Written by Aakash Nadupalli

# 22.Write a Python program for copying the contents of one file into another. Pass the
# file names as command-line arguments. Handle the exceptions that may arise
# during the file operations.

# Assuming the files present in current working directory

import sys
import os

def show_contents_of_file(fl):
    try:
        with open(fl,'r') as f:
            print(f.read())
    except FileNotFoundError as ffe:
        print(ffe)

def copy_contents_oneFile_to_anotherFile(f1,f2):
    try:
        with open(f1,'r') as f1 ,open(f2,'a') as f2:
            f2.write('\n')    # Starts from new line
            for i in f1:
                f2.write(i)
    except FileNotFoundError as fl:
        print(fl)


print("First File Contents : ")
show_contents_of_file(sys.argv[1])
print()
print("Second File Contents : ")
show_contents_of_file(sys.argv[2])
print()

copy_contents_oneFile_to_anotherFile(sys.argv[1],sys.argv[2])

print("First File Contents : ")
show_contents_of_file(sys.argv[1])
print()
print("Second File Contents : ")
show_contents_of_file(sys.argv[2])
print()

## In Command Line just type like python Program_22.py  here mention the path where file exists  (No inverted commas )
# eg.   python Program_22.py File.txt File1.txt   (mention the file name also)

# In pycharm click on dropdown list which is exactly left to run toggle button  (run symbol present right corner 2nd row)
# After that click on Edit Configuration  then a dialog box will be appeared see the parameter option
# In Parameters specify just parameters that you want to pass like  File.txt File1.txt no need of python Program_29.py
