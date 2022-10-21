
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Single_Linked_List:
    def __init__(self):
        self.size = 0
        self.head = None

    def insert_first(self,value):
        new_node = Node(value)
        self.size+=1
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_last(self, value):
        new_node = Node(value)
        self.size+=1
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def delete(self,value):
        if self.head is None:
            return "Empty List so we cannot perform delete operation"
        elif self.head.data == value:
            self.head = self.head.next
            self.size-=1
        else:
            flag = False
            temp = self.head
            while temp.next is not None:
                if temp.next.data == value:
                    flag = True
                    if temp.next.next is None:
                        temp.next = None
                        break
                    else:
                        temp.next = temp.next.next
                        break
                temp = temp.next
            if flag is True:
                self.size-=1
            else:
                return "Element is ot present in the list"

    def print_list(self):
        if self.head is None:
            return "Empty List So no elements to print"
        else:
            print("Single Linked List Elements : ",end='')
            temp = self.head
            while temp is not None:
                print(temp.data,end=' -> ')
                temp = temp.next
            print("Null")

sl = Single_Linked_List()
n = [4,7,8,16,19,24,27]
for i in n:
    sl.insert_last(i)
sl.print_list()
sl.delete(4)
sl.print_list()
sl.delete(27)
sl.print_list()
sl.delete(16)
sl.print_list()