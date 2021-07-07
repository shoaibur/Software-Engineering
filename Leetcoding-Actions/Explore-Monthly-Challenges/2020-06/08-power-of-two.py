# Given an integer, write a function to determine if it is a power of two.

# Solution 1
def is_power_of_two(n):
    if n <= 0: return False
        while n % 2 == 0:
            n /= 2
        return n == 1
    
# Solution 2
def is_power_of_two(n):
    if n <= 0: return False
    if n == 1: return True
    x = 1
    while x < n:
        x = 2 * x
        if x == n:
            return True
    return False
