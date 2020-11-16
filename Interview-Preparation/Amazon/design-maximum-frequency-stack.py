class FreqStack:
    def __init__(self):
        self.heap = []
        self.count = collections.Counter()
        self.push_count = 0

    def push(self, x: int) -> None:
        self.count[x] += 1
        self.push_count += 1
        heapq.heappush(self.heap, (-self.count[x], -self.push_count, x))

    def pop(self) -> int:
        _, _, x = heapq.heappop(self.heap)
        self.count[x] -= 1
        return x
