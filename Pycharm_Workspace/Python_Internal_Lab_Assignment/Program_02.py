
#  Written by Aakash Nadupalli

# 2. Write a Python program that will prompt the user for a file name, read all the lines
# from the file into a list, sort the list, and then print the lines in sorted order.

# Assuming the file present in current working directory and file extension is txt

import os

print(os.getcwd())  # this prints the current working directory

filename = input("Enter FileName : ")
filepath = f'./{filename}.txt'     # If you want from other directory just specify the path here

if os.path.isfile(filepath):
    print("File Exists")
    with open(filepath,'r') as f:
        print(sorted(f.readlines()))
else:
    print("File Does not Exist ..    \n"
          "Make sure to write the names with proper cases.. filename checking is case sensitive")