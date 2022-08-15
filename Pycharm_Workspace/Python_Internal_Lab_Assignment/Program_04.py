
# Written by Aakash Nadupalli

# 4. Write a Python program that will prompt the user for a string and a file name, and then
# print all lines in the file that contain the string.

import os

print(os.getcwd())  # this prints the current working directory

filename = input("Enter FileName : ")
strg = input("Enter String : ")
filepath = f'./{filename}.txt'     # If you want from other directory just specify the path here

if os.path.isfile(filepath):
    print("File Exists")
    with open(filepath,'r') as f:
        for i in f.read().splitlines():
            if strg in i:
                print(i)

else:
    print("File Does not Exist ..    \n"
          "Make sure to write the names with proper cases.. filename checking is case sensitive")