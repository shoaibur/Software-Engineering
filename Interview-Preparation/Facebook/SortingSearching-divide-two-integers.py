class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        negative = False
        if dividend < 0 and divisor < 0:
            negative = False
        elif dividend < 0 or divisor < 0:
            negative = True
            
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0
        
        while dividend >= divisor:
            shift = 0
            while dividend >= (divisor << 1 << shift):
                shift += 1
            result += 1 << shift
            dividend -= divisor << shift
        
        if negative:
            return max(-result, -2147483648)
        else:
            return min(result, 2147483647)
