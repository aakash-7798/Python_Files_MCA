# ## Linked List Implementation   Function Created Are Full ADT
# import self as self

class Node:
    def __init__(self, ele):
        self.data = ele
        self.next = None


class Linked_List:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_first(self, value):
        new_node = Node(value)
        self.size += 1

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
        self.size += 1

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = None

        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            self.tail = new_node
            self.tail.next = None

        print(f"After Adding Last Element {self.tail.data}")
        self.print_list()

    def insert_After(self, after_which, value):
        new_node = Node(value)
        flag = False

        if self.head is None:
            print("Element Not Present In the List.....")

        if self.head.data == after_which:
            new_node.next = self.head.next
            self.head.next = new_node
            flag = True

        if self.tail.data == after_which:
            self.tail.next = new_node;
            self.tail = new_node
            new_node.next = None
            flag = True

        else:
            temp = self.head
            while temp:
                if temp.data == after_which:
                    new_node.next = temp.next
                    temp.next = new_node
                    flag = True
                temp = temp.next

        if not flag:
            print(
                "!!...  .   Element Not Present In the List ...>> ---   Specify only the element which is in the List ",
                "\n")
        else:
            self.size += 1
            print(f"Value {value} Inserted After {after_which}")
            self.print_list()

            #   Below insert is just optional no need to create i just created for testing purpose

    def insert(self, value):
        new_node = Node(value)
        self.size += 1

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
            while (temp.next):
                temp = temp.next
            temp.next = new_node

    def delete_first(self):
        if self.head is None:
            print(
                "No elements to delete -->   to perform this operation you need to have atleast one element in the "
                "list....")
            return

        print("Before Deletion : ", end='')
        self.print_list()

        self.size -= 1

        print(f"After Deleting First Element {self.head.data}")
        self.head = self.head.next

        print(end='')
        self.print_list()

    def delete_last(self):
        if self.head is None:
            print(
                "No elements to delete -->   to perform this operation you need to have atleast one element in the "
                "list....")
            return

        print("Before Deletion : ", end='')
        self.print_list()

        self.size -= 1

        print(f"After Deleting Last Element {self.tail.data}")
        temp = self.head
        temp1 = self.head.next
        while temp1.next:
            temp1 = temp1.next
            temp = temp.next
        temp.next = None
        self.tail = temp

        print(end='')
        self.print_list()

    def delete(self,value):
        flag = False

        if self.head is None:
            print("Emtpy List ..  there should be atleast one element to delete...")
            return

        if self.head.data == value:
            self.delete_first()
            flag = True

        elif self.tail.data == value:
            self.delete_last()
            flag = True

        else:
            temp = self.head
            while temp.next is not None:
                if temp.next.data == value:
                    flag = True
                    temp.next = temp.next.next
                    break
                # print(temp.data,end=' ')
                temp = temp.next
            if temp.next is None:
                flag = False

        if not flag:
            print(f"The Element {value} you are trying to delete is not present in the list ... so specify only which "
                  f"are present.. \n")
        else:
            self.size -= 1

            print(f"After Deleting {value} : ",end='')
            self.print_list()

    def print_list(self):
        if self.head is None:
            print("No Elements To Print...")
            return

        print("Linked List Elements : ", end='')
        temp = self.head
        while temp:
            print(temp.data, end=" --> ")
            temp = temp.next
        print("None")

        print("Head = ", self.head.data, "  ", "Tail = ", self.tail.data, "  ", "Size = ", self.size, '\n')

    ### Initializing


ll = Linked_List()
roll_no = [f"21031F00{i:02d}" for i in range(2,30)]
# elements = [2, 7, 9, 3, 5, 8, 1, 6, 25, 38, 78, 99, 11, 15, 65, 88]
for i in roll_no:
    ll.insert(i)
ll.print_list()
ll.insert_first("21031F0001")
ll.insert_last("21031F0030")
ll.delete("21031F0026")
ll.insert_After("21031F0025","21031F0026")
ll.delete_first()
ll.delete_last()