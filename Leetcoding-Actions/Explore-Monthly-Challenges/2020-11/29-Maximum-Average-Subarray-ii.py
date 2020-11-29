class Solution:
    def findMaxAverage(self, nums, k):
        lo, hi = min(nums), max(nums)
        precision = 1E-6
        while lo+precision < hi:
            mid = lo + (hi-lo)/2.0
            if self.can_process(mid, nums, k):
                lo = mid
            else:
                hi = mid
        return lo
    
    def can_process(self, aver, nums, k):      
        sum_so_far = 0
        for i in range(k):
            sum_so_far += nums[i] - aver
        if sum_so_far >= 0:
            return True
        prev, min_so_far = 0.0, 0.0
        for i in range(k, len(nums)):
            sum_so_far += nums[i] - aver
            prev += nums[i-k]-aver
            min_so_far = min(min_so_far, prev)
            if sum_so_far - min_so_far>=0 :
                return True
        return False
