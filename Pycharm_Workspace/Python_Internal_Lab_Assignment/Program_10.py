
# Written by Aakash Nadupalli

# 10.Write a Python program that implements binary search method non recursively to
# search for an integer key in a sorted list of integers.

def quick_sort(lst):

    if len(lst) < 2:
        return lst

    else:
        pivot = lst[0]
        left = [i for i in lst[1:] if i < pivot]
        right = [i for i in lst[1:] if i > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


def binary_search(lst,key):
    lst = quick_sort(lst)
    lb = 0
    ub = len(lst)-1
    while lb <= ub:
        mid = lb+(ub-lb)//2
        if lst[mid] == key:
            return mid
        elif key<lst[mid]:
            ub = mid-1
        else:
            lb = mid+1
    return "Element Not Found"


lst = [5,7,8,3,10,15,35,89,2,4,6]
print(binary_search(lst,89))
print(binary_search(lst,4))
print(binary_search(lst,100))
