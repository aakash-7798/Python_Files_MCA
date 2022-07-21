## Stack Implementation  (Dynamic)
class stack:
    def __init__(self):
        self.stack_list = []

    def isEmpty(self):
        if len(self.stack_list) == 0:
            return True
        else:
            return False

    def push_s(self,value):
            self.stack_list.append(value)

    def pop_s(self):
        if not self.isEmpty():
            x = self.stack_list.pop()
            print(f"After Deleting {x} Successfully",end =' ')
        else:
            print("Emtpy Stack..  there should be atleast one element to delete...")
            return
        self.print_s()

    def peek_s(self):
        if not self.isEmpty():
            print("Peek Element :",end=' ')
            print(self.stack_list[-1])
        else:
            print("Emtpy Stack..  there should be atleast one element to get top element...")
            return

    def get_size(self):
        if not self.isEmpty():
            print("Size = ",len(self.stack_list))
        else:
            print("Stack Empty...")
            return

    def print_s(self):
        if not self.isEmpty():
            print("Stack Elements -->", end=' ')
            print(self.stack_list)
        else:
            print("No Elements To Print...")
            return
st = stack()
for i in range(1,11):
    st.push_s(i)
st.print_s()
st.pop_s()
st.pop_s()
st.pop_s()
st.push_s(15)
st.peek_s()
st.print_s()
st.get_size()