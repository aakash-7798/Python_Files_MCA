
# Written by Aakash Nadupalli

# 16.Write Python program to implement the deque (double ended queue) ADT using
# a singly linked list.

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue_first(self,value):
        new_node = Node(value)
        self.size += 1

        if self.front is None:
            self.front = new_node
            self.rear = new_node

        else:
            new_node.next = self.front
            self.front = new_node


    def enqueue_last(self,value):
        new_node = Node(value)
        self.size += 1

        if self.front is None:
            self.front = new_node
            self.rear = new_node

        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue_first(self):
        if self.front is None:
            return "Empty Deque...\n"
        else:
            print(f"After Deleting first element {self.front.data}")
            self.front = self.front.next
            self.size -= 1
            self.print_list()


    def dequeue_last(self):
        if self.front is None:
            return "Empty Deque...\n"
        else:
            print(f"After Deleting last element {self.rear.data}")
            last_but_one = self.front
            last = self.front.next
            while last.next is not None:
                last = last.next
                last_but_one = last_but_one.next
            last_but_one.next = None
            self.rear = last_but_one
            self.size -= 1
            self.print_list()

    def print_list(self):
        if self.front is None:
            return "Empty Deque...."
        else:
            temp = self.front
            print("Deque Elements -> [",end='')
            while temp.next is not None:
                print(temp.data,end=',')
                temp = temp.next
            print(f"{temp.data}]")
            print("Front = ", self.front.data, " Rear = ", self.rear.data, " Size=", self.size, '\n')


dq = deque()
lst = [8, 2, 1, 5, 18, 33, 5, 58, 35, 69, 38, 7, 56]
[dq.enqueue_last(i) for i in lst]
dq.print_list()
dq.enqueue_first(5)
dq.enqueue_first(4)
dq.enqueue_first(2)
dq.print_list()
dq.dequeue_first()
dq.dequeue_last()