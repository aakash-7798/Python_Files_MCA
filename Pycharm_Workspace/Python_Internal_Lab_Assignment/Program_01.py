
#  Written by Aakash Nadupalli

# 1.Write a Python program that reads a list of names and ages, then prints the list sorted
# by age.


names_ages= [["karna",35],["bheema",52],["rama",48],["hanuma",47],["arjuna",45],["krishna",52]]
print("Names and Ages Before Sorting -> ",names_ages)
print("Name and Ages after Sorting -> ",sorted(names_ages,key=lambda x:x[1]))



