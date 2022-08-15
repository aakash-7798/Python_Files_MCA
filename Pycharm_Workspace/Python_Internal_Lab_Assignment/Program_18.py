
# Written by Aakash Nadupalli

# 18.Write Python program to implement the stack ADT using a singly linked list.

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.top = None
        self.size = 0

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def push(self,value):
        new_node = Node(value)
        self.size += 1

        if self.isEmpty():
            self.head = new_node
            self.top = new_node

        else:
            self.top.next = new_node
            self.top = new_node


    def pop(self):
        if self.isEmpty():
            return "Empty List..."

        else:
            print(f"After Deleting {self.top.data} ")
            self.size -= 1
            temp = self.head
            temp1 = self.head.next
            while temp1.next is not None:
                temp = temp.next
                temp1 = temp1.next
            temp.next = None
            self.top = temp
        self.print_list()

    def print_list(self):
        if self.head is None:
            return "Empty Stack...."
        else:
            temp = self.head
            print("Stack Elements -> [",end='')
            while temp.next is not None:
                print(temp.data,end=',')
                temp = temp.next
            print(f"{temp.data}]")
            print("Top = ", self.top.data, " Size=", self.size,'\n')


stck = Stack()
lst = [8, 2, 1, 5, 18, 33, 5, 58, 35, 69, 38, 7, 56]
[stck.push(i) for i in lst]
stck.print_list()
stck.pop()