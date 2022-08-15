
# Written by Aakash Nadupalli

# 25.Write a Python program for generating fibonacci sequence.


def fib(n):
    if n < 2:
        if n >= 0:
            return n
        else:
            return "Negative Number.... Consideration"
    else:
        return fib(n-2)+fib(n-1)


n  = int(input("Enter Number : "))
print([fib(i) for i in range(n)])