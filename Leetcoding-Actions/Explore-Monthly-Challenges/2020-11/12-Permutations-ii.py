class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        '''
        T: O(n!) and S: O(n!)
        '''
        def permute(nums):
            if len(nums) <= 1: return [nums]
            permutations = []
            for i in range(len(nums)):
                first = [nums[i]]
                rem = nums[:i] + nums[i+1:]
                for p in permute(rem):
                    permutations.append(first + p)
            return permutations
        
        permutations = permute(nums)
        result = set()
        for item in permutations:
            result.add( tuple(item) )
        return result
