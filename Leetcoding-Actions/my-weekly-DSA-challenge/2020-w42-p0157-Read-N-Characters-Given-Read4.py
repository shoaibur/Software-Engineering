"""
The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def __init__(self):
        self.buffer = deque()
    
    def read(self, buf, n):
        '''
        T: O(n)
        S: O(1)
        '''
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        while len(self.buffer) < n:
            buf4 = [''] * 4
            k = read4(buf4)
            if k == 0: break
            for item in buf4[:k]:
                self.buffer.append(item)
                if len(self.buffer) == n:
                    break
        idx = 0
        while self.buffer:
            buf[idx] = self.buffer.popleft()
            idx += 1
        
        return idx
