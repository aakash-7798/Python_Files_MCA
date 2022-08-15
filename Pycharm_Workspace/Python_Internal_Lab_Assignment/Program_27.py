
# Written By Aakash Nadupalli

# 27.Write a Python program that counts the occurrences of words in a text file and
# displays the words and their frequency counts.


#
with open("New_File.txt",'r') as f:
    dt = {}    # -> dictionary
    Words = f.read().split()
    for i in Words:
        if i not in dt:
            dt[i] = 0
        if i in dt:
            dt[i] += 1
    print(dt)

    # print(sorted(dt.items(),key=lambda x:x[1],reverse=True))


