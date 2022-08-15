
# Written by Aakash Nadupalli

# 30.Write Python program to implement the deque (double ended queue) ADT using
# a list.

class Deque:
    def __init__(self):
        self.list = []

    def isEmpty(self):
        if len(self.list) == 0:
            return True
        else:
            return False

    def enqueue_first(self,value):
        self.list.insert(0,value)

    def enqueue_last(self,value):
        self.list.append(value)

    def dequeue_first(self):
        if self.isEmpty():
            return "Deque Empty .... \n"
        else:
            self.list.pop(0)


    def dequeue_last(self):
        if self.isEmpty():
            return "Deque Empty .... \n"
        else:
            self.list.pop()

    def front(self):
        if self.isEmpty():
            return "Deque Empty .... \n"
        else:
            return self.list[0]

    def rear(self):
        if self.isEmpty():
            return "Deque Empty .... \n"
        else:
            return self.list[-1]

    def print_queue(self):
        if self.isEmpty():
            return "Deque Empty .... \n"
        else:
            print("Deque Elements -> ",self.list)



dq = Deque()
lst = [40, 25, 42, 4, 78, 96, 5, 88, 3, 2, 8]
print(dq.isEmpty())
[dq.enqueue_first(i) for i in lst[:5]]
dq.print_queue()
[dq.enqueue_last(i) for i in lst[5:]]
dq.print_queue()
print("Front = ",dq.front()," Rear = ",dq.rear())
dq.dequeue_first()
dq.print_queue()
print("Front = ",dq.front()," Rear = ",dq.rear())
dq.dequeue_last()
dq.print_queue()
print("Front = ",dq.front()," Rear = ",dq.rear())