class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n == 1: return x
        neg = n < 0
        n = abs(n)
        result = self.myPow(x*x, n // 2)
        if n % 2:
            result *= x
        if neg:
            return 1 / result
        return result
