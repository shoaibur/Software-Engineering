def all_subsets(nums):
    out = [[]]
    for num in nums:
        out += [cur+[num] for cur in out]
    return out
  
