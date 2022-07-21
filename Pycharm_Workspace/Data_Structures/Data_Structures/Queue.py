## Queues Implementation

class queue:
    def __init__(self):
        self.queue_list = []

    def is_q_Empty(self):
        if len(self.queue_list)==0:
            return True
        else:
            return False

    def enqueue(self,value):
        self.queue_list.append(value)

    def dequeue(self):
        if not self.is_q_Empty():
            x = self.queue_list.pop(0)
            print(f"After Deleting {x} Successfully", end=' ')
        else:
            print("Emtpy Queue..  there should be atleast one element to delete...")
            return
        self.print_q()

    def dequeue_last(self):
        if not self.is_q_Empty():
            x = self.queue_list.pop()
            print(f"After Deleting {x} Successfully", end=' ')
        else:
            print("Emtpy Queue..  there should be atleast one element to delete...")
            return
        self.print_q()

    def front_q(self):
        if not self.is_q_Empty():
            return self.queue_list[0]
        else:
            print("Emtpy Queue.. ")
            return

    def rear_q(self):
        if not self.is_q_Empty():
            if len(self.queue_list) ==0:
                return self.queue_list[0]
            else:
                return self.queue_list[-1]
        else:
            print("Queue Empty..")
            return

    def print_q(self):
        if not self.is_q_Empty():
            print("Queue Elements :",self.queue_list)
            print("Front Element = ",self.front_q()," "," Rear Element : ",self.rear_q(),"\n")
        else:
            print("Queue is Empty so no elements To Print...")
            return

qu = queue()
for i in range(20,21):
    qu.enqueue(i)
qu.print_q()
qu.dequeue()
qu.dequeue_last()
