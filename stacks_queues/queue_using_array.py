

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
            return f"Element {element} is pushed in queue"
        else:
            # queue is full
            return f"Can't add, queue is full"  
        
    def pop(self):
        if self.front != self.rear:
            location = self.front % self.queue_size
            ele = self.queue[location]
            self.queue[location] = None
            self.front += 1
            self.no_elements -= 1
            return f"Popped: {ele}"
        else:
            #queue is empty
            return f"Can't pop, queue is empty"
    
    def top(self):
        return f"Current top element is {self.queue[self.front % self.queue_size]}" if self.no_elements > 0 else f"Queue is empty"
    
    def __repr__(self) -> str:
        return f"Current queue is: {[a for a in self.queue]}"
q = Queue(5)

print(q.push(10))
print(q)
print(q.push(1))
print(q)
print(q.push(9))
print(q)
print(q.push(20))
print(q)
print(q.push(234))
print(q)
print(q.push(22435))
print(q)
print(q.top())
print(q.pop()) 
print(q)
print(q.top())
print(q.pop()) 
print(q)
print(q.top())
print(q.pop()) 
print(q)
print(q.top())
print(q.pop()) 
print(q)
print(q.top())
print(q.pop()) 
print(q)
print(q.top())
print(q.pop()) 
print(q)
print(q.top())
print(q.pop()) 
print(q)
print(q.top())
print(q.pop()) 
print(q)
print(q.top())
print(q.pop()) 
print(q)
print(q.top())
print(q.pop()) 
print(q)
print(q.push(10))
print(q)
print(q.push(1))
print(q)
print(q.push(9))
print(q)
print(q.push(20))
print(q)
print(q.push(234))
print(q)
print(q.push(22435))
print(q.push(22435))
print(q.push(22435))
print(q.push(22435))
print(q.push(22435))
print(q.push(22435))
print(q.push(22435))
print(q.push(22435))