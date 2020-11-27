class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.data = deque()
        self.size = size

    def next(self, val: int) -> float:
        self.data.append(val)
        if len(self.data) > self.size:
            self.data.popleft()
        return sum(self.data) / len(self.data)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
