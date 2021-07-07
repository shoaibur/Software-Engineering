# Given an array w of positive integers, where w[i] describes the weight of index i, 
# write a function pickIndex which randomly picks an index in proportion to its weight.

# Example:
# nums = [2, 1, 4, 5]
# cumsum = [2, 3, 7, 12]
# Generate a random number between 1 and 12 (sum of nums), and 
# return the index where the random number falls in the cumsum array.

def random_pick_with_weight(nums):
    cumsum = [nums[0]]
    # O(n)
    for num in nums[1:]:
        cumsum.append(cumsum[-1]+num)
    r = random.randint(1, cumsum[-1])
    # O(n)
    for i in range(len(cumsum)):
        if cumsum[i] >= r:
            return i
    return
  
