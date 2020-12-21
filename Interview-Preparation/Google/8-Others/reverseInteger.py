class Solution:
    def reverse(self, x: int) -> int:
        
        negative = x < 0
        x = abs(x)
        y = x
        
        nDigit = 0
        while x > 0:
            x //= 10
            nDigit += 1
        
        result = 0
        while y > 0:
            y, rem = divmod(y, 10)
            result += rem * 10 ** (nDigit - 1)
            nDigit -= 1
        
        if negative:
            result = -result
        overflow = (result < -2**31) or (result > 2**31 - 1)
        if overflow: return 0
        
        return result
