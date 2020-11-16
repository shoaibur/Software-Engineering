def max_sum_subarray(nums):
    if not nums: return nums
    max_sum = nums[0]
    cur_sum = 0
    for i in range(len(nums)):
        cur_sum = max( cur_sum + nums[i], nums[i] )
        max_sum = max( cur_sum, max_sum )
    return max_sum
