## Distance Vector Routing Algorithm

import pandas as pd

vertices = int(input("Enter Number of Vertices : "))
edges = int(input("Enter Number of Edges : "))
Adjacency_Matrix = [[-1]*vertices for i in range(vertices)]
print("Enter Vertex , Edge , Weight ")
for i in range(vertices):
    v,e,w = list(map(int,input().split()))
    Adjacency_Matrix[v][e] = w
    Adjacency_Matrix[e][v] = w

print("Adjacency_Matrix = ")
print("  ",end=" ")
for i in range(vertices):
    print(" ",i,end = " ")
print()
for i in range(len(Adjacency_Matrix)):
    print(i," ",Adjacency_Matrix[i])

frt = {i:{"Destination":[],"Distance":[],"Next":[]} for i in range(vertices)}

for i in range(len(Adjacency_Matrix)):
    for j in range(len(Adjacency_Matrix)):
        if i==j:
            frt[i]["Destination"]+=[j]
            frt[i]["Distance"] += ['-']
            frt[i]["Next"] += [j]

        elif Adjacency_Matrix[i][j]!=-1:
            frt[i]["Destination"] += [j]
            frt[i]["Distance"] += [Adjacency_Matrix[i][j]]
            frt[i]["Next"] += [j]

        else:
            frt[i]["Destination"] += [j]
            frt[i]["Distance"] += [float('inf')]
            frt[i]["Next"] += ['-']

print()
print("Routing Tables for Each Node as Follows : ")
for i in range(len(frt)):
    print()
    print(f"Routing Table {i}")
    # print(frt[i])
    print(pd.DataFrame(frt[i]))


# 0 1 2
# 1 2 4
# 1 4 3
# 2 3 6
# 3 4 5