class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.k = k
        self.data = [None] * self.k
        self.head = 0
        self.tail = 0
        self.count = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.count < self.k:
            self.data[self.tail] = value
            self.tail += 1
            if self.tail >= self.k:
                self.tail = 0
            self.count += 1
            return True
        return False

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if not self.isEmpty():
            self.data[self.head] = None
            self.head += 1
            if self.head >= self.k:
                self.head = 0
            self.count -= 1
            return True
        return False

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return self.data[self.head] if not self.isEmpty() else -1

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return self.data[self.tail-1] if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.count == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.count == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
