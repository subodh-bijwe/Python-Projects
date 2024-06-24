

class Queue:
    def __init__(self, queue_size):
        self.queue = [None] * queue_size
        self.front = 0
        self.rear = 0
        self.no_elements = 0
        self.queue_size = queue_size
        
    def push(self, element):
        if self.no_elements < self.queue_size:
            self.queue[self.rear % self.queue_size] = element
            self.rear += 1
            self.no_elements += 1
            
        else:
            # queue is full
            return -1 
        
    def pop(self):
        if self.front != self.rear:
            location = self.front % self.queue_size
            ele = self.queue[location]
            self.queue[location] = None
            self.front += 1
            self.no_elements -= 1
            return ele
        else:
            #queue is empty
            return -1
    
    def top(self):
        return self.queue[self.front % self.queue_size]
    
    def __repr__(self) -> str:
        return f"Current queue is: {[a for a in self.queue]}"
q = Queue(5)
