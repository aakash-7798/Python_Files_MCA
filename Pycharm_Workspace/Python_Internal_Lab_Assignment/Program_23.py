
# Written by Aakash Nadupalli

# 23.Write a Python program for adding two matrices.

M1 = [[1,2,3],
      [4,5,6],
      [7,8,9]]

M2 = [[10,11,12],
      [13,14,15],
      [16,17,18]]


# for i in zip(M1,M2):
#     print(i)

# After Performing Above Operation below is the result we get   (here zip combines both list as one)

# ([1, 2, 3], [10, 11, 12])
# ([4, 5, 6], [13, 14, 15])
# ([7, 8, 9], [16, 17, 18])


# for i in zip(M1,M2):
#     print(list(zip(*i)))

# After Performing Above Operation below is the result we get   (here zip combines both list as one)

# [(1, 10), (2, 11), (3, 12)]
# [(4, 13), (5, 14), (6, 15)]
# [(7, 16), (8, 17), (9, 18)]

# for i in zip(M1,M2):
#     print([sum(j) for j in list(zip(*i))])

# After Performing Above Operation below is the result we get   (here zip combines both list as one)

# [11, 13, 15]
# [17, 19, 21]
# [23, 25, 27]

   # or  simply

Addition = [list(map(sum,zip(*i))) for i in zip(M1,M2)]
print("          Matrix M1 =      ",M1)
print("          Matrix M2 =      ",M2)
print("Addition of two matrices = ",Addition)

# or

print()
output = [[0]*len(M1[0])]*len(M1)
for i in range(len(M1)):
    for j in range(len(M2)):
       output[i][j] = M1[i][j]+M2[i][j]
print("          Matrix M1 =      ",M1)
print("          Matrix M2 =      ",M2)
print("Addition of two matrices = ",output)
