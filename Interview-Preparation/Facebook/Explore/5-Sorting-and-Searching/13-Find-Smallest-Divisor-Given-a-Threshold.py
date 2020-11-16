def smallestDivisor(nums, threshold):
    def condition(divisor):
        # return sum((num - 1) // divisor + 1 for num in nums) <= threshold
        maxThreshold = 0
        for num in nums:
            maxThreshold += math.ceil(num/divisor)
            # maxThreshold += (num - 1) // divisor + 1
        return maxThreshold <= threshold
        
    lo, hi = 1, max(nums)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if condition(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
