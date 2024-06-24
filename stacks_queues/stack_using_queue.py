from queue import Queue

class StackUsingQueue:
    def __init__(self, stack_size) -> None:
        self.stack = Queue(stack_size)
        
    def push(self, num):
        self.stack.push(num)
        for i in range(self.stack.no_elements - 1):
            if self.stack.no_elements <= self.stack.queue_size:
                self.stack.push(self.stack.pop())
            
    def pop(self):
        return self.stack.pop()
    
    def top(self):
        return self.stack.top()
    
    def __repr__(self) -> str:
        return str(self.stack)
    
s = StackUsingQueue(5)
s.push(10)
print(s)
s.push(20)
print(s)
s.push(30)
print(s)
s.push(303)
print(s)
s.push(55)
print(s)
s.push(90)
print(s)
print(s.top())
print(s.pop())
print(s.top())
print(s)