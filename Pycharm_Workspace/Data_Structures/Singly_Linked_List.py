# ## Linked List Implementation
# import self as self
#
#
import self


class Node:
    def __init__(self, ele):
        self.data = ele
        self.next = None


class Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_first(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = None
        else:
            new_node.next = self.head
            self.head = new_node
        print(f"After Adding First Element {self.head.data}")
        self.print_list()

    def insert_last(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = None
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = new_node
            self.tail = new_node
            self.tail.next = None
        print(f"After Adding Last Element {self.tail.data}")
        self.print_list()

    def insert_After(self,after_which,value):
        new_node = Node(value)
        if self.head is None:
            print("Element Not Present In the List.....") 
        print(f"Value {value} Inserted After {after_which}")
        if self.head.data == after_which:
            new_node.next = self.head.next
            self.head.next = new_node
        if self.tail.data == after_which:
            self.tail.next = new_node;
            self.tail = new_node
            new_node.next = None
        else:
            temp = self.head
            flag = False
            while temp:
                if temp.data == after_which:
                    new_node.next = temp.next
                    temp.next = new_node
                    flag= True
                temp = temp.next
        if flag==False:
                print("  !!...  .   Element Not Present In the List ...>> ---   Specify only the element which is in the List ")
        else:
            self.print_list()

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = None
            return
        if self.tail.next is None:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = None
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = new_node

    def delete_first(self):
        if self.head is None:
            print("No elements to delete -->   to perform this operation you need to have atleast one element in the list....")
            return
        print(f"After Deleting First Element {self.head.data}")
        self.head = self.head.next
        self.print_list()

    def delete_last(self):
        if self.head is None:
            print("No elements to delete -->   to perform this operation you need to have atleast one element in the list....")
            return
        print(f"After Deleting Last Element {self.tail.data}")
        temp = self.head
        temp1 = self.head.next
        while(temp1.next):
            temp1 = temp1.next
            temp = temp.next
        temp.next = None
        self.tail = temp
        self.print_list()

    def print_list(self):
        if self.head is None:
            print("No Elements To Print...")
            return
        print("Linked List Elements : ",end='')
        temp = self.head
        while(temp):
            print(temp.data,end=" --> ")
            temp = temp.next
        print("None")
        print("Head = ",self.head.data,"Tail = ",self.tail.data)


    ### Initializing
ll = Linked_List()
elements = [2,7,9,3,5,8,1,6,25,38,78,99,11,15,65,88]
for i in range(len(elements)):
    ll.insert(elements[i])
ll.print_list()
ll.insert_After(300,1)
# # ll.print_list()
# ll.insert_After(4,3)
# ll.print_list()
# ll.insert_After(10,11)
# ll.print_list()
# # print("Head = ",ll.head,"Tail = ",ll.tail)
# ll.insert_first(0)
# ll.insert_last(12)
ll.delete_first()
ll.delete_last()
