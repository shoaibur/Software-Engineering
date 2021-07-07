class Solution:
    def reverseBits(self, n: int) -> int:
        out = 0
        for i in range(32):
            out <<= 1
            if n & 1:
                out += 1
            n >>= 1
        return out
                
