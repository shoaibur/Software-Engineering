def get_min_max(nums):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       nums(list): list of integers containing one or more integers
    """
    if len(nums) == 0: raise ValueError('nums must not be empty')
    if len(nums) == 1: return (nums[0], nums[0])
    min_, max_ = nums[0], nums[0] # initialize
    for num in nums[1:]: # One pass traversal, O(n) in time, O(1) in space
        if num < min_:
            min_ = num
        elif num > max_:
            max_ = num
    return (min_, max_)

## Example Test Case of Ten Integers
# import random
# l = [i for i in range(0, 10)]  # a list containing 0 - 9
# random.shuffle(l)
# print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

import unittest
class MinMaxTest(unittest.TestCase):
    def test_case1(self):
        self.assertRaises(ValueError, get_min_max, [])
    
    def test_case2(self):
        self.assertEqual(get_min_max([1]),(1,1))
        
    def test_case3(self): # numbers from 0 to 9
        nums = [i for i in range(0, 10)]
        random.shuffle(nums)
        self.assertEqual(get_min_max(nums),(0,9))
        
    def test_case4(self): # numbers from -100 to 100
        nums = [i for i in range(-100, 101)]
        random.shuffle(nums)
        self.assertEqual(get_min_max(nums),(-100,100))
        
    def test_case5(self):
        self.assertEqual(get_min_max([2,1]),(1,2))        
#     
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
#     
# .....
# ----------------------------------------------------------------------
# Ran 5 tests in 0.009s

# OK
