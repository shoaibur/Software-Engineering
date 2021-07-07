class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        '''
        T: O(n log3) = O(n) and S: O(1)
        '''
        def binarySearch(nums, target):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if nums[mid] >= target:
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        
        n = len(nums)
        if n < 3: return False
        
        incSubSeq = []
        for num in nums:
            i = binarySearch(incSubSeq, num)
            if i == len(incSubSeq):
                incSubSeq.append(num)
            else:
                incSubSeq[i] = num
            
            if len(incSubSeq) == 3:
                return True
        return False
