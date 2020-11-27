class RecentCounter:

    def __init__(self):
        self.calls = deque()

    def ping(self, t: int) -> int:
        self.calls.append(t)
        
        while self.calls[0] < t - 3000:
            self.calls.popleft()
        
        return len(self.calls)
        
# Time: O(time_frame), assuming at most one call at a given time and time is an integer value. So, for 3000 ms time frame, there will be at most 3000 calls in the past 3000 ms.
# Space: O(time_frame)
