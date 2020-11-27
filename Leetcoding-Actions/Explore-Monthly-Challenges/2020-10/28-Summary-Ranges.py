class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        '''
        T: O(n) and S: O(1)
        '''
        
        if not nums: return []
        if len(nums) == 1: return [str(nums[0])]
        
        result = []
        start = nums[0]
        prev = nums[0]
        
        for end in nums[1:]:
            if end - prev != 1:
                s = str(start) + '->' + str(prev) if start != prev else str(start)
                result.append(s)
                start = end
            prev = end
        
        s = str(start) + '->' + str(prev) if start != prev else str(start)
        result.append(s)
        
        return result
