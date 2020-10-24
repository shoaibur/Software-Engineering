class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        '''
        nums = [4,9,10,15,18]
        
        At i = 1: num of missing element = 9 - 4 - 1
        At i = 2: num of missing element = 10 - 9 - 1
        At i = 3: num of missing element = 15 - 10 - 1
        
        So, at any index i=3, num of missing element = add of above 3
        = 15 - 4 - 3 = nums[i] - nums[0] - i
        
        T: O(log n) and S: O(1)
        '''
        def countMissing(idx):
            return nums[idx] - nums[0] - idx
        
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if countMissing(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        '''
        At i = lo: num of missing element = countMissing(lo) >= k
        So, consider nums at lo-1 and compute num of missing element at lo-1.
        The k-th missing element = nums[lo - 1] + k - countMissing(lo - 1)
        '''
        return nums[lo - 1] + k - countMissing(lo - 1)
