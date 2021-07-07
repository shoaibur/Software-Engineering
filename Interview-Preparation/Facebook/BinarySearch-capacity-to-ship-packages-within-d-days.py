class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        
        def feasible(capacity) -> bool:
            days = 1
            total = 0
            for weight in weights:
                total += weight
                if total > capacity:  # too heavy, wait for the next day
                    total = weight
                    days += 1
                    if days > D:  # cannot ship within D days
                        return False
            return True
        
        lo, hi = max(weights), sum(weights)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
