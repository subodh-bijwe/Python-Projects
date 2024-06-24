class Stack:
    def __init__(self, stack_size) -> None:
        self.stack = [None] * stack_size
        self.top = -1
        self.stack_size = stack_size
        self.no_elements = 0
        
    def push(self, num):
        if self.stack_size == self.top + 1:
            #stack is full
            return -1
        else:
            self.top += 1
            self.stack[self.top] = num
            
    
    def pop(self):
        if self.top != -1:
            ele = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            return ele 
        else:
            # stack is empty
            return -1
    
    def top_element(self):
        return self.stack[self.top] if self.top != -1 else -1
    
    def __repr__(self) -> str:
        return f"Current stack is {self.stack}"
    
    
# s = Stack(4)

# s.push(1)
# s.push(2)
# s.push(3)
# s.push(4)
# s.push(5)
# print(s)
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())


# print(s)