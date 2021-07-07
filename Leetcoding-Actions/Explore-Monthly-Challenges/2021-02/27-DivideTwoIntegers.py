class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negative = (dividend < 0) ^ (divisor < 0)
        
        dividend, divisor = abs(dividend), abs(divisor)
        
        result = 0
        while dividend >= divisor:
            shift = 0
            while dividend >= (divisor << 1 << shift):
                shift += 1
            result += 1 << shift
            dividend -= divisor << shift
            
        
        if negative: return max(-result, -2**31)
        return min(result, 2**31-1)
