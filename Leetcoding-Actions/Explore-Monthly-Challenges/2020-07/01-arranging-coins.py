# You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
# Given n, find the total number of full staircase rows that can be formed.
# n is a non-negative integer and fits within the range of a 32-bit signed integer.

# Solution:
# k(k+1)/2 <= n
# k2 + k - 2n <= 0

def arrangeCoins(n):
    # O(1) time, O(1) space
    a = int(-1/2 + math.sqrt( 1 + 8 * n ) / 2)
    b = int(-1/2 - math.sqrt( 1 + 8 * n ) / 2)
    return max(a, b)

