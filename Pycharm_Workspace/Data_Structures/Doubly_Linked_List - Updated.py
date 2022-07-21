### Doubly Linked List Implementation

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None


class Db_Linked_List:
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

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_Last(self, value):
        new_node = Node(value)

        self.size += 1

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_After(self, after_which, value):

        new_node = Node(value)
        flag = False

        if self.head is None:
            print("Element Not Present In the List..... so cannot add value")

        elif self.head.data == after_which:
            new_node.prev = self.head
            new_node.next = self.head.next
            self.head.next = new_node
            new_node.next.prev = new_node
            flag = True

        elif self.tail.data == after_which:
            self.insert_Last(value)
            flag = True

        else:
            temp = self.head
            while temp:
                if temp.data == after_which:
                    flag = True
                    new_node.next = temp.next
                    new_node.prev = temp
                    temp.next = new_node
                    new_node.next.prev = new_node
                    break
                temp = temp.next

        if not flag:
            print(
                f"!!...  .   Element {after_which} Not Present In the List ...>> ---   Specify only the element which is in the List ",
                "\n")
        else:
            self.size += 1
            print(f"Value {value} Inserted After {after_which}")
            self.print_list()

    def insert_Before(self, before_which, value):
        new_node = Node(value)
        flag = False

        if self.head is None:
            print("Element Not Present In the List..... so cannot add value")

        elif self.head.data == before_which:
            self.insert_first(value)
            flag = True

        elif self.tail.data == before_which:
            new_node.next = self.tail
            new_node.prev = self.tail.prev
            self.tail.prev = new_node
            new_node.prev.next = new_node
            flag = True

        else:
            temp = self.head
            while temp:
                if temp.data == before_which and temp.next is not None:
                    flag = True
                    new_node.next = temp
                    new_node.prev = temp.prev
                    temp.prev = new_node
                    new_node.prev.next = new_node
                    break
                temp = temp.next

        if not flag:
            print(
                f"!!...  .   Element {before_which} Not Present In the List ...>> ---   Specify only the element which is in the List ",
                "\n")
        else:
            self.size += 1
            print(f"Value {value} Inserted Before {before_which}")
            self.print_list()

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
        self.tail.prev = temp.prev
        self.tail.prev.next = temp

        print(end='')
        self.print_list()

    def delete(self,value):

        if self.head is None:
            print("Emtpy List ..  there should be atleast one element to delete...")
            return

        if self.head.data == value:
            self.delete_first()

        elif self.tail.data == value:
            self.delete_last()

        else:
            flag = False
            temp = self.head
            while temp.next is not None:
                if temp.next.data == value:
                    flag = True
                    temp.next.next.prev = temp
                    temp.next = temp.next.next
                    break
                temp = temp.next
            if temp.next is None:
                flag = False

            if not flag:
                print(f"The Element {value} you are trying to delete is not present in the list ... so specify only which "
                  f"are present.. \n")
            else:
                self.size -= 1
                print(f"After Deleting {value} : ", end='')
                self.print_list()

    def print_list(self):
        if self.head is None:
            print('No Elements To Print...')
            return
        print("Doubly Linked List Elements : ", end='')
        temp = self.head
        print("None", end=" <--> ")
        while temp:
            print(temp.data, end=" <--> ")
            temp = temp.next
        print("None")

        print("Head = ", self.head.data, "  ", "Tail = ", self.tail.data, "  ", "Size = ", self.size, '\n')

    def print_reverse_list(self):
        if self.head is None:
            print("No Elements To Print...")
            return

        print("Reverse Doubly Linked List Elements : ", end='')
        temp = self.tail
        print("None", end=" <--> ")
        while temp is not None:
            print(temp.data, end=" <--> ")
            temp = temp.prev
        print("None")

        print("Head = ", self.tail.data, "  ", "Tail = ", self.head.data, "  ", "Size = ", self.size, '\n')


Dl = Db_Linked_List()
# roll_no = [f"21031F00{i:02d}" for i in range(1,31)]
elements = [2, 7, 9, 3, 5, 8, 1, 6, 25, 38, 78, 99, 11, 15, 65, 88]
for i in elements:
    Dl.insert_Last(i)
Dl.print_list()
Dl.insert_After(8,50)

Dl.delete(3)
Dl.delete(78)
Dl.insert_first(10)
Dl.insert_After(2,300)
Dl.insert_After(2, 300)
Dl.print_reverse_list()
Dl.insert_Before(2, 1)
Dl.insert_Before(88, 50)
Dl.insert_Before(99, 84)
Dl.print_reverse_list()
# Dl.delete_last()
