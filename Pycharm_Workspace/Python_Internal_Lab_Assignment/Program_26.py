
# Written by Aakash Nadupalli

# 26.Write a Python program that reads in strings from standard input and writes them
# in reverse order using a stack.

# st = 'I am Honest'
# print(' '.join(st.split()[::-1]))

class Stack:
    def __init__(self):
        self.list = []

    def isEmpty(self):
        if len(self.list)==0 :
            return True
        else:
            return False

    def push(self,st):
        for i in st:
            self.list.append(i)

    def pop(self):
        if not self.isEmpty():
            self.list.pop()
        else:
            return "Empty Stack.."

    def Reverse(self,string):
        if self.isEmpty():
            return "Empty Stack.."
        else:
            lst = self.list
            new_string = ""
            for i in string:
                new_string += lst.pop()
        return new_string


Enter_string = input("Enter String : ")
print("String   = ",Enter_string)

st = Stack()
st.push(Enter_string)
# print(st.list)
print("Reversed = ",st.Reverse(Enter_string))
