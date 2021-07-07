class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        1   2   3   4
        1   1   2   6
        24  12  4   1
        '''
        '''
        left = [1] * len(nums)
        right = [1] * len(nums)
        
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
            
        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] = left[i] * right[i]
        return result
        '''
        
        left = [1] * len(nums)
        
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
            
        right = 1
        for i in range(len(nums)-1, -1, -1):
            left[i] = left[i] * right
            right *= nums[i]
        return left
