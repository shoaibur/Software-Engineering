# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.buffer = []
        
    def read(self, buf: List[str], n: int) -> int:
        buf4 = [' '] * 4
        while len(self.buffer) < n:
            k = read4(buf4)
            if k == 0: break
            self.buffer += buf4[:k]
        
        idx = 0
        while(self.buffer and idx<n):
            buf[idx] = self.buffer.pop(0)
            idx += 1
        return idx
