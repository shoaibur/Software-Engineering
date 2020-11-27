# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the 
# same color are adjacent, with the colors in the order red, white and blue.
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

def sort_colors(nums):
    pos0 = 0
    pos2 = len(nums) - 1
    i = 0
    while i <= pos2 and pos0 < pos2:
        if nums[i] == 0:
            nums[pos0], nums[i] = nums[i], nums[pos0]
            pos0 += 1
            i += 1
        elif nums[i] == 2:
            nums[i], nums[pos2] = nums[pos2], nums[i]
            pos2 -= 1
        else:
            i += 1
    return nums

# Test
nums = [0, 1, 1, 0, 2, 1, 1, 2]
sort_colors(nums) # [0, 0, 1, 1, 1, 1, 2, 2]
