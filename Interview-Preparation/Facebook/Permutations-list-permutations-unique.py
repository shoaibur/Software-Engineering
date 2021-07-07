class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        result = set()
        
        def permute(nums):
            if len(nums) <= 1: return [nums]
            
            out = []
            for i in range(len(nums)):
                first = [nums[i]]
                rem = nums[:i] + nums[i+1:]
                for p in permute(rem):
                    out.append(first + p)
            return out
        
        out = permute(nums)
        for item in out:
            result.add(tuple(item))
        return result
