class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        
        def feasible(threshold) -> bool:
            count = 1
            total = 0
            for num in nums:
                total += num
                if total > threshold:
                    total = num
                    count += 1
                    if count > m:
                        return False
            return True
        
        lo, hi = max(nums), sum(nums)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
