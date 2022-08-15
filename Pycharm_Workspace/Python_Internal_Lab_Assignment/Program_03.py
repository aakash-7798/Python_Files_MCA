
#  Written by Aakash Nadupalli

# 3. Write a Python program that asks the user for a file name, and then prints the number
# of characters, words, and lines in the file.

# Assuming the file present in current working directory and file extension is txt

import os

print(os.getcwd())  # this prints the current working directory

filename = input("Enter FileName : ")
filepath = f'./{filename}.txt'     # If you want from other directory just specify the path here

if os.path.isfile(filepath):
    print("File Exists\n")
    with open(filepath,'r') as f:
        lines,words,characters = 0,0,0
        for i in f.readlines():
            lines += 1
            words += len(i.split())
            characters += len(i)
        print("Number of Lines -> ",lines)
        print("Number of Words -> ", words)
        print("Number of Characters -> ", characters)
else:
    print("File Does not Exist ..    \n"
          "Make sure to write the names with proper cases.. filename checking is case sensitive")