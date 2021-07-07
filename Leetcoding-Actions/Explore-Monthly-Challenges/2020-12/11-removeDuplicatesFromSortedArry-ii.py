class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, count = 1, 1
        for j in range(1, len(nums)):
            if nums[j - 1] == nums[j]:
                count += 1
            else:
                count = 1
            
            if count <= 2:
                nums[i] = nums[j]
                i += 1
                
        return i
