class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def permute(nums):
            if len(nums) <= 1: return [nums]
            out = []
            for i in range(len(nums)):
                first = [nums[i]]
                rem = nums[:i] + nums[i+1:]
                for perm in permute(rem):
                    out.append(first+perm)
            return out
        
        out = permute(nums)
        print(out)
        result = set()
        for item in out:
            result.add(tuple(item))
        return result
