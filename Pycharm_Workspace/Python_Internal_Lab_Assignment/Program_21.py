
# Written by Aakash Nadupalli

# 21.Write Python program to implement the queue ADT using a list.

class Queue:
    def __init__(self):
        self.list = []

    def isEmpty(self):
        if len(self.list) == 0:
            return True
        else:
            return False

    def enqueue(self,value):
        self.list.append(value)

    def dequeue(self):
        if self.isEmpty():
            return "Queue Empty .... \n"
        else:
            self.list.pop(0)

    def front(self):
        if self.isEmpty():
            return "Queue Empty .... \n"
        else:
            return self.list[0]

    def rear(self):
        if self.isEmpty():
            return "Queue Empty .... \n"
        else:
            return self.list[-1]

    def print_queue(self):
        if self.isEmpty():
            return "Queue Empty .... \n"
        else:
            print("Queue Elements -> ",self.list)


qu = Queue()
lst = [40, 25, 42, 4, 78, 96, 5, 88, 3, 2, 8]
print(qu.isEmpty())
[qu.enqueue(i) for i in lst]
qu.print_queue()
print("Front =",qu.front())
print("Rear =",qu.rear())

qu.dequeue()

qu.print_queue()
print("Front =",qu.front())
print("Rear =",qu.rear())
