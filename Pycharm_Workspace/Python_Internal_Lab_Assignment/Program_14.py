
# Written by Aakash Nadupalli

# 14.Write Python program to perform the following:
# i)create a singly linked list of integers.
# ii)delete an integer from the above list.
# iii)traverse and display the contents of the above list after deletion.

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_last(self,value):
        new_node = Node(value)
        self.size += 1

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

    def delete(self,value):
        if self.head is None:
            return "Empty List..."

        elif self.head.data == value:
            self.head = self.head.next
            self.size -= 1

        else:
            temp = self.head
            while temp.next is not None:
                if temp.next.data == value:
                    if temp.next.data == self.tail.data:
                        print(f"\nAfter Deleting {value}")
                        temp.next = None
                        self.tail = temp
                        self.size -= 1
                        self.print_list()
                        break
                    else:
                        print(f"\nAfter Deleting {value}")
                        temp.next = temp.next.next
                        self.size -= 1
                        self.print_list()
                        break
                temp = temp.next
        return "Element Not Present in the List.."

    def print_list(self):
        if self.head is None:
            return "Empty List...."
        else:
            temp = self.head
            print("Linked List Elements -> [",end='')
            while temp.next is not None:
                print(temp.data,end=',')
                temp = temp.next
            print(f"{temp.data}]")
            print("Head = ",self.head.data," Tail = ",self.tail.data," Size=",self.size)


ll = Linked_List()
lst = [8, 2, 1, 5, 18, 33, 5, 58, 35, 69, 38, 7, 56]
[ll.insert_last(i) for i in lst]
ll.print_list()
ll.delete(8)
ll.delete(56)
ll.delete(58)

