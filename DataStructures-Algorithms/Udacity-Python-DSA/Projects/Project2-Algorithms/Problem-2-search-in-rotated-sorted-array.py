def rotated_array_search(nums, target):
    """
    Find the index by searching in a rotated sorted array

    Args:
       nums(array), target(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # Binary search, O(n log n) in time and O(1) in space
    lo, hi = 0, len(nums)-1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if target == nums[mid]:
            return mid
        # Check which side is sorted
        elif nums[lo] <= nums[mid]: # left side is sorted
            # Check which side contains target and search accordingly
            if target >= nums[lo] and target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else: # right side must be sorted
            # Check which side contains target and search accordingly
            if target > nums[mid] and target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1

# Tests
def linear_search(nums, target):
    for i, num in enumerate(nums):
        if num == target:
            return i
    return -1

def test_function(test_case):
    nums = test_case[0]
    target = test_case[1]
    if linear_search(nums, target) == rotated_array_search(nums, target):
        print("Pass", end=' ')
    else:
        print("Fail", end=' ')

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[1,3], 3])
test_function([[3,1], 1])
test_function([[1,3], 1])
test_function([[3,1], 3])
test_function([[], 1])
# Pass Pass Pass Pass Pass Pass Pass Pass Pass Pass 

