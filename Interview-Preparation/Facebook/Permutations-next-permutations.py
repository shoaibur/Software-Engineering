class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        4 2 4 || 6 5 3 1
        4 2 5 1 3 4 6
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1: return
        
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                break
                
        if i == 0 and nums[0] > nums[1]:
            nums[:] = nums[::-1]
            return
        
        for j in range(len(nums)-1, i, -1):
            if nums[j] > nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                break
        i = i + 1
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1
        return
