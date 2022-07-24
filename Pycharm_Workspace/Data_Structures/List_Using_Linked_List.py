### List Implementation ADT

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class List_Using_Linked:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append_el(self,value):
        new_node = Node(value)
        self.size += 1
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove_el(self,value):
        rem_node = Node(value)
        if self.head is None:
            print("Empty List.. Add atleast one element to list  ...  to perform delete operation.")
            return
        bl = False
        if self.head.data == value:
            self.head = self.head.next
            bl = True
        else:
            temp = self.head
            while temp.next is not None:
                # print(temp.next.data,end=' , ')
                if temp.next.data == value:
                    bl = True
                    temp.next = temp.next.next
                    break
                temp = temp.next
        if bl is False:
            print("Value you are searching for is not present in the List.....")
            return
        else:
            self.size -= 1
            print(f"After Deleting {value} ")
            self.print_list()


    def clear_el(self):
        if self.head is None:
            print("List is already empty....   --> []")
        else:
            self.head = None
            self.tail = None
        # print("After clearing... List is ->  []")
        self.print_list()


    def print_list(self):
        if self.head is None:
            print("Empty List ......  -->   []")
        else:
            temp = self.head
            print("List Elements ->","[",end='')
            while temp.next is not None:
                print(temp.data,end=",")
                temp = temp.next
            print(f"{self.tail.data}]")



lst = List_Using_Linked()
for i in range(1,11):
    lst.append_el(i)
lst.print_list()
lst.remove_el(1)
# lst.clear_el()