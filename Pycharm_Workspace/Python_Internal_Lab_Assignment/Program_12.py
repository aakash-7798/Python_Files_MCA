
# Written by Aakash Nadupalli

# 12.Write a Python program that implements bubble sort for sorting a list of names
# in ascending order.

def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    return lst


lst = [78, 25, 14, 98, 35, 65, 78, 68, 1, 4, 23, 65]
print("Unsorted List -> ",lst)
print("Sorted List -> ",bubble_sort(lst))