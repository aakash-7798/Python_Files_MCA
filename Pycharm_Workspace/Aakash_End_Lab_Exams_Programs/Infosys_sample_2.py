max_pos_val=4
k=3
ot = []
if k==1 and k>0:
    for i in range(max_pos_val):
        ot.extend([[i+1]])
else:
    for i in range(k):
        for j in range(max_pos_val):
            if sorted([i+1,j+1]) not in ot:
                ot.append([i+1,j+1])
print(ot)