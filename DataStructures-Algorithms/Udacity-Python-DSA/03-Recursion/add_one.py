def add_one(nums):
    if not nums: return []
    if nums == [9]:
        return [1, 0]
    if nums[-1] < 9:
        nums[-1] += 1
        return nums
    return add_one(nums[:-1]) + [0]
  
