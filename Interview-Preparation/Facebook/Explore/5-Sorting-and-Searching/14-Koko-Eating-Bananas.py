def minEatingSpeed(piles, H):
    # def feasible(speed):
    #     return sum((pile - 1) // speed + 1 for pile in piles) <= H

    def feasible(speed):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile/speed)
            # hours += (pile - 1) // speed + 1
        return hours <= H

    lo, hi = 1, max(piles)
    while lo < hi:
        mid = lo  + (hi - lo) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
