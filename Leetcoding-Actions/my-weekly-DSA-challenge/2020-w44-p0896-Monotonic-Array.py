class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        '''
        T: O(n) and S: O(n)
        '''
        
        def isIncreasing(nums):
            for i in range(1, len(nums)):
                if nums[i-1] > nums[i]:
                    return False
            return True
        
        return isIncreasing(A) or isIncreasing(A[::-1])
