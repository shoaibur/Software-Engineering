class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        '''
        [[5,4],[6,4],[6,7],[2,3]]
        [[2,3],[5,4],[6,7],[6,4]]
        '''
        n = len(envelopes)
        if n <= 1: return n
        
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        nums = [env[1] for env in envelopes]
        
        def binarySearch(nums, target):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if nums[mid] >= target:
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        
        def lis(nums):
            result = []
            for num in nums:
                i = binarySearch(result, num)
                if i == len(result):
                    result.append(num)
                else:
                    result[i] = num
            return result
        
        return len( lis(nums) )
