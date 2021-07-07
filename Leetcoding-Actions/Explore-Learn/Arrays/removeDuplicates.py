class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        T: O(n) and S: O(1)
        '''
        if len(nums) <= 1: return len(nums)
        
        i = 0
        currVal = nums[i]
        for j in range(1, len(nums)):
            if nums[j] != currVal:
                i += 1
                nums[i] = nums[j]
                currVal = nums[i]
        return i + 1
