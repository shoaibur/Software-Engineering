# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    '''
    T: O(n) and S: O(n)
    '''
    def __init__(self):
        self.buffer = deque()
        
    def read(self, buf: List[str], n: int) -> int:
        buf4 = [' '] * 4
        while True:
            k = read4(buf4)
            if k == 0: break
            for i in range(k):
                self.buffer.append(buf4[i])
            
        i = 0
        while i < n and self.buffer:
            buf[i] = self.buffer.popleft()
            i += 1
        return i
