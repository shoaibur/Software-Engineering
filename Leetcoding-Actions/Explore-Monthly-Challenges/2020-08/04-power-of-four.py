class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num < 1: return False
        x = math.log2(num) / 2
        return x % 1 == 0
