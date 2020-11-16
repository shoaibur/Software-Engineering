class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = []
        self.right = []
        

    def addNum(self, num: int) -> None:
        if len(self.left) == 0 or num < -self.left[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)
        
        if len(self.left) - len(self.right) > 1:
            pop = heapq.heappop(self.left)
            heapq.heappush(self.right, -pop)
        if len(self.right) > len(self.left):
            pop = heapq.heappop(self.right)
            heapq.heappush(self.left, -pop)
        
        
    def findMedian(self) -> float:
        if (len(self.left) + len(self.right)) % 2:
            return -self.left[0]
        return 0.5 * (-self.left[0] + self.right[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
