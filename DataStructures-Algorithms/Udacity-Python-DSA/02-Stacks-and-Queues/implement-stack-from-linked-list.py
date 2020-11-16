def stack_from_linked_list(head):
    stack = Stack()
    tail = head
    while tail:
        stack.push(tail.value)
    tail = tail.next
    return stack

class Stack(object):
    def __init__(self):
        self.stack = []
        
    def push(self, value):
        self.stack.append(value)
