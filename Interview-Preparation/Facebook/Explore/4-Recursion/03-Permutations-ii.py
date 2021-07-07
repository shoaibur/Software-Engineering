class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def permute(nums):
            if len(nums) <= 1: return [nums]

            permutations = []
            for i in range(len(nums)):
                first = [nums[i]]
                rem = nums[:i] + nums[i+1:]
                for perm in permute(rem):
                    permutations.append(first + perm)
            return permutations
        
        permutations = permute(nums)
                
        uniquePermutations = set()
        for item in permutations:
            uniquePermutations.add(tuple(item))
        return uniquePermutations
