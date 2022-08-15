
# Written by Aakash Nadupalli

# 9. Write a Python program that implements binary search method recursively to search
# for an integer key in a sorted list of integers.

def quick_sort(lst):

    if len(lst) < 2:
        return lst

    else:
        pivot = lst[0]
        left = [i for i in lst[1:] if i < pivot]
        right = [i for i in lst[1:] if i > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


def binary_search(lst,lb,ub,key):
    lst = quick_sort(lst)
    if lb > ub:
        return "Element Not Found"
    else:
        mid = lb+(ub-lb)//2
        if lst[mid] == key:
            return mid
        elif key<lst[mid]:
            return binary_search(lst,lb,mid-1,key)
        else:
            return binary_search(lst,mid+1,ub,key)
    return "Element Not Found"


lst = [5,7,8,3,10,15,35,89,2,4,6]
print(binary_search(lst,0,len(lst)-1,89))
print(binary_search(lst,0,len(lst)-1,4))
print(binary_search(lst,0,len(lst)-1,100))
