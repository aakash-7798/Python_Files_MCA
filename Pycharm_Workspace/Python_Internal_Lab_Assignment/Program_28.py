
# Written By Aakash Nadupalli

# 28.Write a Python program to determine if the given string is a palindrome or not.

def IsPalindrome(st):
    if st == st[::-1]:
        return f'{st} is Palindrome'
    else:
        return f'{st} is not Palindrome'


lst = ['madam','dad',"mom","linked","array"]
for i in lst:
    print(IsPalindrome(i))