class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        '''
        T: O(n) and S: O(n)
        '''
        nums = [lower - 1] + nums + [upper + 1]
        result = []
        for i in range(len(nums)-1):
            diff = nums[i+1] - nums[i]
            if diff <= 1: continue
            lo = max(nums[i] + 1, lower)
            hi = min(nums[i+1] - 1, upper)
            if lo == hi:
                result.append(str(lo))
            else:
                result.append(str(lo)+"->"+str(hi))
        return result
            
