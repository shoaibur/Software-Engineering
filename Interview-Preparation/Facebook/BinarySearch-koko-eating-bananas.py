class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        
        def feasible(speed) -> bool:
            return sum((pile - 1) // speed + 1 for pile in piles) <= H
        
        # def feasible(speed) -> bool:
        #     hours = 0
        #     for pile in piles:
        #         # hours += math.ceil(pile/speed)
        #         hours += (pile - 1) // speed + 1
        #     return hours <= H

        left, right = 1, max(piles)
        while left < right:
            mid = left  + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
    
    
