def deep_reverse(nums):
    if len(nums) <= 1:
        return nums
    out = []
    for i in range(len(nums)-1, -1, -1):
        if type(nums[i]) is int:
            out[i] = nums[i]
        else:
            out[i] = deep_reverse(nums[i])
    return out

def deep_reverse2(nums):
    if len(nums) <= 1: return nums
    i, j = 0, len(nums)-1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        if type(nums[i]) is list:
            nums[i] = deep_reverse2(nums[i])
        if type(nums[j]) is list:
            nums[j] = deep_reverse2(nums[j])
    mid_index = len(nums) // 2
    mid_num = nums[mid_index]
    if type(mid_num) is list:
        nums[mid_index] = deep_reverse2(mid_num)
    return nums
  
