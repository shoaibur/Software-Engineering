class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) <= 1: return [nums]
        result = []
        for i in range(len(nums)):
            first = [nums[i]]
            rem = nums[:i] + nums[i+1:]
            for perm in self.permute(rem):
                result.append(first+perm)
        return result
