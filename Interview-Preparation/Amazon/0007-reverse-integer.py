class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            x = int(str(x)[::-1])
        elif x < 0:
            x = -int(str(-x)[::-1])
        else:
            x = 0
        if -2**31 > x or x > 2**31-1:
            return 0
        return x
