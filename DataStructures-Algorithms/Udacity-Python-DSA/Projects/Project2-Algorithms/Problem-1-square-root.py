def sqrt(n):
    """
    Calculate the floored square root of a number

    Args:
       n(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    # Check for negative numbers
    if n < 0:
        raise ValueError('math domain error')
    # Base case
    if n <= 1: return n
    
    # Binary search, O(log n) in time, O(1) in space
    lo, hi = 0, n
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        mid2 = mid * mid
        if mid2 == n:
            return mid
        elif mid2 < n:
            lo = mid+1
            out = mid
        else:
            hi = mid-1
    return out

# Tests
# print ("Pass" if  (3 == sqrt(9)) else "Fail")
# print ("Pass" if  (0 == sqrt(0)) else "Fail")
# print ("Pass" if  (4 == sqrt(16)) else "Fail")
# print ("Pass" if  (1 == sqrt(1)) else "Fail")
# print ("Pass" if  (5 == sqrt(27)) else "Fail")
# Pass Pass Pass Pass Pass

import unittest
class SimpleTest(unittest.TestCase):
    
    def test_case1(self):
        self.assertEqual(3, sqrt(9))
        
    def test_case2(self):
        self.assertEqual(0, sqrt(0))
        
    def test_case3(self):
        self.assertEqual(4, sqrt(16))
        
    def test_case4(self):
        self.assertEqual(1, sqrt(1))
        
    def test_case5(self):
        self.assertEqual(5, sqrt(27))
        
    def test_case6(self): # sqrt of large numbers
        import math
        n = range(10000,1000000,98765)
        mathsqrt = [int(math.sqrt(i)) for i in n]
        testsqrt = [sqrt(i) for i in n]
        self.assertEqual(mathsqrt, testsqrt)
        
    def test_case7(self): # sqrt of negative numbers
        self.assertRaises(ValueError, sqrt, -5)
# 
if __name__ == '__main__':
    #unittest.main()
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
#     
# .......
# ----------------------------------------------------------------------
# Ran 7 tests in 0.010s

# OK


