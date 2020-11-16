class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.minstack:
            self.minstack.append(x)
        elif x < self.minstack[-1]:
            self.minstack.append(x)
        else:
            self.minstack.append(self.minstack[-1])

    def pop(self) -> None:
        self.minstack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = float('inf')

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append(x)
            self.min = x
        elif x >= self.min:
            self.stack.append(x)
        else:
            self.stack.append( 2*x - self.min )
            self.min = x

    def pop(self) -> None:
        en = self.stack.pop()
        if en < self.min:
            self.min = 2*self.min - en

    def top(self) -> int:
        en = self.stack[-1]
        if en < self.min:
            return (en + self.min) / 2
        return en
        
    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
