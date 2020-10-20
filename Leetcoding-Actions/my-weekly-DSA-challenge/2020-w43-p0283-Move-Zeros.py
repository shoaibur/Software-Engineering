class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        T: O(n) and S: O(1)
        """
        n = len(nums)
        if n <= 1: return
        
        for i in range(n):
            if nums[i] == 0:
                break
        if i == n-1: return
        
        j = i + 1
        while j < n:
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
            
        return
