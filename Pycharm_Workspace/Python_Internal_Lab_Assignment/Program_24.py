
# Written by Aakash Nadupalli

# 24.Write a Python program for generating all the prime numbers between 1 and N
# where N is a value supplied by the user.
import math

def check_prime_or_not(n):
    i = 2
    while i**2 <= n:
        if n % i == 0:
            return False
        i += 1
    return True


# def check_prime_or_not(n):
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     else:
#         return True


def generate_prime_numbers(n):
    prm = []
    for i in range(2,n):
        if check_prime_or_not(i):
            prm.append(i)
    return prm


N = int(input("Enter Value of N : "))
print("Prime Numbers -> ",generate_prime_numbers(N))
# print(check_prime_or_not(5))

