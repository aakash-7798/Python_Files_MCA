
# Written by Aakash Nadupalli

# 13.Write a Python program that implements selection sort for sorting a list of integers
# in ascending order.

def selection_sort(lst):
    for i in range(len(lst)):
        m_id = i
        for j in range(i+1,len(lst)):
            if lst[m_id] > lst[j]:
                m_id = j
        lst[m_id],lst[i] = lst[i],lst[m_id]
    return lst


lst = [8,2,1,5,8,33,5,58,35,69,8,7,56]
print("Unsorted List -> ",lst)
print("Sorted List -> ",selection_sort(lst))
