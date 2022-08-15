
# Written by Aakash Nadupalli

# 11.Write a Python program that implements insertion sort for sorting a list of integers
# in ascending order.

def insertion_sort(lst):
    for i in range(len(lst)):
        j = i-1
        while j >= 0:
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
            j -= 1
    return lst


lst = [5,7,8,3,10,15,35,89,2,4,6]
print("Unsorted List ->",lst)
print("Sorted List -> ",insertion_sort(lst))
