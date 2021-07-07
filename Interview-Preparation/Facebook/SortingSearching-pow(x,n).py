class Solution:
    def myPow(self, x: float, n: int) -> float:        
        if n == 0: return 1
        result = self.myPow(x*x, abs(n)//2)
        if n % 2:
            result *= x
        if n < 0:
            return 1/result
        return result
