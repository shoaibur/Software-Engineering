class Stack(object):
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        return self.stack.pop()
     
    def is_empty(self):
        return self.stack == []
    
    def size(self):
        return len(self.stack)
# Example
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.stack) # [1, 2, 3]
s.pop()
print(s.stack) # [1, 2]
