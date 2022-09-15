class Queue:
    def __init__(self):
        self.queue = []


    #add an element
    def enqueue(self, item):
        self.queue.append(item)

    #remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    #display in queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)

q.display()

q.dequeue()
q.dequeue()


print("After removing an element")
q.display()

    