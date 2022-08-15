
# Written by Aakash Nadupalli

# 20.Write Python program to implement the stack ADT using a list.

class Stack:
    def __init__(self):
        self.list = []

    def isEmpty(self):
        if len(self.list) == 0:
            return True
        else:
            return False

    def push(self,value):
        self.list.append(value)

    def pop(self):
        if self.isEmpty():
            return "Stack Empty .... \n"
        else:
            self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack Empty .... \n"
        else:
            return self.list[-1]

    def print_stack(self):
        if self.isEmpty():
            return "Stack Empty .... \n"
        else:
            print("Stack Elements -> ",self.list)


stck = Stack()
lst = [40, 25, 42, 4, 78, 96, 5, 88, 3, 2, 8]
print(stck.isEmpty())
[stck.push(i) for i in lst]
stck.print_stack()
print("Top = ",stck.peek())
stck.pop()
stck.print_stack()
print("Top = ",stck.peek())
