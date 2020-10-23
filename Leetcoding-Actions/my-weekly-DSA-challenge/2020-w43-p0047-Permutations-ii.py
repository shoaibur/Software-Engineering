class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        '''
        T: O(n!) and S: O(n!)
        '''
        def permute(nums):
            n = len(nums)
            if n <= 1: return [nums]
            
            out = []
            for i in range(n):
                first = [nums[i]]
                rem = nums[:i] + nums[i+1:]
                
                for p in permute(rem):
                    out.append(first + p)
            return out
        
        out = permute(nums)
        return set([tuple(item) for item in out])
    
