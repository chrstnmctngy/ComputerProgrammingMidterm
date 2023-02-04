print("Submitted by: Christian R. Macatangay (1R12)")

print()

class Queue:

    def __init__ (self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        else:
            return self.queue.pop(0)
    
    def size(self):
        return len(self.queue)

    def empty(self):
        return len(self.queue) == 0

    def front(self):
        return self.queue[0]
    
    def display(self):
        return self.queue

lstQueue = Queue()
lstQueue.enqueue("Alpha")
lstQueue.enqueue("Beta")
lstQueue.enqueue("Gamma")
lstQueue.enqueue("Delta")
lstQueue.enqueue("Epsilon")
print("Enqueue Method: " + str(lstQueue.display()))

print()

lstQueue.dequeue()
lstQueue.dequeue()
print("Dequeue Method: " + str(lstQueue.display()))

print()

print("Size Method: " + str(lstQueue.size()))

print()

print("Empty Method: " + str(lstQueue.empty()))

print()

print("Front Method: " + str(lstQueue.front()))



