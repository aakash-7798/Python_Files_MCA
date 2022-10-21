class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def insert(self,root,value):
        if root is None:
            return Node(value)
        if value < root.data:
            root.left = self.insert(root.left,value)
        elif value > root.data:
            root.right = self.insert(root.right, value)
        return root

    def postorder(self,root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data,end=" ")

bst = BST()
lt = [4,2,6,1,3,5,7]
root = None
print("Binary Search Tree ")
for i in lt:
    root = bst.insert(root,i)
print("PostOrder --> ",end='')
bst.postorder(root)

lst = [4,6,8,12,15,17,19]
def linear_search(lt,key):
    for i in range(len(lt)):
        if lt[i] == key:
            return i
    return -1

print("\n\nLinear Search Method")
ls = linear_search(lst,15)
if ls>=0:
    print('Element Found at Position -> ',ls)
else:
    print('Element Not Found ...')
