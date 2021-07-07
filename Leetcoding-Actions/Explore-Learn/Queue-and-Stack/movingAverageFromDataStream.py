class MovingAverage:
    '''
    T: O(1) and S: O(size)
    '''

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.q = deque()
        self.size = size
        self.sum = 0

    def next(self, val: int) -> float:
        self.q.append(val)
        if len(self.q) > self.size:
            self.sum -= self.q.popleft()
        self.sum += val
        return self.sum / len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
