# Given a sorted array and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.

def searchInsert(nums, target):
    if not nums: return None
    low, high = 0, len(nums)-1
    while low <= high:
        mid = (low+high) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return low
