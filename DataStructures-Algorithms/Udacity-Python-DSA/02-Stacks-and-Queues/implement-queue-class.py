class Queue(object):
    def __init__(self):
        self.q = []
    
    def push(self, value):
        self.q.insert(0, value)
    
    def pop(self):
        return self.q.pop()
    
    def is_empty(self):
        return self.q == []
    
    def size(self):
        return len(self.q)
# Example
q = Queue()
q.push(1)
q.push(2)
q.push(3)
print(q.q) # [3, 2, 1]
q.pop()
print(q.q) # [3, 2]
