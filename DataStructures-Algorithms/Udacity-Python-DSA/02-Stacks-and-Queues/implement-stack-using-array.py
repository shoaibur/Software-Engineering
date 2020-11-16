def stack_from_array(nums):
    stack = Stack()
    for num in nums:
        stack.push(num)
    return stack
    
class Stack(object):
    def __init__(self):
        self.stack = []
        
    def push(self, value):
        self.stack.append(value)
