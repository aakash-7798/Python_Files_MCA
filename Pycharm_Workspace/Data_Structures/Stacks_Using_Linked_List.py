## Stacks Using Linked List Implementation

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Stack_Linked_List:
    def __init__(self):
        self.head = None
        self.top = None
        self.size = 0

    def push_sul(self,value):
        new_node = Node(value)
        self.size += 1
        if self.head is None:
            self.head = new_node
            self.top = new_node

        else:
            self.top.next = new_node
            self.top = new_node

    def pop_sul(self):
        if self.head is None:
            print("Stack is Empty... To delete ..stack should have atleast one element....")
            return

        self.size-=1

        print(f"After Deleting Top Element -> {self.top.data}"," ",end=' ')

        last_but_one = self.head
        last = self.head.next
        while last.next:
            last = last.next
            last_but_one = last_but_one.next
        last_but_one.next = None
        self.top = last_but_one
        self.print_sul()

    def print_sul(self):
        if self.head is None:
            print("No Elements To Print...")
            return
        temp = self.head
        print("Stack ELements Are : ",end=' ')
        while temp:
            print(temp.data,end=' --> ')
            temp = temp.next
        print("None")
        print("Top Element : ", self.top.data," ","Size of Stack : ",self.size)


sll = Stack_Linked_List()
for i in range(1,11):
    sll.push_sul(i)
sll.print_sul()
sll.pop_sul()
sll.print_sul()
