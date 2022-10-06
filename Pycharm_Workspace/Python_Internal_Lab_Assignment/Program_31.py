# 31.Write a Python program to perform the following:
# i)create non recursively a binary search tree of integers.
# ii)traverse the above binary search tree recursively in inorder.
# iii)traverse the above binary search tree recursively in preorder.
# iv)traverse the above binary search tree recursively in postorder.


class bst_node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Following is recursive method
# def insert(root,value):
#     if root is None:
#         root = bst_node(value)
#         return root
#
#     if root.data > value:
#         root.left = insert(root.left,value)
#
#     else:
#         root.right = insert(root.right,value)
#     return root

# NonRecursive Method

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


def Inorder(root):
    if root is None:
        return
    else:
        Inorder(root.left)
        print(root.data,end=" ")
        Inorder(root.right)

def Pre_order(root):
    if root is None:
        return
    else:
        print(root.data,end=" ")
        Pre_order(root.left)
        Pre_order(root.right)

def Post_order(root):
    if root is None:
        return
    else:
        Post_order(root.left)
        Post_order(root.right)
        print(root.data,end=" ")


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
print("Inorder Traversal   -> ",end=' ')
Inorder(root)
print()
print("Preorder Traversal  -> ",end=" ")
Pre_order(root)
print()
print("Postorder Traversal -> ",end=" ")
Post_order(root)
print()