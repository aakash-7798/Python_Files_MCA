
# Written by Aakash Nadupalli

# 19.Write Python program to implement the queue ADT using a singly linked list.

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0


    def enqueue(self,value):
        new_node = Node(value)
        self.size += 1

        if self.front is None:
            self.front = new_node
            self.rear = new_node

        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return "Empty Queue...\n"
        else:
            print(f"After Deleting first element {self.front.data}")
            self.front = self.front.next
            self.size -= 1
            self.print_list()


    def print_list(self):
        if self.front is None:
            return "Empty Queue...."
        else:
            temp = self.front
            print("Queue Elements -> [",end='')
            while temp.next is not None:
                print(temp.data,end=',')
                temp = temp.next
            print(f"{temp.data}]")
            print("Front = ", self.front.data, " Rear = ", self.rear.data, " Size=", self.size, '\n')


q = Queue()
lst = [8, 2, 1, 5, 18, 33, 5, 58, 35, 69, 38, 7, 56]
[q.enqueue(i) for i in lst]
q.print_list()
q.dequeue()