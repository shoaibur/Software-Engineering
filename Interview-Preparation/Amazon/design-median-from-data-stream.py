class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        # Put num into left or right halves
        if len(self.left) == 0 or num <= -self.left[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)
        # Balance the size of left and right halves
        if len(self.left) - len(self.right) > 1:
            p = heapq.heappop(self.left)
            heapq.heappush(self.right, -p)
        if len(self.left) < len(self.right):
            p = heapq.heappop(self.right)
            heapq.heappush(self.left, -p)
            
    def findMedian(self) -> float:
        #print(self.left, self.right)
        if len(self.left) != len(self.right):
            return -self.left[0]
        else:
            return (-self.left[0] + self.right[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
