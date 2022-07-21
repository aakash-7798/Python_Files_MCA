# Queues Using Linked List Implementation

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Queues_Linked_List:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def Enqueue_ll(self,value):
        new_node = Node(value)
        self.size += 1
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def Dequeue(self):
        if self.front is None:
            print("Queue is Empty... To delete ..stack should have atleast one element....")
            return

        self.size -= 1
        print(f"After Deleting Front Element -> {self.front.data}", " ", end=' ')

        self.front = self.front.next
        self.print_qul()

    def print_qul(self):
        if self.front is None:
            print("No Elements To Print...")
            return
        temp = self.front
        print("Queue elements Are : ",end=' ')
        while temp:
            print(temp.data,end=' --> ')
            temp = temp.next
        print("None")
        print("Front Element : ", self.front.data," ","Rear Element : ", self.rear.data," ","Size of Stack : ",self.size)


qul = Queues_Linked_List()
for i in range(1,11):
    qul.Enqueue_ll(i)
qul.print_qul()
qul.Dequeue()
