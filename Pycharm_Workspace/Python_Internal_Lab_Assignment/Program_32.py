# 32. Write a Python program to perform the following:
# i)create non recursively a binary search tree of integers.
# ii)search non recursively for an integer key in the above binary search tree.
# iii)search recursively for an integer key in the above binary search tree.


class bst_node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root,value):
    current,parent = root,None
    if root is None:
        return bst_node(value)
    while current:
        parent = current
        if value < current.data:
            current = current.left
        else:
            current = current.right
    if value < parent.data:
        parent.left = bst_node(value)
    else:
        parent.right = bst_node(value)
    return root

def search_recur(root,key):
    if root is None:
        return f'Element {key} Not Found....'
    else:
        if root.data == key:
            return f'Element {key} is present in the Tree'
        elif key < root.data:
            return search_recur(root.left,key)
        else:
            return search_recur(root.right, key)

def search_non_recur(root,key):
        while root:
            if key < root.data:
                root = root.left
            elif key > root.data:
                root = root.right
            else:
                return f'Element {key} is present in the Tree'
        return f'Element {key} Not Found....'
values = [5,8,2,3,1,9,7,6,4]
#               5
#          /        \
#        2           8
#      /   \       /    \
#     1     3     7      9
#            \   /
#             4 6
root = None
for i in values:
    root = insert(root,i)
print(search_recur(root,3))
print(search_recur(root,30))
print(search_non_recur(root,8))
print(search_non_recur(root,6))
print(search_non_recur(root,15))